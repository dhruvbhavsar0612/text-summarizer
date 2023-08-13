import setuptools
with open("README.md",'r',encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = "0.0.1"
REPO_NAME="text-summarizer"
AUHTOR_NAME="Dhruv Bhavsar"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="dbhavsar9898@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUHTOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://www.github.com/{AUHTOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://www.github.com/{AUHTOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
