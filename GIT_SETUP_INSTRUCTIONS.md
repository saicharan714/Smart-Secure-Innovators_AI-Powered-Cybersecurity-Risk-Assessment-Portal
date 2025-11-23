# GitHub Repository Setup & Git Commit Instructions

## Step-by-Step GitHub Repository Creation

### 1. Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in the form:
   - **Repository name:** SmartSecureInnovators_AIRiskAssessmentPortal
   - **Description:** AI-Powered Cybersecurity Risk Assessment Portal for final project submission
   - **Visibility:** Public
   - **Initialize with README:** NO (we have our own)
   - **Add .gitignore:** Python
   - **Add License:** MIT
3. Click "Create repository"

---

## Initial Setup - Local Git Configuration

### In PowerShell (First time only):

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

# Configure Git (if not already done)
git config --global user.name "Sai Charan"
git config --global user.email "your-email@example.com"

# Initialize Git (if not already initialized)
git init

# Add all files
git add .

# Verify status
git status
```

---

## Three Required Commits

### COMMIT 1: Initial Project Setup

**Timing:** After creating folder structure and basic files

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

git add .
git commit -m "Initial project setup for final project - Smart Secure Innovators"
git branch -M main
git remote add origin https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git
git push -u origin main
```

**Files included in this commit:**
- README.md
- .gitignore
- LICENSE (MIT)
- requirements.txt
- Empty src/ and tests/ directories
- docs/ with PROJECT_CHARTER.md, Cost_Calculations_Payback_NPV.md, Milestones_and_Schedule.md

---

### COMMIT 2: Progress Update - AI Model & Web App Framework

**Timing:** After adding initial model code and framework

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

# Add your progress updates
git add src/
git commit -m "Added initial AI model code and web app framework"
git push origin main
```

**Files/changes to include:**
- `src/ai_model/model_training.py` (initial model training code)
- `src/web_app/backend/` (Express.js setup files - can be placeholder)
- `src/web_app/frontend/` (React setup - can be placeholder)
- `src/web_app/api/` (API routes skeleton)
- `src/dashboard/` (dashboard placeholder)

---

### COMMIT 3: Final Version - Complete Implementation

**Timing:** Before final submission

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

git add .
git commit -m "Final project version with full documentation, model, and portal"
git push origin main
```

**Files/changes to include:**
- Complete AI model implementation
- Full backend API with endpoints
- React frontend with all components
- Dashboard with real-time visualization
- Complete test files (model_tests, api_tests, ui_tests)
- Final README and documentation
- Any additional documentation or setup files

---

## Verification Steps

### Check Commit History

```powershell
git log --oneline
# Should show 3 commits with our messages
```

### Verify Remote Connection

```powershell
git remote -v
# Should show: origin https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git
```

### Verify Repository is Public

1. Go to: https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal
2. Check if "Public" badge is visible
3. Anyone should be able to view without authentication

---

## Adding Repository to Basecamp

1. Go to your **Basecamp Project**
2. Navigate to **Docs & Files** section
3. Click **Add Files** or **Add Link**
4. Paste repository URL: `https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal`
5. Add description: "Team GitHub Repository - Smart Secure Innovators AI-Powered Cybersecurity Risk Assessment Portal"
6. Save

---

## Common Git Commands Reference

```powershell
# Check status
git status

# View commit history
git log
git log --oneline --graph

# Check branches
git branch

# Pull latest changes from remote
git pull origin main

# Create a new branch (for feature development)
git checkout -b feature-branch-name

# Switch branches
git checkout main

# Merge branches
git merge feature-branch-name

# View differences
git diff

# Revert a commit (if needed)
git revert <commit-hash>
```

---

## Troubleshooting

### If you get "Repository not found" error:
- Check repository URL is correct
- Ensure you're logged into GitHub
- Verify repository is public

### If you need to reset/start over:
```powershell
# Remove remote (don't push again)
git remote remove origin

# Add correct remote
git remote add origin https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git

# Push again
git push -u origin main
```

### If commits haven't pushed:
```powershell
git push origin main --force-with-lease
```

---

**Document Date:** November 23, 2025  
**Repository Link:** https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal  
**Team:** Smart Secure Innovators
