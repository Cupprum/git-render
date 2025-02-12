import os
import plotly.express as px
from git import Repo

repo = Repo("../unitycatalog")

blobs = [{
    'parent': os.path.dirname(blob.path) or "/",
    'path': blob.path,
    'size': blob.size,
    'commits': len(commits := list(repo.iter_commits(paths=blob.path))),
    'collabs': len(set(c.author.email for c in commits)),
} for blob in repo.tree().traverse()]

px.treemap(
    blobs,
    names='path',
    parents='parent',
    values='size',
    hover_data=['commits', 'collabs'],
    color='commits',
    color_continuous_scale='amp',
).show()