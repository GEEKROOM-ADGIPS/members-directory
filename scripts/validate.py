#!/usr/bin/env python3
"""
Validate members.json before allowing PR merge.
Run this in CI or locally before committing.
"""

import json
import sys
import re

REQUIRED_FIELDS = ["name", "github", "batch", "department", "role", "skills"]
VALID_DEPARTMENTS = ["aiml", "dsa", "emerging-tech", "webdev", "event-management"]
VALID_ROLES = ["Member", "Lead", "Co-Lead", "Core Team", "Alumni"]

def validate():
    errors = []
    warnings = []

    try:
        with open("members.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ members.json not found")
        sys.exit(1)

    members = data.get("members", [])
    if not members:
        errors.append("No members found in members.json")

    # Check for template member still present
    for m in members:
        if m.get("github") == "your-github-username":
            errors.append("Template member (your-github-username) still present — replace with real data!")

    # Validate each member
    github_usernames = []
    for i, member in enumerate(members):
        prefix = f"Member [{i+1}]"

        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in member:
                errors.append(f"{prefix}: Missing required field '{field}'")

        # GitHub username format
        github = member.get("github", "")
        if github:
            if not re.match(r'^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$', github):
                errors.append(f"{prefix}: Invalid GitHub username '{github}'")
            if github in github_usernames:
                errors.append(f"{prefix}: Duplicate GitHub username '{github}'")
            github_usernames.append(github)

        # Department validation
        dept = member.get("department", "")
        if dept and dept not in VALID_DEPARTMENTS:
            errors.append(f"{prefix}: Invalid department '{dept}'. Must be one of: {', '.join(VALID_DEPARTMENTS)}")

        # Role validation
        role = member.get("role", "")
        if role and role not in VALID_ROLES:
            errors.append(f"{prefix}: Invalid role '{role}'. Must be one of: {', '.join(VALID_ROLES)}")

        # Batch format
        batch = member.get("batch", "")
        if batch and not re.match(r'^\d{4}-\d{4}$', batch):
            errors.append(f"{prefix}: Invalid batch format '{batch}'. Use YYYY-YYYY")

        # Skills should be a list
        skills = member.get("skills", [])
        if not isinstance(skills, list):
            errors.append(f"{prefix}: 'skills' must be an array")
        elif len(skills) > 8:
            warnings.append(f"{prefix}: Consider keeping skills to top 5-8 (you have {len(skills)})")

        # Bio length
        bio = member.get("bio", "")
        if len(bio) > 150:
            warnings.append(f"{prefix}: Bio is quite long ({len(bio)} chars). Consider keeping it under 150.")

    # Print results
    print("=" * 50)
    print("🔍 members.json Validation Report")
    print("=" * 50)

    if errors:
        print(f"\n❌ {len(errors)} Error(s) found:")
        for e in errors:
            print(f"   • {e}")

    if warnings:
        print(f"\n⚠️  {len(warnings)} Warning(s):")
        for w in warnings:
            print(f"   • {w}")

    if not errors and not warnings:
        print("\n✅ All checks passed! members.json is valid.")
        print(f"📊 Total members: {len(members)}")
        return 0
    elif not errors:
        print("\n✅ No errors, but please review warnings above.")
        return 0
    else:
        print(f"\n❌ Validation failed. Please fix {len(errors)} error(s) before submitting.")
        return 1

if __name__ == "__main__":
    sys.exit(validate())
