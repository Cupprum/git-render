import plotly.express as px
from git import Repo

repo = Repo(".")
data = []

for blob in repo.tree().traverse():
    path = blob.path
    commits = list(repo.iter_commits(paths=path))
    data.append({
        'parent': path.removesuffix(f"/{blob.name}") if "/" in path else "ALL",
        'path': path,
        'size': blob.size,
        'commits': len(commits) if blob.type == "blob" else 0,
        # 'collabs': len(set(c.author.email for c in commits)), # TODO: this is not being render on the screen
    })

px.treemap(
    data,
    names='path',
    parents='parent',
    values='size',
    # custom_data='collabs', # TODO: does not work
    color='commits', # TODO: can color representing number of commits update when i click around? check color settings
    color_continuous_scale='amp',
).show()

