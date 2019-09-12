#!/usr/bin/env python
# coding: utf-8

import pygraphviz as pgv


def draw_graph(out_file_name):
    """
    """

    # init empty graph
    A = pgv.AGraph()

    # set some default node attributes
    A.node_attr['style']='filled'
    A.node_attr['shape']='circle'

    # Add edges (and nodes)
    A.add_edge(1,2)
    A.add_edge(2,3)
    A.add_edge(1,3)

    # layout with default (neato)
    A.layout()

    # draw png
    png = A.draw(format='png')

    # print dot file to standard output
    # print(A.string())

    # write
    with open(out_file_name, 'w') as f_out:
        f_out.write(A.string())


def draw_graph2(out_file_name):
    """
    https://github.com/pgv/pygraphviz/blob/master/examples/subgraph.py
    """

    # init empty graph
    A = pgv.AGraph(directed=True)
    A.node_attr['fontname'] = 'helvetica'
    A.node_attr['shape'] = 'box'

    A.add_node("aardvark")

    items0 = ["coyote", "dingo", "dog", "fox", "jackal", "wolf"]
    items1 = ["cat", "lion", "tiger"]
    items2 = ["hippo", "ibex", "javelina", "kangaroo"]

    add_nodes_and_connect(A, items0)
    add_nodes_and_connect(A, items1)
    add_nodes_and_connect(A, items2)

    B = A.add_subgraph(items0, name='cluster0', label='canids', rank='same')
    B.graph_attr['rank'] = 'same'

    A.add_edge("aardvark", items0[0])

    B = A.add_subgraph(items1, name='cluster1', label='felines')

    A.add_edge(items0[-1], items1[0])

    B = A.add_subgraph(items2, name='cluster2', label='other', rank='same')

    A.add_edge(items1[-1], items2[0])

    # write
    with open(out_file_name, 'w') as f_out:
        f_out.write(A.string())


def add_nodes_and_connect(graph, items):
    previous_item = None

    for item in items:
        graph.add_node(item)
        if previous_item is not None:
            graph.add_edge(previous_item, item)

        previous_item = item


if __name__ == '__main__':

    # draw_graph('./data/g.dot')
    draw_graph2('./data/g2.dot')
