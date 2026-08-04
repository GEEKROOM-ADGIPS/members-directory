#!/usr/bin/env python3
"""
Geek Room ADGIPS - Members Directory Generator
This script generates README.md from members.json data.
Run this script after updating members.json to regenerate the README.
"""

import json
from datetime import datetime

def load_data():
    with open("members.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_github_avatar(username):
    return f"https://github.com/{username}.png"

def get_role_priority(role):
    """Return sort priority: lower number = higher rank"""
    priorities = {
        "Lead": 0,
        "Co-Lead": 1,
        "Core Team": 2,
        "Member": 3,
        "Alumni": 4
    }
    return priorities.get(role, 5)

def generate_stats(data):
    members = data["members"]
    total = len(members)
    leads = sum(1 for m in members if "Lead" in m["role"])
    core_team = sum(1 for m in members if m["role"] == "Core Team")
    departments = len(data["departments"])
    batches = len(set(m["batch"] for m in members))

    return f"""
## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| 👥 Total Members | **{total}** |
| ⭐ Leads & Co-Leads | **{leads}** |
| 🏛️ Core Team | **{core_team}** |
| 🏢 Departments | **{departments}** |
| 📅 Active Batches | **{batches}** |

"""

def generate_executive_board(members, departments):
    board_members = [m for m in members if m["role"] == "Core Team"]
    if not board_members:
        return ""

    board_members.sort(key=lambda x: x["name"])

    rows = []
    for m in board_members:
        avatar = get_github_avatar(m["github"])
        dept = next((d for d in departments if d["id"] == m["department"]), None)
        dept_emoji = dept["emoji"] if dept else "📌"
        dept_name = dept["name"] if dept else m["department"]
        links = f"[GitHub](https://github.com/{m['github']})"
        if m.get("linkedin"):
            links += f" · [LinkedIn](https://linkedin.com/in/{m['linkedin']})"
        if m.get("portfolio"):
            links += f" · [Portfolio]({m['portfolio']})"

        rows.append(f"""| <img src="{avatar}" width="40" height="40" style="border-radius:50%"> | **{m['name']}** | {dept_emoji} {dept_name} | {m['batch']} | {links} |""")

    table = "| | Name | Department | Batch | Links |\n"
    table += "|---|------|------------|-------|-------|\n"
    table += "\n".join(rows)

    return f"""
## 🏛️ Executive Board

{table}

"""

def generate_department_section(dept, members):
    dept_members = [m for m in members if m["department"] == dept["id"]]
    if not dept_members:
        return f"""
### {dept["emoji"]} {dept["name"]}

*{dept["description"]}*

> No members added yet. Be the first! [Add yourself →](CONTRIBUTING.md)

"""

    # Sort: Lead → Co-Lead → Core Team → Member → Alumni
    dept_members.sort(key=lambda x: (get_role_priority(x["role"]), x["name"]))

    rows = []
    for m in dept_members:
        avatar = get_github_avatar(m["github"])
        skills = ", ".join(m["skills"][:3]) if m["skills"] else "—"
        role_badge = f"`{m['role']}`" if m["role"] != "Member" else ""
        links = f"[GitHub](https://github.com/{m['github']})"
        if m.get("linkedin"):
            links += f" · [LinkedIn](https://linkedin.com/in/{m['linkedin']})"
        if m.get("portfolio"):
            links += f" · [Portfolio]({m['portfolio']})"

        rows.append(f"""| <img src="{avatar}" width="40" height="40" style="border-radius:50%"> | **{m['name']}** {role_badge} | {m['batch']} | {skills} | {links} |""")

    table = "| | Name | Batch | Skills | Links |\n"
    table += "|---|------|-------|--------|-------|\n"
    table += "\n".join(rows)

    return f"""
### {dept["emoji"]} {dept["name"]}

*{dept["description"]}*

{table}

"""

def generate_batch_section(batch, members, departments):
    batch_members = [m for m in members if m["batch"] == batch["year"]]
    if not batch_members:
        return ""

    batch_members.sort(key=lambda x: (get_role_priority(x["role"]), x["name"]))

    items = []
    for m in batch_members:
        dept = next((d for d in departments if d["id"] == m["department"]), None)
        dept_emoji = dept["emoji"] if dept else "📌"
        role = f" ({m['role']})" if m["role"] != "Member" else ""
        items.append(f"- {dept_emoji} **{m['name']}**{role} — [{m['github']}](https://github.com/{m['github']})")

    return f"""### {batch["emoji"]} {batch["label"]}

""" + "\n".join(items) + "\n\n"

def generate_readme(data):
    members = data["members"]
    departments = data["departments"]
    batches = data["batches"]

    # Generate executive board
    board_section = generate_executive_board(members, departments)

    # Generate department sections
    dept_sections = ""
    for dept in departments:
        dept_sections += generate_department_section(dept, members)

    # Generate batch sections
    batch_sections = ""
    for batch in batches:
        batch_sections += generate_batch_section(batch, members, departments)

    # Get leads for featured section
    leads = [m for m in members if "Lead" in m["role"]]
    leads_section = ""
    if leads:
        leads_section = "### 👑 Leadership Team\n\n"
        for lead in leads:
            dept = next((d for d in departments if d["id"] == lead["department"]), None)
            dept_name = dept["name"] if dept else lead["department"]
            leads_section += f"- **{lead['name']}** — {lead['role']} of {dept_name} ([@{lead['github']}](https://github.com/{lead['github']}))\n"
        leads_section += "\n"

    readme = f"""<div align="center">

# 👨‍💻👩‍💻 Geek Room ADGIPS — Members Directory

**Official directory of all past and active members of Geek Room - ADGIPS Chapter**

[![Members](https://img.shields.io/badge/Members-{len(members)}-blue?style=for-the-badge)]()
[![Departments](https://img.shields.io/badge/Departments-{len(departments)}-green?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[🚀 Website](https://geekroom-adgips.github.io) · [📋 Contribute](CONTRIBUTING.md) · [🐛 Report Issue](../../issues)

</div>

---

## 📖 Table of Contents

- [Quick Stats](#-quick-stats)
- [Leadership](#-leadership-team)
- [Executive Board](#-executive-board)
- [Members by Department](#-members-by-department)
- [Members by Batch](#-members-by-batch)
- [How to Join](#-how-to-join)
- [Contributing](#-contributing)

---

{generate_stats(data)}

---

## 👑 Leadership Team

{leads_section}---
{board_section}## 🏢 Members by Department

{dept_sections}
---

## 📅 Members by Batch

{batch_sections}
---

## 🚀 How to Join

We\'re always looking for passionate students who want to learn, build, and grow together!

### Eligibility
- Must be a student at **ADGIPS**
- Interest in tech, coding, or community building
- Willingness to collaborate and contribute

### Steps to Join
1. **Fork** this repository
2. **Add your details** to `members.json` ([see format →](CONTRIBUTING.md))
3. **Submit a Pull Request** with title: `Add member: <Your Name>`
4. Wait for review and approval from the leads

> 💡 **New to open source?** Check our [Contributing Guide](CONTRIBUTING.md) for step-by-step instructions!

---

## 🤝 Contributing

We welcome contributions! Whether you want to:
- 📝 Add yourself as a member
- 🐛 Fix a typo or outdated info
- ✨ Suggest improvements to the directory structure
- 📚 Add documentation

Please read our [Contributing Guidelines](CONTRIBUTING.md) before making a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) — feel free to use this structure for your own college communities!

---

<div align="center">

**Made with ❤️ by the Geek Room ADGIPS Community**

*Last updated: {datetime.now().strftime("%B %d, %Y")}*

</div>
"""
    return readme

def main():
    data = load_data()
    readme = generate_readme(data)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("✅ README.md generated successfully!")
    print(f"📊 Total members: {len(data['members'])}")
    print(f"🏢 Departments: {len(data['departments'])}")

if __name__ == "__main__":
    main()
        
