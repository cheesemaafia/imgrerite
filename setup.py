import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imgrerite",
    version="0.1.1",
    author="Jigyasu",
    author_email="jigyasu@outlook.in",
    description="A command-line tool to hide and reveal information inside images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cheesemaafia/imgrerite",
    project_urls={
        "Bug Tracker": "https://github.com/cheesemaafia/imgrerite/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)