pip install --upgrade pip && pip install mkdocs mkdocs-material mkdocs-material[imaging] mkdocs-dracula-theme  mkdocs-i18n  && mkdocs build

# Add a step to validate and fix broken links
# echo "--- Fixing broken links by adding language prefixes ---"
# find docs/ -type f -name "*.md" -exec sed -i '' -E 's#\]\((/[^)]+)\)#](en\1)#g' {} \;

echo "--- Listing current directory contents (repo root) ---" && ls -la && echo "--- Listing site directory contents ---" && ls -la site && rm -rf site/_redirects

## pull docs/ directory from main branch to publish branch
#git checkout publish && git checkout main -- docs/ &&  git commit -m "Pull docs/ directory from main branch to publish branch" && git push origin && git push origin publish