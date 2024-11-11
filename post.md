A new colleague was using something like this in interactive python during his first days to learn about history of a new project he was assigned to.

This caught my attention as it is really great way of getting additional perspective on the state of git project. It helps with seeing where the core issue of the project is being addressed, by showing which files are edited most, and contain the largest amount of collaborators. Based on these information its easier to find out which parts of the code are more interesting, and likely to be touched in the future, so it might make sense to learn a bit more about them.

However i did not remember what the exact commands were.

Later I found out about [git-truck](https://github.com/git-truck/git-truck) from another colleague. It is a very simple and convenient tool. It is installed and executed by one simple command `npx -y git-truck`. It allows to use filters to highlight different information about the project.

When the colleague was using his own make shift git-truck, i remember he used something to interact with git and something to render the filesystem as a `treemap`. After a bit of searching i figured a great combination are [GitPython](https://gitpython.readthedocs.io/en/stable/quickstart.html#gitpython-quick-start-tutorial) and [Plotly](https://plotly.com/python/treemaps/).

GitPython allows to easily iterate over the git history, and also to create the tree of directories and files.

Plotly can be used to easily visualize this tree in browser. It allows for simple configuration based on which its easy to highlight different information about the project.

I especially appreciate the simplicity of these two libraries. How nicely they fit together and can be used in symbiosis in order to create neat renders.