# 🤝 Contributing to Members Directory

Thank you for your interest in joining Geek Room ADGIPS! This guide will help you add yourself to the directory.

---

## 📝 How to Add Yourself

### Step 1: Fork the Repository
Click the **Fork** button at the top right of this page to create your own copy.

### Step 2: Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/members-directory.git
cd members-directory
```

### Step 3: Edit `members.json`

Open `members.json` and add your details to the `members` array. Here's the format:

```json
{
  "name": "Your Full Name",
  "github": "your-github-username",
  "batch": "YYYY-YYYY",
  "department": "dept-id",
  "role": "Member",
  "skills": ["Skill 1", "Skill 2", "Skill 3"],
  "linkedin": "your-linkedin-username",
  "twitter": "your-twitter-handle",
  "portfolio": "https://your-portfolio.com",
  "bio": "A short bio about yourself (optional)"
}
```

### Department IDs
Use one of these exact IDs for the `department` field:

| Department | ID to Use |
|------------|-----------|
| AI / ML | `aiml` |
| DSA & CP | `dsa` |
| Emerging Tech | `emerging-tech` |
| Web Development | `webdev` |
| Event Management | `event-management` |

### Batch Format
Use your college batch years: `YYYY-YYYY` (e.g., `2024-2028`)

### Role Options
- `Member` — Default for new joiners
- `Lead` — Department lead (assigned by board)
- `Co-Lead` — Department co-lead (assigned by board)
- `Core Team` — Core organizing team
- `Alumni` — Graduated members

### Step 4: Regenerate README
```bash
python scripts/generate_readme.py
```

> 💡 **Note:** If you can't run Python, that's okay! The maintainers will regenerate the README when they merge your PR.

### Step 5: Commit and Push
```bash
git add members.json README.md
git commit -m "Add member: Your Name"
git push origin main
```

### Step 6: Create a Pull Request
1. Go to your forked repository on GitHub
2. Click **Contribute** → **Open pull request**
3. Use title: `Add member: Your Name`
4. Add a brief description about yourself
5. Submit the PR!

---

## ✅ PR Checklist

Before submitting, make sure:

- [ ] My GitHub username is correct
- [ ] Department ID matches one from the table above
- [ ] Batch format is `YYYY-YYYY`
- [ ] I haven't modified any other member's data
- [ ] (Optional) I ran `generate_readme.py` to update README

---

## 🐛 Reporting Issues

Found a bug or outdated information?

1. [Open an issue](../../issues/new)
2. Use title format: `[Fix] Brief description`
3. Describe the problem and expected fix

---

## 💡 Tips

- **Keep your bio short** — 1-2 lines max
- **List 3-5 skills** — your top skills only
- **Use your real name** — helps the community know you
- **Be patient** — PR reviews may take 1-2 days

---

## 📞 Need Help?

- 💬 Ask in the [organization discussions](https://github.com/orgs/GEEKROOM-ADGIPS/discussions)
- 📧 Contact your department lead
- 🎓 Join our Discord/WhatsApp group (ask a lead for the link)

**Welcome to the community! 🚀**
