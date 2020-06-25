# Help on module mp3treesim:

## NOTE
    This is a documentation of the exposed FUNCTIONS only.

## NAME
    mp3treesim - # coding: utf-8

## FUNCTIONS
    build_tree(T, labeled_only=False, exclude=None)
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
        
    read_dotfile(path, labeled_only=False, exclude=None)
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

    read_dotstring(string, labeled_only=False, exclude=None)
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

    draw_tree(tree):
        Draw the tree using networkx's drawing methods.

        NOTE 1: Networkx uses matplotlib to display the tree. If you are using a Notebook-like
        environment (Jupyter, CoLab) it will be display automatically. 
        If you are using it from command line it will be necessary to run `plt.show()` to 
        display it.

        NOTE 2: Due to an unreliable behaviour of netxwork and pygraph it is necessary to
        create a copy of the input tree and loop over the nodes twice. Beware this in case
        you want to display very large trees.

        Parameters: 
        tree: MP3-treesim tree representation

    similarity(tree1, tree2, mode='sigmoid', cores=1)
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
        cores (int); Number of cores used for the computation.
        
        Returns: 
        float: Similarity score