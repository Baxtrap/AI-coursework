from graphviz import Digraph

def tree_pic(tree):
    tree_graph = visualize_tree(tree)
    tree_graph.render('/mnt/data/tree', format='png', view=False)
    tree_graph.render('tree', format='png', view=True)

def visualize_tree(pathway, parent=None, edge_label="", graph=None):
    if graph is None:
        graph = Digraph(comment='Decision Tree')
        graph.attr(ranksep='4')
        graph.attr(nodesep='1.5')

    if isinstance(pathway, dict):
        for branch, subtree in pathway.items():
            if isinstance(subtree, dict):
                node_name = str(id(subtree))
                graph.node(node_name, label=str(branch))
                if parent:
                    graph.edge(parent, node_name, label=edge_label)
                visualize_tree(subtree, parent=node_name, graph=graph)
            else:
                if subtree in {'acc', 'unacc', 'good', 'vgood'}:
                    leaf_name = f"leaf_{str(id(subtree))}"
                    graph.node(leaf_name, label=str(subtree), shape='box')
                    graph.edge(parent, leaf_name, label=str(branch))
    else:
        if pathway in {'acc', 'unacc', 'good', 'vgood'}:
            leaf_name = f"leaf_{str(id(pathway))}"
            graph.node(leaf_name, label=str(pathway), shape='box')
            if parent:
                graph.edge(parent, leaf_name, label=edge_label)

    return graph
