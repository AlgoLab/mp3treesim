import setuptools

long_description = r'''
# MP3-treesim

Triplet-based similarity score for fully multi-labeled trees with poly-occurring labels.

```
usage: mp3treesim [-h] [-i | -u | -g] [-c CORES] [--labeled-only]
                   [--exclude [EXCLUDE [EXCLUDE ...]]]
                   TREE TREE

MP3 tree similarity measure

positional arguments:
  TREE                  Paths to the trees

optional arguments:
  -h, --help            show this help message and exit
  -i                    Run MP3-treesim in Intersection mode.
  -u                    Run MP3-treesim in Union mode.
  -g                    Run MP3-treesim in Geometric mode.
  -c CORES, --cores CORES
                        Number of cores to be used in computation.
  --labeled-only        Ingore nodes without "label" attribute. The trees will
                        be interpred as partially-label trees.
  --exclude [EXCLUDE [EXCLUDE ...]]
                        String(s) of comma separated labels to exclude from
                        computation. If only one string is provided the labels
                        will be excluded from both trees. If two strings are
                        provided they will be excluded from the respective
                        tree. E.g.: --exclude "A,D,E" will exclude labels from
                        both trees; --exclude "A,B" "C,F" will exclude A,B
                        from Tree 1 and C,F from Tree 2; --exclude "" "C" will
                        exclude and C from Tree 2 and nothing from Tree 1

```

A detailed description of the module is available on our [github repo](https://github.com/AlgoLab/mp3treesim).

'''

setuptools.setup(
    name="mp3treesim",
    version="1.0.6",
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
