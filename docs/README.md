# Help on module mp3treesim:

## NOTE
    This is a documentation of the exposed FUNCTIONS only.

## NAME
    mp3treesim - # coding: utf-8

## FUNCTIONS
    build_tree(T)
        Builds the MP3-treesim tree representation from a networkx representation.
        
        NOTE: the tree must have a attribute `label` for each node. Labels in a node
        must be separated by a comma.
        
        Parameters:
        T (nx.nx_agraph): Tree in networkx representation
        
        Returns:
        Tree: MP3-treesim tree representation
        
    read_dotfile(path)
        Reads a dot file and returns its MP3-treesim tree representation.
        
        NOTE: the tree must have a attribute `label` for each node. Labels in a node
        must be separated by a comma.
        
        Parameters: 
        path (str): Path to the dot file
        
        Returns: 
        Tree: MP3-treesim tree representation
        
    similarity(tree1, tree2, mode='sigmoid')
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