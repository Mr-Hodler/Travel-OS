#!/usr/bin/env python3
"""Build every skill in skills/ into an installable dist/<name>.skill package.

A .skill file is a zip with SKILL.md at the archive root.

Two things this script exists to prevent, both of which shipped silently once:

1. **Frontmatter that does not parse.** A description written as a plain scalar
   containing ": " breaks YAML. The file looks fine, the skill never installs,
   and nothing says why. Descriptions are therefore validated as real YAML.

2. **Shared references that never reach the package.** Skills that cite a
   repo-root-relative path only resolve standalone if that file travels with
   them, so SHARED is bundled into every archive. Without it, an installed
   skill points at files that are not there.

Usage:
    python3 scripts/build.py                 # build all
    python3 scripts/build.py business-plan market-research   # build named skills
    python3 scripts/build.py --check         # verify only, build nothing
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "skills", ROOT / "dist"

# archive path -> source dir. Bundled into EVERY package so repo-root-relative
# citations resolve when a skill is installed on its own.
SHARED = {"knowledge": ROOT / "knowledge"}

# Single files bundled into every package. The licence travels with the skill:
# a package that leaves this repo without its terms attached is a package that
# looks unowned.
SHARED_FILES = {"LICENSE": ROOT / "LICENSE"}

SKIP_NAMES = {".DS_Store", "Thumbs.db"}
SKIP_DIRS = {"__pycache__", ".ipynb_checkpoints"}
DESC_LIMIT = 1024  # hard frontmatter limit; over this the skill will not install


def parse_frontmatter(text: str) -> tuple[dict, str | None]:
    """Return (fields, error). Uses PyYAML when available: it is the same parser
    the loader uses, so it catches breakage a regex would wave through."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}, "no YAML frontmatter"
    block = m.group(1)

    try:
        import yaml  # type: ignore
    except ImportError:
        pass
    else:
        try:
            d = yaml.safe_load(block)
        except Exception as e:  # noqa: BLE001 - report whatever YAML complains about
            return {}, f"YAML does not parse: {str(e).splitlines()[0]}"
        return (d if isinstance(d, dict) else {}), None

    # Fallback parser. Approximates YAML, so it also checks the one construct
    # that silently breaks it: a plain scalar containing ": ".
    out, key, buf, folded = {}, None, [], False
    for line in block.split("\n"):
        m2 = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if m2 and not (folded and line.startswith(("  ", "\t"))):
            if key:
                out[key] = " ".join(buf).strip()
            key, rest = m2.group(1), m2.group(2).strip()
            folded = rest in (">-", ">", "|", "|-")
            if not folded and ": " in rest and rest[0] not in "\"'":
                return {}, f"'{key}' is a plain scalar containing ': ' - YAML will not parse it"
            buf = [] if folded else [rest]
        elif key:
            buf.append(line.strip())
    if key:
        out[key] = " ".join(buf).strip()
    return out, None


def check(name: str) -> list[str]:
    """Problems that would stop this skill installing."""
    p = SRC / name / "SKILL.md"
    if not p.exists():
        return [f"no SKILL.md in skills/{name}/"]
    fm, err = parse_frontmatter(p.read_text())
    if err:
        return [err]
    problems = []
    if fm.get("name") != name:
        problems.append(f"frontmatter name '{fm.get('name')}' != folder '{name}'")
    d = len((fm.get("description") or "").strip())
    if d == 0:
        problems.append("empty description")
    elif d >= DESC_LIMIT:
        problems.append(f"description {d} chars, limit {DESC_LIMIT}")
    return problems


# A skill that tells the agent to read a file which is not there does not error.
# It just proceeds without the rules it was told to follow, which is worse.
# config/ is exempt: those resolve to a gitignored personal copy, then to the
# committed .example.md fallback, which is a documented pattern rather than a gap.
CITATION = re.compile(
    r"(?<![\w/.-])((?:\.\./)?(?:references|templates|examples|adapters|knowledge)"
    r"/[A-Za-z0-9_./-]+\.(?:md|yml|yaml|json|csv|html))"
)

# A cross-skill citation. It is legal - the file exists in a sibling skill - but a
# zip cannot hold a path above its own root, so it only resolves once BOTH skills
# are installed. Written without "../" it resolves to nothing at all, which is the
# defect this pattern exists to catch.
SIBLING = re.compile(
    r"(?<![\w/.-])(?:\.\./)?([a-z][a-z0-9-]+)/((?:references|assets)"
    r"/[A-Za-z0-9_./-]+\.(?:md|yml|yaml|json|csv|html))"
)


# A skill may legitimately name a file it has not written yet, as long as it says
# so. Those lines are declarations of intent, not broken reads, so they are not
# reported - but only when the skill is explicit about it.
DEFERRED = ("not yet created", "to create", "to be created", "roadmap", "planned",
            "created at runtime", "to be written", "future", "placeholder", "draft")


def dangling(name: str) -> list[str]:
    """Input files a skill says it reads, that do not exist."""
    skill_dir = SRC / name
    missing: set[str] = set()
    for f in skill_dir.rglob("*.md"):
        section, block = "", ""   # section holds until the next heading; block until a blank line
        for line in f.read_text(errors="ignore").split("\n"):
            stripped = line.strip()
            if stripped.startswith("#"):
                section, block = stripped.lower(), ""
            elif stripped.startswith("**") and not CITATION.search(stripped):
                block = stripped.lower()
            elif not stripped:
                block = ""
            context = f"{section} {block} {stripped}".lower()
            if any(d in context for d in DEFERRED):
                continue
            for cite in CITATION.findall(line):
                target = cite[3:] if cite.startswith("../") else cite
                if cite.startswith("../"):
                    ok = (skill_dir.parent / target).exists() or (ROOT / target).exists()
                else:
                    ok = (skill_dir / cite).exists() or (ROOT / cite).exists()
                if not ok:
                    missing.add(cite)

            # A sibling's file cited without "../" points inside this skill and
            # resolves to nothing. Report it with the correction.
            for sib, rest in SIBLING.findall(line):
                if sib == name or not (SRC / sib).is_dir():
                    continue
                if f"../{sib}/{rest}" in line:
                    continue
                if (SRC / sib / rest).exists():
                    missing.add(f"{sib}/{rest}  (sibling skill - write ../{sib}/{rest})")
    return sorted(missing)


def build(name: str) -> Path:
    skill_dir = SRC / name
    OUT.mkdir(exist_ok=True)
    target = OUT / f"{name}.skill"
    written: set[str] = set()

    def add(z: zipfile.ZipFile, f: Path, arc: str) -> None:
        if f.name in SKIP_NAMES or any(part in SKIP_DIRS for part in f.parts):
            return
        if f.suffix == ".pyc" or re.search(r"\.(bak[0-9]*|tmp|orig|rej)$", f.name):
            return
        if arc in written:
            return
        # Fixed timestamp: a rebuild with no content change must produce an
        # identical file, or every build shows up as a diff in git.
        info = zipfile.ZipInfo(arc, date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, f.read_bytes())
        written.add(arc)

    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file():
                add(z, f, str(f.relative_to(skill_dir)))
        for arc_prefix, base in SHARED.items():
            if not base.exists():
                continue
            for f in sorted(base.rglob("*")):
                if f.is_file():
                    add(z, f, f"{arc_prefix}/{f.relative_to(base)}")
        for arc, src in SHARED_FILES.items():
            if src.exists():
                add(z, src, arc)
    return target


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv
    names = args or sorted(d.name for d in SRC.iterdir() if d.is_dir())

    failed, warned = 0, 0
    for n in names:
        problems = check(n)
        if problems:
            failed += 1
            print(f"  FAIL {n:24s} {'; '.join(problems)}")
            continue
        gaps = dangling(n)
        if check_only:
            print(f"  ok   {n}")
        else:
            p = build(n)
            with zipfile.ZipFile(p) as z:
                names_in = z.namelist()
                shared_ok = not SHARED or any(k in m for m in names_in for k in SHARED)
            flag = "" if shared_ok else "   <-- SHARED MISSING"
            print(f"  ok   {n:24s} {len(names_in):3} files  {p.stat().st_size/1024:7.1f} KB{flag}")
        if gaps:
            warned += 1
            print(f"       cites {len(gaps)} file(s) that do not exist: {', '.join(gaps)}")

    print(f"\n{len(names) - failed}/{len(names)} "
          f"{'verified' if check_only else 'built'}"
          f"{'' if not failed else f', {failed} FAILED'}"
          f"{'' if not warned else f', {warned} with dangling citations'}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
