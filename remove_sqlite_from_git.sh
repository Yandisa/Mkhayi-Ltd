#!/bin/bash
# Run these commands in your project root to remove db.sqlite3 from git history

# 1. Remove db.sqlite3 from git tracking (keeps the file locally)
git rm --cached db.sqlite3

# 2. Stage the updated .gitignore
git add .gitignore

# 3. Commit both changes
git commit -m "chore: remove db.sqlite3 from version control, update .gitignore"

# 4. Push to GitHub
git push origin main

# Note: your local db.sqlite3 file is untouched — git just stops tracking it.
# On the server, Coolify mounts /app/db as a volume so the database persists across redeploys.
