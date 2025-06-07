# Git: Working with Branches and Merge Requests

## What is a Git Branch?

A **branch** in Git is a lightweight movable pointer to a commit. It's used to develop features, fix bugs, or experiment safely—**without affecting the main codebase** (usually `main` or `master`).

> Think of a branch as your personal sandbox.

---

## Common Branch Workflow

| Step                      | Command                                     | Purpose                               |
| ------------------------- | ------------------------------------------- | ------------------------------------- |
| 1. Create a branch        | `git checkout -b feature/my-new-feature`    | Creates and switches to a new branch  |
| 2. Work & commit          | `git add .` + `git commit -m "Add feature"` | Save your changes                     |
| 3. Push to remote         | `git push origin feature/my-new-feature`    | Push branch to GitHub or GitLab       |
| 4. Create a Merge Request | On GitHub/GitLab                            | Ask to merge your feature into `main` |
| 5. Merge the branch       | Via merge request or locally                | Combine branch changes into main      |

---

## What is a Merge Request (MR) or Pull Request (PR)?

A **merge request (MR)** (GitLab) or **pull request (PR)** (GitHub) is a way to **propose changes** from one branch to another, typically from `feature/` → `main`.

### Benefits

* Code review
* CI/CD checks
* Discuss changes before merging
* Maintains cleaner history

---

## Example Workflow

### Step-by-Step

```bash
# 1. Start a new feature
git checkout -b feature/add-contact-form

# 2. Make some code changes, then:
git add .
git commit -m "Add contact form feature"

# 3. Push to remote
git push origin feature/add-contact-form
```

### Create Merge Request (via GitHub/GitLab UI)

* Open your repo on the website.
* Click **"Compare & pull request"** or **"New Merge Request"**.
* Choose base = `main`, compare = your branch.
* Submit!

---

## Merging the Branch

Once reviewed:

```bash
# Option 1: Via web UI
# Click "Merge" on GitHub/GitLab

# Option 2: Locally
git checkout main
git pull
git merge feature/add-contact-form
git push origin main
```

---

## Cleaning Up

After merging, delete the feature branch:

```bash
git branch -d feature/add-contact-form      # Local
git push origin --delete feature/add-contact-form   # Remote
```

---

## Handling Merge Conflicts

If two branches change the same line, Git needs help:

```bash
# While merging, you'll see conflicts like:
<<<<<<< HEAD
old code
=======
new code
>>>>>>> feature-branch

# Edit and resolve them manually
git add .
git commit
```

---

## Summary Table

| Concept                             | Purpose                              |
| ----------------------------------- | ------------------------------------ |
| `git branch`                        | Lists all branches                   |
| `git checkout -b <name>`            | Creates and switches to a new branch |
| `git push origin <branch>`          | Pushes branch to remote              |
| Merge Request (MR)                  | Propose to merge branch changes      |
| `git merge`                         | Combine branches                     |
| `git branch -d <branch>`            | Delete branch locally                |
| `git push origin --delete <branch>` | Delete branch remotely               |
