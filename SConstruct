import subprocess as sp
import os

def make_gh_pages(target, source, env):
    # checkout the gh-pages branch, and pull in the relevant files
    # from master (e.g. images, stylesheets, etc.)
    sp.call(["git checkout", "gh-pages"])
    sp.call(["git checkout", "master", "--"] + source[1:])

    # copy the slides to index.html and update them in the index
    sp.call(["cp", source[0], target])
    sp.call(["git add", "-A", target])

    # update the other files as well
    for src in source:
        sp.call(["git add", "-A", src])

    # commit the changes, and push them to github if it's not a dryrun
    sp.call(["git commit", "-m", "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"])
    if not env["DRYRUN"]:
        sp.call(["git push", "origin" "gh-pages"])

    # checkout the master branch again
    sp.call(["git checkout", "master"])


## Create the environment
env = Environment(ENV=os.environ)
env['PREFIX'] = "mental-rotation-cogsci2014"


## Specify nbconvert target, to generate the slides
env.Command(
    "mental-rotation-cogsci2014.slides.html",
    ["mental-rotation-cogsci2014.ipynb", "reveal.tpl", "reveal.js"],
    " ".join([
        "ipython nbconvert",
        "--RevealHelpTransformer.url_prefix=reveal.js",
        "--to slides",
        "--template reveal.tpl",
        "$SOURCE"]))

env.Alias("slides", "mental-rotation-cogsci2014.slides.html")


## Specify the gh-pages target, to generate the version of the slides
## for github pages
env.Command(
    "index.html", 
    ["mental-rotation-cogsci2014.slides.html", "images", "custom.css", "reveal.js"], 
    make_gh_pages)

env.Alias("gh-pages", "index.html")
