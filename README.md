# cdl-capstone-myproject
Django web-based attendance and skills-tracking system for the Transportation &amp; Logistics Training Academy (Tri-C CDL Program). Built by Cleveland Codes Cohort 20 to support administrators, instructors, and students with login access, rating forms, attendance sheets, and skill-tracking workflows.

## 🚀 Team Workflow Guide (GitHub Desktop Version)

This project uses a branching workflow so everyone can safely add features without overwriting each other's work.  
Follow these steps every time you contribute.

---

## 1️⃣ Clone the Repository (First Time Only)

1. Open **GitHub Desktop**  
2. Click **File → Clone Repository…**  
3. Choose the URL tab  
4. Paste the repo:  

5. Click **Clone**

---

## 2️⃣ Always Pull Before You Start Working

Every time you sit down to code:

1. Open GitHub Desktop  
2. Make sure the current branch is **main**  
3. Click **Fetch origin**  
4. If anything is available, click **Pull origin**  

This makes sure you are up to date.

---

## 3️⃣ Create a New Branch for Your Work

Use this naming format:


Examples:
- `feature/student-models`
- `feature/instructor-forms`
- `feature/attendance-tracking`

### Steps:

1. In GitHub Desktop:  
   - Go to the top bar → click **Current Branch**
   - Click **New Branch**
2. Name your branch (ex: `feature/student-models`)
3. Click **Create Branch**
4. Desktop will switch you to your new branch automatically.

---

## 4️⃣ Make Your Changes Locally

Open your project in VS Code (or your editor):

- Add/edit Django models, views, templates, forms, etc.
- Run the server to test:

---

## 5️⃣ Commit Your Changes

In GitHub Desktop:

1. On the left side, check the changed files  
2. Add a **summary** commit message  
3. Click **Commit to feature/your-branch**

Examples of good commit messages:

- `"Add Student model and migration"`
- `"Create instructor attendance rating form"`
- `"Update login template with styles"`

---

## 6️⃣ Push Your Branch to GitHub

After committing:

Click **Push origin**

This uploads your branch to the repo.

---

## 7️⃣ Open Your Pull Request (PR)

1. After pushing, GitHub Desktop will show a banner:
 **"Create Pull Request"**
2. Click that button  
 (or go to GitHub → **Pull Requests → New Pull Request**)  
3. Make sure:
 - **base branch = main**
 - **compare branch = your branch**
4. Add a short description
5. Submit the PR

---

## 8️⃣ Wait for Review & Merge

Your reviewer (Wayne Largent @waynelargent and Corn @Corncodes ) will:

- Review your code  
- Approve or request changes  
- Merge to main  
- Delete the branch afterward  

---

## 🔁 Repeat for Each Feature

Never reuse old branches.  
Always make a new one for new work.

---

## 🧩 Branch Naming Conventions

| Type      | Example                      |
|-----------|------------------------------|
| Feature   | `feature/student-dashboard`  |
| Bug Fix   | `fix/login-validation`       |
| Refactor  | `refactor/models`            |
| Docs      | `docs/update-readme`         |

---

## 🛑 Important Notes

- **Do NOT commit your virtual environment** (`venv/`)
- **Do NOT commit your .env or SECRET_KEY**
- Always **pull before switching or creating a branch**
- Keep commits small and meaningful

