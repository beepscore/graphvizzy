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
    A = pgv.AGraph()

    # add some edges
    A.add_edge(1,2)
    A.add_edge(2,3)
    A.add_edge(1,3)
    A.add_edge(3,4)
    A.add_edge(3,5)
    A.add_edge(3,6)
    A.add_edge(4,6)

    # make a subgraph with rank='same'
    B = A.add_subgraph([4,5,6],name='s1',rank='same')
    B.graph_attr['rank']='same'

    # write
    with open(out_file_name, 'w') as f_out:
        # write A not B
        f_out.write(A.string())


def draw_graph3(out_file_name):
    """
    """

    # init empty graph
    A = pgv.AGraph()
    A.node_attr['fontname'] = 'helvetica'
    A.node_attr['shape'] = 'box'

    items = ["aardvark", "bull", "cheetah", "dog", "emu", "frog", "gopher", "hippo", "ibex", "javelina", "kangaroo"]

    previous_item = None

    for item in items:
        A.add_node(item)
        if previous_item is not None:
            # TODO: fix edges not showing. Need to use a directed graph?
            A.add_edge(previous_item, item)

        previous_item = item

    # make a subgraph with rank='same'
    B = A.add_subgraph(["bull", "emu", "gopher"], name='cluster1', rank='same')
    B.graph_attr['rank']='same'

    # write
    with open(out_file_name, 'w') as f_out:
        f_out.write(A.string())


if __name__ == '__main__':

    # draw_graph('./data/g.dot')
    # draw_graph2('./data/g2.dot')
    draw_graph3('./data/g3.dot')
