#!/usr/bin/env python
# coding: utf-8

import pygraphviz as pgv


def draw_graph(out_file_name):

    # init empty graph
    a = pgv.AGraph()

    # set some default node attributes
    a.node_attr['style'] = 'filled'
    a.node_attr['shape'] = 'circle'

    # Add edges (and nodes)
    a.add_edge(1, 2)
    a.add_edge(2, 3)
    a.add_edge(1, 3)

    # layout with default (neato)
    a.layout()

    # draw png
    png = a.draw(format='png')

    # print dot file to standard output
    # print(A.string())

    # write
    with open(out_file_name, 'w') as f_out:
        f_out.write(a.string())


def draw_graph2(out_file_name):
    """
    https://github.com/pgv/pygraphviz/blob/master/examples/subgraph.py
    """

    # init empty graph
    a = pgv.AGraph(directed=True)
    a.node_attr['fontname'] = 'helvetica'
    a.node_attr['shape'] = 'box'

    a.add_node("aardvark")

    items0 = ["coyote", "dingo", "dog", "fox", "jackal", "wolf"]
    items1 = ["cat", "lion", "tiger"]
    items2 = ["hippo", "ibex", "javelina", "kangaroo"]
    items3 = ["horse", "zebra", "donkey"]

    add_nodes_connected_by_edges(a, items0, False)
    add_nodes_connected_by_edges(a, items1, False)
    add_nodes_connected_by_edges(a, items2, False)

    b = a.add_subgraph(items0, name='cluster0', label='canids', rank='same')

    a.add_edge("aardvark", items0[0])

    b = a.add_subgraph(items1, name='cluster1', label='felines')

    a.add_edge(items0[-1], items1[0])

    b = a.add_subgraph(items2, name='cluster2', label='other', rank='same')

    a.add_edge(items1[-1], items2[0], rank='same')

    a.add_nodes_from(items3)

    b = a.add_subgraph(items3, name='cluster3', label='equids', rank='same')

    # write .dot file
    with open(out_file_name, 'w') as f_out:
        f_out.write(a.string())


def draw_graph3(out_file_name):
    a = pgv.AGraph(directed=True)

    items0 = ["coyote", "wolf"]
    items1 = ["lion", "tiger"]
    items2 = ["mouse", "rat"]
    items3 = ["horse", "zebra"]

    # add nodes, not connected by edges. These appear at same level
    a.add_nodes_from(items0)

    # add nodes connected by edges
    add_nodes_connected_by_edges(graph=a, items=items1, constraint=True)
    add_nodes_connected_by_edges(graph=a, items=items2, constraint=False)
    add_nodes_connected_by_edges(graph=a, items=items3, constraint=False)

    b = a.add_subgraph(items3, name='cluster3', label='equids')

    # write .dot file
    with open(out_file_name, 'w') as f_out:
        f_out.write(a.string())


def add_nodes_connected_by_edges(graph: pgv.AGraph, items: [str], constraint: bool) -> pgv.AGraph:
    """
    Adds nodes to graph, one node per string in items
    :param graph: a pygraphviz graph
    :param items: a list of strings
    :param constraint: if False, the edge is not used in ranking the nodes
    """
    previous_item = None

    for item in items:
        graph.add_node(item)
        if previous_item is not None:
            # rank: If rank="same", all nodes are placed on the same rank.
            # https://graphviz.gitlab.io/_pages/doc/info/attrs.html#d:rank
            # constraint: If False, the edge is not used in ranking the nodes.
            # https://stackoverflow.com/questions/22756929/graphviz-make-edges-not-affecting-the-hierarchy-of-nodes
            # https://graphviz.gitlab.io/_pages/doc/info/attrs.html#d:constraint
            graph.add_edge(previous_item, item, rank='same', constraint=constraint)

        previous_item = item


if __name__ == '__main__':

    # draw_graph('./data/g.dot')
    # draw_graph2('./data/g2.dot')
    draw_graph3('./data/g3.dot')
