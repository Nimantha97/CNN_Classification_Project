import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "CNN_Classification_Project"
AUTHOR_NAME = "Nimantha97"
SRC_NAME = "cnnClassifier"
AUTHOR_EMAIL = "nimanthagayan0309@gmail.com"

setuptools.setup(
    name = SRC_NAME,
    version = __version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description= " small python package for CNN app",
    long_description= long_description,
    long_description_content = "text/markdown",
    url= f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = { "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",},
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")
)

