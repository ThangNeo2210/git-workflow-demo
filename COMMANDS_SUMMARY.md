# Git Workflow Commands Summary

This document summarizes the CLI commands used to create a standard Git workflow project using `gh`, `git`, and `uv`.

## 1. Prerequisites & Checks
```bash
gh --version
git --version
uv --version
gh auth status
```

## 2. Repository & Project Setup
Initialize the git repo and create it on GitHub:
```bash
git init -b main
gh repo create git-workflow-demo --public --source=. --remote=origin
```

Initialize Python project with `uv`:
```bash
uv init
uv add --dev pytest ruff
```

Organize project structure:
```bash
mkdir -p src/git_workflows tests
touch src/git_workflows/__init__.py
mv main.py src/git_workflows/main.py
```

*(Note: Config files like `.gitignore`, `pyproject.toml`, and source code were created/edited via file operations)*

Initial Commit:
```bash
git add .
git commit -m "Initial project setup with uv, pytest, and ruff"
git push -u origin main
```

## 3. Feature Workflow
Create an Issue:
```bash
gh issue create --title "Add multiply function" --body "We need a function to multiply two numbers..."
```

Create Feature Branch:
```bash
git checkout -b feature/add-multiply
```

*(Code implemented and tests added here)*

Run Tests Locally:
```bash
uv run pytest
```

Push Feature Branch:
```bash
git add .
git commit -m "Add multiply function"
git push -u origin feature/add-multiply
```

## 4. CI/CD Setup
Switch to main to add CI config:
```bash
git checkout main
mkdir -p .github/workflows
```
*(Created `.github/workflows/ci.yml`)*

Push CI Workflow:
```bash
git add .github/workflows/ci.yml
git commit -m "Add CI workflow"
git push
```

## 5. Merging & PR
Sync Feature Branch with Main (to get CI config):
```bash
git checkout feature/add-multiply
git merge main -m "Merge main into feature branch to get CI workflow"
git push
```

Create Pull Request:
```bash
gh pr create --title "Add multiply function" --body "Closes #1..." --base main --head feature/add-multiply
```

## 6. QA & Fixes
Check PR Status:
```bash
gh pr list
gh pr checks 2
```

Fix Linting Errors (Automated):
```bash
uv run ruff check --fix .
```

Push Fixes:
```bash
git add tests/test_main.py
git commit -m "Fix linting issues"
git push
```

Verify Checks:
```bash
gh pr checks 2
```
