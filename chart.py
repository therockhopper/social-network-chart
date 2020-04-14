#!/usr/bin/env python3
from igraph import *
import csv

def main():

    points = []
    size_dict = {}

    with open("source.csv") as f:
        reader = csv.reader(f)
        titles = next(reader)
        titles.pop(0) # first item in CSV headers is always empty
        size_dict = {el:0 for el in titles}
        for rowIndex, row in enumerate(reader):
            rowTitle = row.pop(0) # remove name of row
            for colIndex, col in enumerate(row):
                colTitle = titles[colIndex]
                size_dict[rowTitle] += int(col)
                if int(col) > 0:
                    points.append((int(rowIndex),int(colIndex)))


    print(size_dict)
    g = Graph(points)
    g.vs["name"] = titles
    g.vs["label"] = g.vs["name"]

    layout = g.layout("kk")

    visual_style = {}
    visual_style["vertex_size"] = [size_dict[name] for name in g.vs["name"]]
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["vertex_label_dist"] = 1
    visual_style["layout"] = layout
    visual_style["edge_curved"] = 0
    visual_style["edge_width"] = [(int(size_dict[name]) / 10) for name in g.vs["name"]]
    visual_style["margin"] = 50

    plot(g, "social_network.pdf", **visual_style)

if __name__ == "__main__":
    main()
