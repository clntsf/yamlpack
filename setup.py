import setuptools

with open("README.md", "r") as reader:
    long_description = reader.read() \
        .replace("- [", "[")                # normalize checkboxes for pypi format

REQ_PKGS = [
    "pyyaml>=6.0.0",
    "platformdirs>=4.3.0"
]

params = {
    "name": "yamlpack",
    "version": "0.3.0",
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
    "entry_points": {
        'console_scripts': [
            'yamlpack = yamlpack.__main__:main',
        ],
    }
}

setuptools.setup(
    **params
)