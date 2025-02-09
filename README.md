# Git Render
Is a simple python script which can be used to visualize git history of a project.

Learn more in this [post]().

## Website
This website is supposed to be as simple as possible, so i that i do not have to spend my time maintaining it. The post is a plain html file, which contains basic css. It is hosted on [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages).

## Script
Following section describes how to install and execute the Python script.

### Installation
```
git clone git@github.com:Cupprum/git-render.git
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Execution
```
# Source venv if needed.
source venv/bin/activate
# Update `git_render.py` to target desired codebase.
python3 git_render.py
```