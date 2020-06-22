#!/usr/bin/env python3
# coding: utf-8

from itertools import combinations
from collections import defaultdict, Counter

import networkx as nx
import numpy as np
from pygraphviz import AGraph


class Tree:
    def __init__(self, T, label_to_nodes, node_to_labels, label_set):
        self.T = T
        self.label_to_nodes = label_to_nodes
        self.node_to_labels = node_to_labels
        self.label_set = label_set

        self.LCA = LCA(self.T,
                       self.label_to_nodes,
                       self.node_to_labels)


class LCA:
    def __init__(self, T, T_label_to_node, T_node_to_labels):
        self.LCA_dict = dict()
        self.LCA_label_dict = T_label_to_node
        self.LCA_node2lbl = T_node_to_labels
        for lca in nx.tree_all_pairs_lowest_common_ancestor(T):
            self.LCA_dict[(lca[0][0], lca[0][1])] = lca[1]

    def lca_nodes(self, node1, node2):
        try:
            return self.LCA_dict[node1, node2]
        except:
            return self.LCA_dict[node2, node1]

    def lca_labels(self, label1, label2):
        nodes1 = self.LCA_label_dict[label1]
        nodes2 = self.LCA_label_dict[label2]

        lca_mset = Counter()
        for n1 in nodes1:
            for n2 in nodes2:
                lca_mset.update(self.lca_nodes(n1, n2))

        return lca_mset

    def label_to_node(self, label):
        return self.LCA_label_dict[label]

    def node_to_labels(self, node):
        return self.LCA_node2lbl[node]

    def __str__(self):
        return str(self.LCA_dict)


class ExtValue:
    def __init__(self):
        self.counter = 1
        self.nodes = defaultdict(set)

    def get(self, node):
        if not node in self.nodes:
            self.nodes[node].add('EXT{}'.format(self.counter))
            self.counter += 1
        return self.nodes[node]


def sigmoid(x, mult=10.0):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return 1 / (1 + np.exp(-mult * (x - 0.5)))


def intersect_mset_card(list_lca1, list_lca2):
    mset1 = defaultdict(int)
    mset2 = defaultdict(int)

    for lca in list_lca1:
        mset1[','.join(str(x) for x in lca)] += 1

    for lca in list_lca2:
        mset2[','.join(str(x) for x in lca)] += 1

    card = 0

    for k in mset1:
        if k in mset2:
            card += min(mset1[k], mset2[k])

    return card


def is_equal_struct(triple, LCA1, LCA2):
    t = sorted(triple)
    t_set = set(triple)

    triples_nodes_T1 = list()

    for node1 in LCA1.label_to_node(t[0]):
        for node2 in LCA1.label_to_node(t[1]):
            for node3 in LCA1.label_to_node(t[2]):
                triples_nodes_T1.append([node1, node2, node3])

    triples_nodes_T2 = list()

    for node1 in LCA2.label_to_node(t[0]):
        for node2 in LCA2.label_to_node(t[1]):
            for node3 in LCA2.label_to_node(t[2]):
                triples_nodes_T2.append([node1, node2, node3])

    cmp_vecs_t1 = [[None, None, None]
                   for x in range(len(triples_nodes_T1))]
    ext_t1 = [ExtValue() for x in range(len(triples_nodes_T1))]

    cmp_vecs_t2 = [[None, None, None]
                   for x in range(len(triples_nodes_T2))]
    ext_t2 = [ExtValue() for x in range(len(triples_nodes_T2))]

    for ix_c, couple in enumerate(combinations(t, 2)):
        ix_lb1 = t.index(couple[0])
        ix_lb2 = t.index(couple[1])
        ix_other = list({0, 1, 2} - set([ix_lb1, ix_lb2]))[0]

        for ix_t1, triple_T1 in enumerate(triples_nodes_T1):
            lca_nd = LCA1.lca_nodes(triple_T1[ix_lb1], triple_T1[ix_lb2])
            lca_lb = LCA1.node_to_labels(lca_nd)
            if len(lca_lb & t_set) > 0:
                cmp_vecs_t1[ix_t1][ix_c] = lca_lb & t_set
            else:
                lca_nd_other = LCA1.lca_nodes(lca_nd, triple_T1[ix_other])
                lca_lb_other = LCA1.node_to_labels(lca_nd_other)
                if len(lca_lb_other & t_set) > 0:
                    cmp_vecs_t1[ix_t1][ix_c] = lca_lb_other & t_set
                else:
                    cmp_vecs_t1[ix_t1][ix_c] = ext_t1[ix_t1].get(lca_nd)

        for ix_t2, triple_T2 in enumerate(triples_nodes_T2):
            lca_nd = LCA2.lca_nodes(triple_T2[ix_lb1], triple_T2[ix_lb2])
            lca_lb = LCA2.node_to_labels(lca_nd)
            if len(lca_lb & t_set) > 0:
                cmp_vecs_t2[ix_t2][ix_c] = lca_lb & t_set
            else:
                lca_nd_other = LCA2.lca_nodes(lca_nd, triple_T2[ix_other])
                lca_lb_other = LCA2.node_to_labels(lca_nd_other)
                if len(lca_lb_other & t_set) > 0:
                    cmp_vecs_t2[ix_t2][ix_c] = lca_lb_other & t_set
                else:
                    cmp_vecs_t2[ix_t2][ix_c] = ext_t2[ix_t2].get(lca_nd)

    missing = True if len(cmp_vecs_t1) == 0 or len(cmp_vecs_t2) == 0 else False

    return missing, intersect_mset_card(cmp_vecs_t1, cmp_vecs_t2), max(len(cmp_vecs_t1), len(cmp_vecs_t2))


def get_nset_sig(x_i, x_u):
    return x_u + sigmoid(x_i) * (x_i - x_u)


def similarity(tree1, tree2, mode='sigmoid', sigmoid_mult=10.0):
    """ 
    Compute the similarity score of the two trees.

    Parameters: 
    tree1 (Tree): MP3-treesim tree representation
    tree2 (Tree): MP3-treesim tree representation

    Keyword arguments:
    mode (str): 'sigmoid', 'intersection', 'union'
                 or 'geometric',
                 sets the similarity calculation.
                 By default is set to 'sigmoid'.
    sigmoid_mult (float): Multiplicator for the 
                 sigmoid calculation.

    Returns: 
    float: Similarity score

    """

    if not mode in ['sigmoid', 'intersection', 'union', 'geometric']:
        raise AttributeError('Incorrect value of mode passed.')

    numerator = 0
    denominator_i = 0
    denominator_u = 0

    if len(set(tree1.label_set) & set(tree2.label_set)) == 0:
        return 0.0

    if mode == 'intersection':
        labels = set(tree1.label_set) & set(tree2.label_set)
    else:
        labels = set(tree1.label_set) | set(tree2.label_set)

    for triple in combinations(labels, 3):
        missing, num, dem = is_equal_struct(triple, tree1.LCA, tree2.LCA)
        numerator += num
        if missing:
            denominator_u += dem
        else:
            denominator_i += dem

    similarity_score = 0
    if mode == 'intersection':
        similarity_score = float(numerator) / denominator_i
    elif mode == 'union':
        similarity_score = float(numerator) / (denominator_i + denominator_u)
    else:
        similarity_score_i = float(numerator) / denominator_i
        similarity_score_u = float(numerator) / (denominator_i + denominator_u)

        if mode == 'sigmoid':
            similarity_score = similarity_score_u + \
                sigmoid(similarity_score_i, mult=sigmoid_mult) * \
                min(similarity_score_i - similarity_score_u, similarity_score_u)

        elif mode == 'geometric':
            similarity_score = np.sqrt(
                similarity_score_i * similarity_score_u
            )

    return similarity_score


def build_tree(T, labeled_only=False, exclude=None):
    """
    Builds the MP3-treesim tree representation from a networkx representation.

    NOTE: the tree must have a attribute `label` for each node. Labels in a node
    must be separated by a comma.

    Parameters:
    T (nx.nx_agraph): Tree in networkx representation
    labeled_only (bool): If true nodes without attribute `label` 
    will be ignored, meaning that T is a partially labeled tree.
    exclude (list(str)): List of labels to exclude from computation

    Returns:
    Tree: MP3-treesim tree representation

    """

    if not nx.is_tree(T):
        raise ValueError("Not a valid tree.")

    label_to_nodes = defaultdict(set)
    label_set = set()
    node_to_labels = defaultdict(set)

    for node in T.nodes(data=True):
        id_node = node[0]

        if not 'label' in node[1] and not labeled_only:
            node[1]['label'] = str(node[0])
        if not 'label' in node[1] and labeled_only:
            node[1]['label'] = ''
            continue

        labels = node[1]['label'].split(',')
        for l in labels:
            if exclude:
                if l in exclude:
                    continue

            label_set.add(l)
            label_to_nodes[l].add(id_node)
            node_to_labels[id_node].add(l)

    label_set = sorted(list(label_set))

    return Tree(T, label_to_nodes, node_to_labels, label_set)


def read_dotfile(path, labeled_only=False, exclude=None):
    """ 
    Reads a dot file and returns its MP3-treesim tree representation.

    NOTE: the tree should have an attribute `label` for each node. 
    In case this is not true, the label of the node will be it's ID.    
    It recommended to use the `label` attribute.
    Labels in a node must be separated by a comma.

    Parameters: 
    path (str): Path to the dot file
    labeled_only (bool): If true nodes without attribute `label` will be ignored, meaning that T is a partially labeled tree.
    exclude (list(str)): List of labels to exclude from computation

    Returns: 
    Tree: MP3-treesim tree representation

    """

    T = nx.DiGraph(nx.drawing.nx_agraph.read_dot(path))

    return build_tree(T, labeled_only=labeled_only, exclude=exclude)


def read_dotstring(string, labeled_only=False, exclude=None):
    """ 
    Reads a string containing a dot graph and returns its MP3-treesim tree representation.

    NOTE: the tree should have an attribute `label` for each node. 
    In case this is not true, the label of the node will be it's ID.    
    It recommended to use the `label` attribute.
    Labels in a node must be separated by a comma.

    Parameters: 
    string (str): dot representation of the tree
    labeled_only (bool): If true nodes without attribute `label` will be ignored, meaning that T is a partially labeled tree.
    exclude (list(str)): List of labels to exclude from computation

    Returns: 
    Tree: MP3-treesim tree representation

    """

    T = nx.DiGraph(nx.drawing.nx_agraph.from_agraph(AGraph(string=string)))

    return build_tree(T, labeled_only=labeled_only, exclude=exclude)


def draw_tree(tree):
    """ 
    Draw the tree using networkx's drawing methods.

    NOTE 1: Networlx uses matplotlib to display the tree. If you are using a Notebook-like
    environment (Jupyter, CoLab) it will be display automatically. 
    If you are using it from command line it will be necessary to run `plt.show()` to 
    diplay it.

    NOTE 2: Due to an unreliable behaviour of netxwork and pygraph it is necessary to
    create a copy of the input tree and loop over the nodes twice. Beware this in case
    you want to display very large trees.

    Parameters: 
    tree: MP3-treesim tree representation

    """

    drawtree = nx.convert_node_labels_to_integers(tree.T)
    labels = nx.get_node_attributes(drawtree, 'label')

    for node in drawtree.nodes(data=True):
        del node[1]['label']

    try:
        pos = nx.nx_pydot.pydot_layout(drawtree, prog='dot')
    except:
        pos = None

    nx.draw_networkx(
        drawtree, pos=pos, labels=labels)
