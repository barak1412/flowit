from setuptools import setup, find_packages

install_requires = [
    'networkx'
]

setup(
    name="flowit",
    version="1.0.0",
    author="Barak David",
    license="MIT",
    keywords="Lightweight DAG execution library.",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3'
)