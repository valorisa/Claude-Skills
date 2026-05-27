#!/usr/bin/env python3
"""
Skill Validator - Validates Claude skill structure and content
Based on Anthropic's official skill guidelines (Feb 2026)

Usage:
    python validate_skill.py <skill_directory>
    python validate_skill.py .  # Validate current directory
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

try:
    import yaml
except ImportError:
    print("⚠️  PyYAML not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
    import yaml


class SkillValidator:
    """Validates Claude skill structure and content."""

    # Reserved prefixes (Anthropic guidelines)
    RESERVED_PREFIXES = ["claude-", "anthropic-"]

    # Valid kebab-case pattern
    KEBAB_CASE_PATTERN = r"^[a-z0-9]+(-[a-z0-9]+)*$"

    # Trigger words that should appear in description
    TRIGGER_WORDS = ["use when", "trigger", "asks to", "says", "mentions", "uploads"]

    def __init__(self, skill_dir: Path):
        self.skill_dir = skill_dir
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def validate(self) -> Tuple[bool, List[str], List[str], List[str]]:
        """Run all validation checks. Returns (success, errors, warnings, info)."""

        # Phase 1: File structure
        self._check_skill_file_exists()

        if not (self.skill_dir / "SKILL.md").exists():
            # Can't continue without SKILL.md
            return False, self.errors, self.warnings, self.info

        # Phase 2: Frontmatter
        content = (self.skill_dir / "SKILL.md").read_text(encoding="utf-8")
        frontmatter, body = self._extract_frontmatter(content)

        if frontmatter:
            self._check_frontmatter_structure(frontmatter, content)
            self._check_frontmatter_fields(frontmatter)
            self._check_security(frontmatter, content)

        # Phase 3: Content quality
        if body:
            self._check_content_length(body)
            self._check_instruction_quality(body)

        # Phase 4: File organization
        self._check_folder_structure()

        # Phase 5: Naming consistency
        if frontmatter and "name" in frontmatter:
            self._check_name_consistency(frontmatter["name"])

        success = len(self.errors) == 0
        return success, self.errors, self.warnings, self.info

    def _check_skill_file_exists(self):
        """Check SKILL.md exists with exact spelling."""
        skill_file = self.skill_dir / "SKILL.md"

        if not skill_file.exists():
            # Check for common misspellings
            alternatives = list(self.skill_dir.glob("*skill*.md"))
            if alternatives:
                alt_names = [f.name for f in alternatives]
                self.errors.append(
                    f"❌ Missing SKILL.md (case-sensitive). Found: {', '.join(alt_names)}"
                )
            else:
                self.errors.append("❌ Missing SKILL.md (case-sensitive)")
        else:
            self.info.append("✅ SKILL.md found")

    def _extract_frontmatter(self, content: str) -> Tuple[dict, str]:
        """Extract YAML frontmatter and body content."""
        if not content.startswith("---"):
            self.errors.append("❌ Missing YAML frontmatter (must start with ---)")
            return {}, content

        # Match frontmatter block
        match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
        if not match:
            self.errors.append("❌ Invalid frontmatter structure (must end with ---)")
            return {}, content

        fm_text, body = match.groups()

        # Parse YAML
        try:
            frontmatter = yaml.safe_load(fm_text)
            if not isinstance(frontmatter, dict):
                self.errors.append("❌ Frontmatter must be a YAML object (key-value pairs)")
                return {}, body
            self.info.append("✅ Frontmatter structure valid")
            return frontmatter, body
        except yaml.YAMLError as e:
            self.errors.append(f"❌ Invalid YAML syntax: {e}")
            return {}, body

    def _check_frontmatter_structure(self, fm: dict, content: str):
        """Check frontmatter has proper --- delimiters."""
        lines = content.split("\n")

        # Check first line
        if lines[0] != "---":
            self.errors.append("❌ Frontmatter must start with --- on its own line")

        # Find closing ---
        closing_line = None
        for i, line in enumerate(lines[1:], start=1):
            if line == "---":
                closing_line = i
                break

        if closing_line is None:
            self.errors.append("❌ Frontmatter must end with --- on its own line")

    def _check_frontmatter_fields(self, fm: dict):
        """Check required and optional frontmatter fields."""

        # Required: name
        if "name" not in fm:
            self.errors.append("❌ Missing required field: 'name'")
        else:
            name = fm["name"]

            # Check name is kebab-case
            if not re.match(self.KEBAB_CASE_PATTERN, name):
                self.errors.append(
                    f"❌ Invalid name '{name}' (must be kebab-case: lowercase, hyphens only)"
                )
            else:
                self.info.append(f"✅ Name '{name}' is valid kebab-case")

            # Check for reserved prefixes
            for prefix in self.RESERVED_PREFIXES:
                if name.startswith(prefix):
                    self.errors.append(
                        f"❌ Name '{name}' uses reserved prefix '{prefix}' (reserved for Anthropic)"
                    )

        # Required: description
        if "description" not in fm:
            self.errors.append("❌ Missing required field: 'description'")
        else:
            desc = fm["description"]

            # Check description length
            if len(desc) < 50:
                self.warnings.append(
                    f"⚠️  Description very short ({len(desc)} chars). "
                    "Recommend 100-500 chars with trigger phrases."
                )
            elif len(desc) > 1024:
                self.errors.append(
                    f"❌ Description too long ({len(desc)} chars). Max 1024 characters."
                )
            else:
                self.info.append(f"✅ Description length OK ({len(desc)} chars)")

            # Check for trigger language
            desc_lower = desc.lower()
            has_trigger = any(tw in desc_lower for tw in self.TRIGGER_WORDS)
            if not has_trigger:
                self.warnings.append(
                    "⚠️  Description missing trigger phrases. "
                    f"Should include: {', '.join(self.TRIGGER_WORDS[:3])}, etc."
                )
            else:
                self.info.append("✅ Description includes trigger language")

        # Optional but recommended: metadata
        if "metadata" in fm:
            meta = fm["metadata"]
            if not isinstance(meta, dict):
                self.warnings.append("⚠️  'metadata' should be an object (key-value pairs)")
            else:
                # Check recommended metadata fields
                if "author" not in meta:
                    self.info.append("💡 Consider adding 'metadata.author'")
                if "version" not in meta:
                    self.info.append("💡 Consider adding 'metadata.version'")
                if "category" in meta:
                    valid_categories = ["document-creation", "workflow-automation", "mcp-enhancement"]
                    if meta["category"] not in valid_categories:
                        self.warnings.append(
                            f"⚠️  Unknown category '{meta['category']}'. "
                            f"Valid: {', '.join(valid_categories)}"
                        )

    def _check_security(self, fm: dict, content: str):
        """Check for security issues."""

        # Check for XML angle brackets in frontmatter (injection risk)
        fm_text = yaml.dump(fm)
        if "<" in fm_text or ">" in fm_text:
            self.errors.append(
                "❌ XML angle brackets (<, >) forbidden in frontmatter (security risk)"
            )

        # Check for hardcoded credentials
        sensitive_patterns = [
            r"password\s*[:=]\s*['\"]?\w+",
            r"api[_-]?key\s*[:=]\s*['\"]?\w+",
            r"secret\s*[:=]\s*['\"]?\w+",
            r"token\s*[:=]\s*['\"]?\w+",
        ]

        for pattern in sensitive_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.warnings.append(
                    "⚠️  Possible hardcoded credential detected. "
                    "Never commit API keys or passwords."
                )
                break

    def _check_content_length(self, body: str):
        """Check SKILL.md body length (token efficiency)."""
        word_count = len(body.split())

        if word_count < 100:
            self.warnings.append(
                f"⚠️  SKILL.md body very short ({word_count} words). "
                "Should include instructions, examples, error handling."
            )
        elif word_count > 5000:
            self.warnings.append(
                f"⚠️  SKILL.md body very long ({word_count} words). "
                "Consider moving details to references/ for token efficiency."
            )
        else:
            self.info.append(f"✅ Content length reasonable ({word_count} words)")

    def _check_instruction_quality(self, body: str):
        """Check for instruction quality markers."""

        # Check for key sections
        required_sections = ["## Instructions", "## Examples", "## Troubleshooting"]
        for section in required_sections:
            if section.lower() not in body.lower():
                self.warnings.append(f"⚠️  Missing recommended section: {section}")

        # Check for validation gates
        if "⛔" in body or "STOP" in body or "DO NOT" in body:
            self.info.append("✅ Includes explicit validation gates")
        else:
            self.info.append(
                "💡 Consider adding validation gates (⛔, STOP, DO NOT) for critical steps"
            )

        # Check for references to reference files
        if "references/" in body:
            self.info.append("✅ Uses progressive disclosure (links to references/)")
        else:
            self.info.append(
                "💡 Consider moving detailed docs to references/ and linking"
            )

    def _check_folder_structure(self):
        """Check optional folder structure."""

        # Check for README.md in skill folder (should not exist)
        if (self.skill_dir / "README.md").exists():
            self.warnings.append(
                "⚠️  README.md found in skill folder. "
                "Skill folders should NOT contain README.md. "
                "Documentation should be in SKILL.md or references/."
            )

        # Check for recommended folders
        if (self.skill_dir / "references").is_dir():
            self.info.append("✅ references/ folder found")

        if (self.skill_dir / "scripts").is_dir():
            self.info.append("✅ scripts/ folder found")

        if (self.skill_dir / "tests").is_dir():
            self.info.append("✅ tests/ folder found")

    def _check_name_consistency(self, skill_name: str):
        """Check folder name matches skill name."""
        folder_name = self.skill_dir.name

        if folder_name != skill_name:
            self.warnings.append(
                f"⚠️  Folder name '{folder_name}' != skill name '{skill_name}'. "
                "Recommend matching for consistency."
            )
        else:
            self.info.append(f"✅ Folder name matches skill name '{skill_name}'")


def main():
    """CLI entry point."""
    # Fix Windows console encoding for emoji output
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <skill_directory>")
        print("Example: python validate_skill.py .")
        sys.exit(1)

    skill_path = Path(sys.argv[1]).resolve()

    if not skill_path.is_dir():
        print(f"❌ Error: '{skill_path}' is not a directory")
        sys.exit(1)

    print(f"\n🔍 Validating skill: {skill_path.name}")
    print(f"📁 Location: {skill_path}\n")

    validator = SkillValidator(skill_path)
    success, errors, warnings, info = validator.validate()

    # Print results
    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(f"   {error}")
        print()

    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   {warning}")
        print()

    if info:
        print("ℹ️  INFO:")
        for i in info:
            print(f"   {i}")
        print()

    # Summary
    if success:
        print("✅ Skill validation PASSED")
        print(f"   {len(warnings)} warning(s), {len(info)} info message(s)\n")
        sys.exit(0)
    else:
        print(f"❌ Skill validation FAILED")
        print(f"   {len(errors)} error(s), {len(warnings)} warning(s)\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
