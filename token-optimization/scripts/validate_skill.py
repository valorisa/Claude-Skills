#!/usr/bin/env python3
"""
Token Optimization Skill Validator

Validates skill structure, frontmatter, and content quality.
"""

from pathlib import Path
import re
import sys
import yaml


def validate_skill(skill_dir: Path) -> list[str]:
    """Validate skill structure and content."""
    errors = []
    skill_md = skill_dir / "SKILL.md"

    # Check file exists
    if not skill_md.exists():
        errors.append("[ERROR] Missing SKILL.md (case-sensitive)")
        return errors

    content = skill_md.read_text(encoding="utf-8")

    # Check frontmatter
    if not content.startswith("---"):
        errors.append("[ERROR] Missing YAML frontmatter (must start with ---)")

    # Extract and parse frontmatter
    try:
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            errors.append("[ERROR] Invalid frontmatter structure")
        else:
            fm = yaml.safe_load(fm_match.group(1))

            # Check required fields
            if "name" not in fm:
                errors.append("[ERROR] Missing 'name' in frontmatter")
            elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", fm["name"]):
                errors.append(f"[ERROR] Invalid name '{fm['name']}' (must be kebab-case)")

            # Verify folder name matches
            if skill_dir.name != fm.get("name"):
                errors.append(f"[WARNING] Folder name '{skill_dir.name}' != skill name '{fm.get('name')}'")

            if "description" not in fm:
                errors.append("[ERROR] Missing 'description' in frontmatter")
            elif len(fm["description"]) < 50:
                errors.append("[WARNING] Description very short (<50 chars)")
            elif len(fm["description"]) > 1024:
                errors.append("[ERROR] Description too long (>1024 chars)")

            # Check for trigger language
            desc = fm.get("description", "").lower()
            trigger_words = ["use when", "trigger", "asks to", "says", "mentions"]
            if not any(tw in desc for tw in trigger_words):
                errors.append("[WARNING] Description missing explicit trigger phrases")

            # Check metadata if present
            if "metadata" in fm:
                meta = fm["metadata"]
                if "category" in meta:
                    valid_categories = ["document-creation", "workflow-automation", "mcp-enhancement"]
                    if meta["category"] not in valid_categories:
                        errors.append(f"[WARNING] Unknown category '{meta['category']}'")

    except yaml.YAMLError as e:
        errors.append(f"[ERROR] Invalid YAML: {e}")

    # Security checks
    if "<" in content and ">" in content:
        # Allow markdown links but flag potential XML
        if re.search(r"<[a-z][a-z0-9]*>", content, re.IGNORECASE):
            errors.append("[WARNING] Possible XML tags detected (review manually)")

    # Check content length
    if len(content) < 500:
        errors.append("[WARNING] SKILL.md suspiciously short (<500 chars)")

    # Check for essential sections
    body = content[fm_match.end():] if fm_match else content

    if "## " not in body:
        errors.append("[WARNING] No H2 sections found (consider adding structure)")

    if "example" not in body.lower():
        errors.append("[WARNING] No examples found (consider adding usage examples)")

    # Check references directory
    ref_dir = skill_dir / "references"
    if ref_dir.exists():
        ref_files = list(ref_dir.glob("*.md"))
        if not ref_files:
            errors.append("[WARNING] references/ directory exists but is empty")

    # Check tests directory
    test_dir = skill_dir / "tests"
    if test_dir.exists():
        trigger_tests = test_dir / "trigger-tests.md"
        functional_tests = test_dir / "functional-tests.md"

        if not trigger_tests.exists():
            errors.append("[WARNING] Missing tests/trigger-tests.md")
        if not functional_tests.exists():
            errors.append("[WARNING] Missing tests/functional-tests.md")
    else:
        errors.append("[WARNING] No tests/ directory (consider adding test cases)")

    return errors


def main():
    """Main validation entry point."""
    if len(sys.argv) > 1:
        skill_path = Path(sys.argv[1])
    else:
        skill_path = Path(".")

    if not skill_path.exists():
        print(f"[ERROR] Path does not exist: {skill_path}")
        sys.exit(1)

    print(f"\nValidating skill: {skill_path.name}\n")

    errors = validate_skill(skill_path)

    if errors:
        for err in errors:
            print(err)
        print()

        # Exit with error only if critical issues found
        critical = any("[ERROR]" in e for e in errors)
        if critical:
            print("[ERROR] Validation failed (critical issues found)")
            sys.exit(1)
        else:
            print("[WARNING] Validation passed with warnings")
            sys.exit(0)
    else:
        print(f"[OK] Skill validation passed: {skill_path.name}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
