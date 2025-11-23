# Ready-to-Execute Git Commands

**Copy and paste these commands in PowerShell in order**

---

## Step 1: Initial Repository Setup (First Time Only)

```powershell
# Navigate to project directory
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

# Configure Git (if not already done)
git config --global user.name "Sai Charan"
git config --global user.email "your-email@example.com"

# Initialize repository (if not already done)
git init

# Verify Git is working
git --version
```

---

## Step 2: Check Repository Status

```powershell
# See what files will be committed
git status

# View all files
git ls-files -o --exclude-standard
```

---

## COMMIT 1: Initial Project Setup

Execute these commands in PowerShell:

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

# Stage all files
git add .

# Verify files are staged
git status

# Create first commit
git commit -m "Initial project setup for final project - Smart Secure Innovators"

# Verify commit
git log --oneline
```

---

## Step 3: Connect to GitHub (First Time Only)

After creating repository on GitHub at https://github.com/new

```powershell
# Set main branch as default
git branch -M main

# Add remote repository
git remote add origin https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git

# Verify remote connection
git remote -v
```

---

## Step 4: First Push to GitHub

```powershell
# Push initial commit to GitHub
git push -u origin main

# Verify it worked - check GitHub.com in your browser
```

---

## COMMIT 2: Progress Update - AI Model & Framework

Add your progress files, then execute:

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

# Stage updated files
git add src/

# Create second commit
git commit -m "Added initial AI model code and web app framework"

# Verify commit
git log --oneline

# Push to GitHub
git push origin main
```

---

## COMMIT 3: Final Version - Complete Implementation

After finalizing all code and documentation:

```powershell
cd C:\Users\saich\Smart-Secure-Innovators_AI-Powered-Cybersecurity-Risk-Assessment-Portal

# Stage all remaining files
git add .

# Create third commit
git commit -m "Final project version with full documentation, model, and portal"

# Verify all commits
git log --oneline --graph

# Push final commit to GitHub
git push origin main
```

---

## Verify Everything is Correct

```powershell
# Check commit history
git log --oneline

# Should show something like:
# abc1234 Final project version with full documentation, model, and portal
# def5678 Added initial AI model code and web app framework
# ghi9012 Initial project setup for final project - Smart Secure Innovators

# Check remote connection
git remote -v

# Should show:
# origin  https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git (fetch)
# origin  https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git (push)

# Check current branch
git branch -v
# Should show: * main
```

---

## Verify on GitHub Website

1. Visit: https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal
2. Verify you can see:
   - ✅ "Public" badge
   - ✅ 3 commits in commit history
   - ✅ README.md displayed
   - ✅ All folders (docs, src, tests) visible
   - ✅ LICENSE file visible

---

## Additional Useful Commands (If Needed)

```powershell
# Check what would be committed before git add
git diff

# View detailed commit info
git show

# See specific commit details
git show <commit-hash>

# Check for uncommitted changes
git status

# View last N commits
git log -N 5

# View commits with changes
git log --stat

# View specific file history
git log -- <filename>

# Check branch status vs remote
git branch -vv

# Pull latest from remote (if working with team)
git pull origin main
```

---

## Troubleshooting Commands

```powershell
# If you need to undo the last commit (before pushing)
git revert HEAD

# If you need to check what would be pushed
git diff origin/main

# If remote shows as "not found"
git remote remove origin
git remote add origin https://github.com/saicharan714/SmartSecureInnovators_AIRiskAssessmentPortal.git

# If you need to force push (use with caution!)
git push origin main --force-with-lease
```

---

## Order of Execution Summary

1. ✅ GitHub Repository Setup (one-time)
2. ✅ Local Git Configuration (one-time)
3. ✅ Add Files & Execute Commit 1
4. ✅ Connect to GitHub (one-time)
5. ✅ First Push
6. ✅ Add More Files & Execute Commit 2
7. ✅ Push Commit 2
8. ✅ Complete Implementation & Execute Commit 3
9. ✅ Push Commit 3
10. ✅ Verify on GitHub

---

**Ready to execute!** Copy commands one section at a time and paste into PowerShell.

**Document Date:** November 23, 2025
