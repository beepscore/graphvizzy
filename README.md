# Purpose
Use Python, pygraphviz, graphviz and dot to draw a graph.

# References

## pygraphviz
https://github.com/pygraphviz/pygraphviz

## graphviz
https://graphviz.gitlab.io/_pages/doc/info/command.html
https://graphviz.gitlab.io/_pages/doc/info/attrs.html

# Results

## install pygraphviz
I used Anaconda

    conda activate beepscore_data_science

## run script

    python graphvizzy.py

## dot command

    dot -Tpng g.dot -o g.png

    dot -Tpng ./data/g2.dot -o ./data/g2.png
