# Setting Up an Existing Repository on a New Computer

## Prerequisites

Before you begin, ensure the following software is installed:

- [Git](https://git-scm.com/downloads)

---

## Step 1: Clone the Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository:
   ```sh
   cd path/to/your/directory
   ```
3. Clone the repository using:
   ```sh
   git clone <repository-url>
   ```
   Example:
   ```sh
   git clone https://github.com/username/repository.git
   ```

---

## Step 2: Navigate to the Project Directory

```sh
cd repository-name
```

---

## Step 3: Verify Everything Works

- Check if all the files matches your repository

---

## Step 4: Connect to GitHub (If Contributing Changes)

To push changes back to GitHub:

1. Configure Git credentials (if not already set up):
   ```sh
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   ```
2. Check the remote URL:

   ```sh
   git remote -v
   ```

   should match your remote repository

3. Ensure the correct upstream branch:
   ```sh
   git branch --set-upstream-to=origin/main main
   ```
4. Pull the latest changes before making edits:
   ```sh
   git pull origin main
   ```

---

## Step 5: Commit and Push Changes (If Needed)

```sh
git add .
git commit -m "Your commit message"
git push origin main
```

This guide ensures a smooth setup process on any new computer. 🚀
