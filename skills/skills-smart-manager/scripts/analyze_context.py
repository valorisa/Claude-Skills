#!/usr/bin/env python3
"""
Skills Smart Manager — Context Analysis Engine

Analyzes active Claude Code skills and recommends optimizations to reduce
token waste and improve session performance.

Usage:
    python3 analyze_context.py --action scan
    python3 analyze_context.py --action unload --skill diagnose
    python3 analyze_context.py --action health-check
    python3 analyze_context.py --action gc
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


# Configuration
STALENESS_THRESHOLD = 15  # turns without invocation before considered stale
CONTEXT_THRESHOLD = 60    # percentage before triggering auto-recommendations


class ContextAnalyzer:
    """Analyzes Claude Code context and skill usage."""

    def __init__(self, staleness_threshold: int = STALENESS_THRESHOLD):
        self.staleness_threshold = staleness_threshold
        self.skills_dir = Path.home() / ".claude" / "skills"
        self.project_root = Path.cwd()

    def scan(self) -> Dict:
        """
        Scan current session and return analysis.

        Returns:
            Dict with active_skills, last_invoked, token_footprint, etc.
        """
        # NOTE: This is a simplified implementation
        # In production, this would integrate with Claude Code's internal APIs

        # Detect project type
        project_type = self._detect_project_type()

        # Get active skills (simulated — would need Claude Code API)
        active_skills = self._get_active_skills()

        # Estimate token footprint per skill
        token_footprint = self._estimate_token_footprint(active_skills)

        # Get invocation history (simulated)
        last_invoked = self._get_last_invoked(active_skills)

        # Calculate context percentage (simulated)
        context_percentage = self._estimate_context_percentage()

        return {
            "active_skills": active_skills,
            "last_invoked": last_invoked,
            "estimated_token_footprint": token_footprint,
            "total_skill_tokens": sum(token_footprint.values()),
            "context_percentage": context_percentage,
            "project_type_detected": project_type,
            "timestamp": datetime.now().isoformat()
        }

    def _detect_project_type(self) -> str:
        """Detect project type based on files in working directory."""
        indicators = {
            "rust-cargo": ["Cargo.toml"],
            "nodejs-npm": ["package.json"],
            "python-pip": ["requirements.txt", "pyproject.toml", "setup.py"],
            "docker": ["Dockerfile", "docker-compose.yml"],
            "go": ["go.mod"],
            "java-maven": ["pom.xml"],
            "java-gradle": ["build.gradle"],
            "ruby": ["Gemfile"],
            "php-composer": ["composer.json"]
        }

        for project_type, files in indicators.items():
            if any((self.project_root / f).exists() for f in files):
                return project_type

        return "unknown"

    def _get_active_skills(self) -> List[str]:
        """
        Get list of active skills in current session.

        NOTE: This is simulated. Real implementation would query Claude Code.
        """
        # In production, this would read from Claude Code's session state
        # For now, return example data

        if not self.skills_dir.exists():
            return []

        # List all installed skills
        installed = [
            d.name for d in self.skills_dir.iterdir()
            if d.is_dir() and (d / "SKILL.md").exists()
        ]

        return installed

    def _estimate_token_footprint(self, skills: List[str]) -> Dict[str, int]:
        """
        Estimate token footprint for each skill.

        Rough approximation: 1 character ≈ 0.25 tokens
        """
        footprint = {}

        for skill in skills:
            skill_md = self.skills_dir / skill / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text()
                # Rough token estimate: 4 chars per token
                tokens = len(content) // 4
                footprint[skill] = tokens
            else:
                footprint[skill] = 0

        return footprint

    def _get_last_invoked(self, skills: List[str]) -> Dict[str, int]:
        """
        Get turns since last invocation for each skill.

        NOTE: Simulated. Real version would track from Claude session history.
        """
        # In production, read from session history
        # For demonstration, return placeholder values

        return {skill: 0 for skill in skills}

    def _estimate_context_percentage(self) -> int:
        """
        Estimate current context window usage percentage.

        NOTE: Simulated. Real version would query Claude Code.
        """
        # Placeholder — real implementation would query context API
        return 45

    def identify_stale_skills(self, scan_result: Dict) -> List[str]:
        """Identify skills that haven't been used in >threshold turns."""
        stale = []

        for skill, turns_ago in scan_result["last_invoked"].items():
            if turns_ago > self.staleness_threshold:
                stale.append(skill)

        return stale

    def recommend_for_project_type(self, project_type: str) -> List[str]:
        """Recommend skills based on detected project type."""
        recommendations = {
            "rust-cargo": ["rust-best-practices", "cargo-optimizer"],
            "nodejs-npm": ["npm-scripts", "package-json-optimizer"],
            "python-pip": ["python-best-practices", "poetry-helper"],
            "docker": ["docker-compose-wizard", "dockerfile-optimizer"]
        }

        return recommendations.get(project_type, [])

    def unload_skill(self, skill_name: str) -> bool:
        """
        Unload a specific skill from session.

        NOTE: Simulated. Real version would call Claude Code API.
        """
        print(f"[SIMULATED] Unloading skill: {skill_name}")
        print(f"In production, this would call Claude Code API to disable '{skill_name}'")
        return True

    def health_check(self) -> Dict[str, str]:
        """
        Perform health check on skill dependencies.

        Returns:
            Dict mapping component to status (ok/warning/error)
        """
        results = {}

        # Check if gh CLI is installed
        results["gh_cli"] = "ok" if os.system("which gh > /dev/null 2>&1") == 0 else "error"

        # Check if docker is installed
        results["docker"] = "ok" if os.system("which docker > /dev/null 2>&1") == 0 else "warning"

        # Check if python3 is available
        results["python3"] = "ok" if os.system("which python3 > /dev/null 2>&1") == 0 else "error"

        return results

    def garbage_collect(self) -> List[str]:
        """
        Clean up temporary files created by skills.

        Returns:
            List of deleted file paths
        """
        deleted = []

        # Patterns for temporary files
        temp_patterns = [
            "*.skill-temp.*",
            ".claude-export-*.pdf",
            "diagnose-*.log"
        ]

        for pattern in temp_patterns:
            for file_path in self.project_root.glob(pattern):
                if file_path.is_file():
                    try:
                        file_path.unlink()
                        deleted.append(str(file_path))
                    except Exception as e:
                        print(f"Warning: Could not delete {file_path}: {e}", file=sys.stderr)

        return deleted

    def archive_session_memory(self, scan_result: Dict) -> Path:
        """
        Create .skill-memory.json for this repository.

        Returns:
            Path to created memory file
        """
        memory_file = self.project_root / ".skill-memory.json"

        memory = {
            "repository": str(self.project_root),
            "project_type": scan_result["project_type_detected"],
            "recommended_skills": self.recommend_for_project_type(
                scan_result["project_type_detected"]
            ),
            "avoid_skills": self.identify_stale_skills(scan_result),
            "last_updated": datetime.now().isoformat()
        }

        with open(memory_file, "w") as f:
            json.dump(memory, f, indent=2)

        return memory_file


def main():
    parser = argparse.ArgumentParser(
        description="Skills Smart Manager — Context Analysis Engine"
    )
    parser.add_argument(
        "--action",
        required=True,
        choices=["scan", "unload", "health-check", "gc", "archive"],
        help="Action to perform"
    )
    parser.add_argument(
        "--skill",
        help="Skill name (for unload action)"
    )
    parser.add_argument(
        "--skills",
        help="Comma-separated skill names (for batch unload)"
    )
    parser.add_argument(
        "--staleness-threshold",
        type=int,
        default=STALENESS_THRESHOLD,
        help=f"Turns without invocation before skill considered stale (default: {STALENESS_THRESHOLD})"
    )
    parser.add_argument(
        "--auto-unload",
        action="store_true",
        help="Automatically unload stale skills without prompting"
    )

    args = parser.parse_args()

    analyzer = ContextAnalyzer(staleness_threshold=args.staleness_threshold)

    if args.action == "scan":
        result = analyzer.scan()
        print(json.dumps(result, indent=2))

        # Identify stale skills
        stale = analyzer.identify_stale_skills(result)
        if stale:
            print("\n=== Stale Skills Detected ===", file=sys.stderr)
            for skill in stale:
                tokens = result["estimated_token_footprint"].get(skill, 0)
                turns = result["last_invoked"].get(skill, 0)
                print(f"  - {skill}: {tokens} tokens, {turns} turns ago", file=sys.stderr)

        # Recommend skills for project type
        recommended = analyzer.recommend_for_project_type(result["project_type_detected"])
        if recommended:
            print("\n=== Recommended Skills ===", file=sys.stderr)
            for skill in recommended:
                print(f"  - {skill}", file=sys.stderr)

    elif args.action == "unload":
        if args.skill:
            analyzer.unload_skill(args.skill)
        elif args.skills:
            for skill in args.skills.split(","):
                analyzer.unload_skill(skill.strip())
        else:
            print("Error: --skill or --skills required for unload action", file=sys.stderr)
            sys.exit(1)

    elif args.action == "health-check":
        results = analyzer.health_check()
        print("=== Health Check Results ===")
        for component, status in results.items():
            emoji = {"ok": "✅", "warning": "⚠️", "error": "❌"}[status]
            print(f"{emoji} {component}: {status}")

    elif args.action == "gc":
        deleted = analyzer.garbage_collect()
        print(f"Deleted {len(deleted)} temporary files:")
        for path in deleted:
            print(f"  - {path}")

    elif args.action == "archive":
        scan_result = analyzer.scan()
        memory_file = analyzer.archive_session_memory(scan_result)
        print(f"Session memory archived to: {memory_file}")


if __name__ == "__main__":
    main()
