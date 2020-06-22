import setuptools

long_description = r'''
# MP3-treesim

Triplet-based similarity score for fully multi-labeled trees with poly-occurring labels.

# Usage

A detailed description of the module is available on our [github repo](https://github.com/AlgoLab/mp3treesim).

'''

setuptools.setup(
    name="mp3treesim",
    version="1.0.4",
    author="Simone Ciccolella",
    author_email="s.ciccolella@campus.unimib.it",
    description="Triplet-based similarity score for fully multi-labeled trees with poly-occurring labels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlgoLab/mp3treesim",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.18.1',
        'networkx>=2.4',
        'pygraphviz>=1.5'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'mp3treesim=mp3treesim.__main__:main']},
)
