from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="copilot-cli",
    version="1.0.0",
    author="Razak Mo",
    description="CLI for GitHub Copilot Chat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "copilot-cli=copilot_cli.__main__:main",
        ],
    },
    include_package_data=True,
    package_data={
        "copilot_cli": ["actions.yml"],  # Include actions.yml in the package
    },
)
