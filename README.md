# CLI Practice

Class starter: **[github.com/arulmabr/cli](https://github.com/arulmabr/cli)**.

A small COMPSS 211A practice project for command-line basics, Python scripts, Git, and GitHub Pages. About 45–60 minutes, plus setup and questions.

The six campus resources in this project are **fictional practice data**. They are not recommendations or information about real services.

## Start here

1. Make your own copy on GitHub: **Use this template → Create a new repository**. Give your copy a short name such as `cli-practice`. A public copy is the simplest route for the Pages exercise; only use the supplied fictional content.
2. Clone **your copy** with GitHub Desktop, then open it in VS Code. Do not edit the instructor's original.
3. In VS Code, open **Terminal → New Terminal**. On Windows, select **Git Bash**. These commands are for Bash/Zsh, not Windows Command Prompt.
4. From the repository folder, check:

   ```bash
   pwd
   git status
   uv run python --version
   ```

   This repo needs Python 3.10 or newer and no extra packages. Use the `uv` installation from course setup. If Python is already available directly, you may use `python3` (macOS/Linux) or `python` (Windows) in place of `uv run python` throughout.

5. Open [PRACTICE.md](PRACTICE.md). Predict each command's result before running it.

Downloading a ZIP lets you inspect the files, but does not give you Git history or a configured remote. Use a clone for the full exercise.

## What is here?

```text
cli-practice/
├── README.md              ← start here
├── PRACTICE.md            ← guided activities
├── data/
│   └── resources.csv      ← six fictional records
├── scripts/
│   └── inspect_resources.py ← runnable Python starter with two TODOs
├── notes/
│   └── observations.md    ← your notes and one recovery exercise
└── index.html            ← a tiny website to personalize
```

The script prints a summary in the terminal. The HTML page is edited separately; running the script does not update the page. GitHub Pages serves the HTML and does not execute the Python script for visitors.

## Our workflow

```text
edit → save → inspect → stage → commit → push → check GitHub
                                               ↓
                                     Pages deploys the website
```

A commit records local history. A push sends commits to the remote. A working website is a separate result to verify.

Work only in your practice copy. Keep personal details, credentials, and real student data out of it. The ignored `generated/` directory is for temporary output.
