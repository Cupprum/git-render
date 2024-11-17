import os
import plotly.express as px
from git import Repo

# repo = Repo(".")
repo = Repo("../unitycatalog")
# repo = Repo("../../NN/posit")

data = [{
    'parent': os.path.dirname(blob.path) or "/",
    'path': blob.path,
    # 'size': blob.size,
    'commits': len(commits := list(repo.iter_commits(paths=blob.path))),
    # 'collabs': len(set(c.author.email for c in commits))
} for blob in repo.tree().traverse()]

px.treemap(
    data,
    names='path',
    parents='parent',
    # values='size',
    # hover_data=['commits', 'collabs'],
    color='commits', # TODO: can color representing number of commits update when i click around? check color settings
    color_continuous_scale='amp',
).show()