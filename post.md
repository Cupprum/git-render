# A simple way of visualizing git repository evolution.

Some time ago, a new colleague joined our department and started working on a platform our department provides. During his initial days, I noticed he was using an interactive Python shell to create [treemap](https://en.wikipedia.org/wiki/Treemapping) visualizations of the project's git history.

The visualizations looked something like this.

![Unity catalog basic visualization](pictures/git_render_unity_catalog_basic.png)

This immediately sparked my interest.
Normally, when starting to learn about a new codebase, I would also look at git history, but i would mainly focus on basic information like the number of commits, contributors, stars and so on. However, these visualizations offered a new interesting perspective on understanding how the repository evolved over time.

Creating these visualizations helped the colleague to see where the core issue of the project is being addressed by showing which files are edited most, and contain the largest amount of collaborators. Based on these information its easier to find out which parts of the code are more interesting, and likely to be touched in the future. Therefore it might make sense to learn a bit more about these frequently used files before starting to work on the project.

I did not sadly remember the exact commands the colleague used.

Later I found out about [git-truck](https://github.com/git-truck/git-truck) from another colleague. It is a very simple and convenient tool. It is installed and executed by one simple command `npx -y git-truck`. It allows to use filters to highlight different information about the project. The tool is private by design, free and open source.

When the back then new colleague was using his own make shift git-truck, i remember he used something to interact with git and something to render the filesystem as a [treemap](https://en.wikipedia.org/wiki/Treemapping).

After a bit of searching i figured a great combination are [GitPython](https://gitpython.readthedocs.io/en/stable/quickstart.html#gitpython-quick-start-tutorial) and [Plotly](https://plotly.com/python/treemaps/).

GitPython is a simple library which allows for interaction with git repository directly from Python. Traversing through tree of files and directories or iterating through the git commit history can be easily done by using this library.

Plotly can be used to create uncomplicated visualizations of this tree in a browser. It allows for simple configuration based on which its clear to highlight different information about the project.

I especially like the simplicity of these two libraries, and that its possible to quickly change them to render different interesting data.

For instance the size of tiles can depend on the sizes of files. Or we can also render the amount of collaborators on each specific file.

These couple of lines can be useful when analyzing small git repos. However if you try to run this code snippet against a larger code base, like trying visualize the git history of [CPython](https://github.com/python/cpython), it will take a very long time. I don't know how long it would take as i canceled it after couple of minutes. Luckily `git-truck` loads even larger projects very quickly.