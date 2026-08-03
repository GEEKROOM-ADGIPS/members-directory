# 🚀 First-Time Setup Guide for Leads

Welcome, Lead! This guide will help you set up the Members Directory for the first time and add yourself as the first real member.

---

## 📋 Step-by-Step Setup

### Step 1: Fork & Clone (if you haven't already)

```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/members-directory.git
cd members-directory
```

### Step 2: Replace the Template Member with Yourself

Open `members.json` and replace the template entry with your real information:

**Before:**
```json
{
  "name": "Your Name",
  "github": "your-github-username",
  "batch": "2024-2028",
  "department": "webdev",
  "role": "Lead",
  "skills": ["React", "Node.js", "MongoDB"],
  "linkedin": "your-linkedin-username",
  "twitter": "",
  "portfolio": "https://your-portfolio.com",
  "bio": "Short bio about yourself"
}
```

**After (example):**
```json
{
  "name": "Rahul Sharma",
  "github": "rahulsharma",
  "batch": "2024-2028",
  "department": "webdev",
  "role": "Lead",
  "skills": ["React", "Node.js", "MongoDB", "TypeScript"],
  "linkedin": "rahulsharma",
  "twitter": "",
  "portfolio": "https://rahulsharma.dev",
  "bio": "Full-stack developer building open-source tools for the community"
}
```

### Step 3: Validate Your Changes

```bash
python scripts/validate.py
```

You should see:
```
✅ All checks passed! members.json is valid.
📊 Total members: 1
```

### Step 4: Generate the README

```bash
python scripts/generate_readme.py
```

This creates the `README.md` with your profile displayed.

### Step 5: Commit & Push

```bash
git add members.json README.md
git commit -m "Add first lead: Your Name"
git push origin main
```

### Step 6: Create Pull Request

1. Go to your fork on GitHub
2. Click **Contribute** → **Open pull request**
3. Title: `Add lead: Your Name`
4. Submit!

---

## 🎯 Adding More Members

Once you're set up, other members can follow the [Contributing Guide](CONTRIBUTING.md).

As a lead, you'll review PRs and merge them. The GitHub Action will auto-update the README.

---

## 🏢 Department Lead Assignment

After adding yourself, update the department lead in `members.json`:

```json
{
  "id": "webdev",
  "name": "Web Development",
  "emoji": "🌐",
  "description": "Frontend, Backend, Full-Stack Web Dev & Web Apps",
  "lead": "rahulsharma"
}
```

---

## 📞 Need Help?

- Check [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions
- Run `python scripts/validate.py` if something seems off
- Open an issue if you get stuck

**Welcome to Geek Room ADGIPS! 🚀**
