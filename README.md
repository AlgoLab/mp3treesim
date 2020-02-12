# MP3-treesim

Triplet-based similarity score for fully multi-labeled trees with poly-occurring labels

Link to publication: TBD

## Installation

```bash
pip3 install mp3treesim
```

## Usage from Command Line (CLI)

```
usage: mp3treesim [-h] [-i | -u | -g] TREE TREE

mp3treesim <------------------------- FIX THIS

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