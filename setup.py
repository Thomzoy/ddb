from setuptools import find_packages, setup


def get_lines(relative_path):
    with open(relative_path) as f:
        return f.readlines()


setup(
    name="edslinkage",
    version="0.1.0",
    author="Data Science - DSI APHP",
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=get_lines("requirements.txt"),
)
