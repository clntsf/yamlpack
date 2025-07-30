import setuptools

with open("README.md", "r") as reader:
    long_description = reader.read()

with open("requirements.txt") as reader:
    REQ_PKGS = reader.read().splitlines()

params = {
    "name": "yamlpack",
    "version": "0.1.0",
    "author": "Colin Simon-Fellowes",
    "author_email": "colin.tsf@gmail.com",
    "description": "Package boilerplate creator using YAML schemas",

    "long_description": long_description,
    "long_description_content_type": "text/markdown",

    "url": "https://github.com/clntsf/yamlpack",
    "project_urls": {
        "Repo":"https://github.com/clntsf/yamlpack"
    },
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    "package_dir": {"": "src"},
    "package_data": {
        "yamlpack": ["yamlpack/resources/*"]
    },
    "packages": setuptools.find_packages(where="src"),
    "install_requires": REQ_PKGS,
    "python_requires": ">=3.12.2",
}

setuptools.setup(
    **params
)