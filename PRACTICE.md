# From local files to a small website

Work with a neighbor, taking turns at the keyboard. Keep this file open as a guide. Type commands one at a time in the terminal; type Python into the script in VS Code.

## 1. Find your files · 5 minutes

Start in your cloned practice repository:

```bash
pwd
ls
cd data
pwd
ls
head -n 4 resources.csv
cd ..
```

**Check:** You are back at the repository root. The first four CSV lines contain a header and three records.

**Explain:** What does `..` mean? From the repository root, what is the relative path to the CSV?

Optional shell practice:

```bash
mkdir -p generated
cp data/resources.csv generated/resources_copy.csv
mv generated/resources_copy.csv generated/practice_copy.csv
head -n 4 generated/practice_copy.csv | wc -l
```

Expect `4`, a count of lines. `generated/` is ignored by Git. Do not overwrite the source CSV. If you already have the named output files, choose fresh names.

## 2. Run, edit, and rerun Python · 10 minutes

From the repository root:

```bash
uv run python scripts/inspect_resources.py
```

**Check:** The starter runs. It prints a TODO for the count and previews Maple Study Room and Willow Reading Corner.

Open `scripts/inspect_resources.py` in VS Code. The loading code is supplied; leave it as it is. Complete the two TODOs:

1. Count the items in the `resources` list. Hint: which Python function gives a list's length?
2. Preview the first three records. Hint: change the endpoint of the slice.

Save, predict the result, and run the same terminal command again.

**Check:** The count is `6`. The preview contains Maple Study Room, Willow Reading Corner, and Cedar Computer Desk. No traceback appears.

**Explain:** What actually ran the updated code? Would this script know about a variable you created in a separate notebook?

## 3. Make and diagnose a path error · 5 minutes

Leave the Python code unchanged:

```bash
cd scripts
pwd
uv run python inspect_resources.py
```

**Check:** Expect a `FileNotFoundError` mentioning `data/resources.csv`. Read the final error line.

**Explain:** Where is Python looking for that relative path now? Did the data move?

Repair the run by returning to the agreed starting folder:

```bash
cd ..
uv run python scripts/inspect_resources.py
```

**Check:** The script succeeds again. Do not change the CSV path in the script for this exercise.

## 4. Commit your completed script · 5 minutes

```bash
git status
git diff -- scripts/inspect_resources.py
git add scripts/inspect_resources.py
git diff --cached
git commit -m "Complete resource count and preview"
git log --oneline -3
git status
```

**Check:** The staged diff contains only the intended script changes. The new commit appears in history, and the working tree is clean.

If Git asks for a name and email, use your GitHub Desktop identity setup; a GitHub-provided no-reply email can keep your personal email out of public commits. If output opens in a pager, press `q` to return to the prompt.

**Explain:** Has the commit reached GitHub yet? What does staging select?

## 5. Undo one deliberate practice edit · 5 minutes

Start with `git status` and a clean working tree. Before writing real observations, add this temporary line to `notes/observations.md` and save:

```text
TEMPORARY: this sentence is only for the recovery exercise.
```

Inspect it:

```bash
git status
git diff -- notes/observations.md
```

Name the exact line you want to discard. Do not stage it. Then:

```bash
git restore -- notes/observations.md
git diff -- notes/observations.md
git status
git log --oneline -3
```

**Check:** Only the temporary edit is gone. Your script commit remains. Reopen the notes file to verify.

`git restore` here replaces this file's unstaged edits with its staged version. Because you did not stage the temporary line, that version still matches the last commit. Discarded uncommitted edits may not be recoverable. Do not use a broad restore or `reset --hard`.

## 6. Personalize and publish the page · 10–15 minutes

Open `index.html` in VS Code and change just the two marked pieces:

- the main heading: use a fictional team nickname;
- the learning sentence: describe one thing you can now explain.

Save and open `index.html` in a browser to inspect it locally. Then:

```bash
git diff -- index.html
git add index.html
git diff --cached
git commit -m "Personalize our practice page"
```

In GitHub Desktop, choose **Push origin**. Open **your repository** on GitHub and verify that both new commits and the changed HTML arrived. Students with a configured upstream can instead use `git push`.

For this repo's simple HTML page, on GitHub:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Select the branch containing your changes (normally `main`) and **/(root)**, because `index.html` is at the root.
4. Save. Check the Pages deployment run in **Actions**; deployment may take a few minutes.
5. Open the website URL shown in Pages settings in a signed-out/private browser window. Verify your heading, learning sentence, and CSV link.

The repository URL and website URL are different. A push is not proof that a site deployed successfully. If you get a 404, check the selected branch/folder, that `index.html` was pushed there, and the deployment result.

Reference: [GitHub's Pages publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## 7. Explain what happened · 5 minutes

Now fill in `notes/observations.md` with your explanations and both URLs. Review, commit, and push it:

```bash
git diff -- notes/observations.md
git add notes/observations.md
git diff --cached
git commit -m "Record workflow observations and project links"
```

Use **Push origin** again and verify the notes on GitHub. This gives you three meaningful commits of your own, in addition to the starter history.

Show your neighbor:

- the script's successful output;
- the three commits on GitHub;
- the live page and its working CSV link;
- an explanation of the path error and the difference between commit and push.

This is discussion practice. Follow the separate course instructions for any homework or quiz submission.
