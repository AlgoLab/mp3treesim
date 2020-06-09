# MP3-treesim
[![PyPI version](https://badge.fury.io/py/mp3treesim.svg)](https://pypi.org/project/mp3treesim/)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/mp3treesim/README.html)

Triplet-based similarity score for fully multi-labeled trees with poly-occurring labels

Link to publication: https://www.biorxiv.org/content/10.1101/2020.04.14.040550v1

## Installation

Using pip
```bash
pip3 install mp3treesim
```

Using bioconda
```bash
conda install mp3treesim
```
## Usage from Command Line (CLI)

```
usage: mp3treesim [-h] [-i | -u | -g] TREE TREE

mp3treesim

positional arguments:
  TREE        Paths to the trees

optional arguments:
  -h, --help  show this help message and exit
  -i          Run MP3-treesim in Intersection mode.
  -u          Run MP3-treesim in Union mode.
  -g          Run MP3-treesim in Geometric mode.
```

For example:
```bash
 $ mp3treesim examples/trees/tree10.gv examples/trees/tree3.gv 
 > 0.02347746030469402
```

## Usage from Python3 as a module

It is possible to use `mp3treesim` directly in a python script by import it.

```python
import mp3treesim as mp3

tree1 = mp3.read_dotfile('examples/trees/tree10.gv')
tree2 = mp3.read_dotfile('examples/trees/tree3.gv')

print(mp3.similarity(tree1, tree2))
# 0.02347746030469402
```

A more detailed example in a clustering use case is availabe in [example/clustering](examples/clustering.ipynb) Jupyter Notebook.

## Input format

The input file must be a valid Graphviz format with the following assumptions:
 - each node must have a label attribute,
 - each label in a node must be separated by a `,` (comma).

Example:
```
digraph Tree {
    1 [label="A"];
    2 [label="B,G"];
    3 [label="C"];
    4 [label="D"];
    5 [label="E"];
    6 [label="F"];
    1 -> 2;
    1 -> 3;
    2 -> 4;
    2 -> 5;
    3 -> 6;
}
```

## Requirements
- `numpy` >= 1.18.1
- `networkx` >= 2.4
- `pygraphviz` >= 1.5 (requires libgraphviz-dev)

## Supplementary material
The supplementary materials and the settings to reproduce the experiments are in https://github.com/AlgoLab/mp3treesim_supp

## We thank for the contributions
- Michele Zoncheddu [@michelezoncheddu](https://github.com/michelezoncheddu)