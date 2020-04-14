#!/usr/bin/env python3
from igraph import *
import csv

def main():

    points = []

    with open("source.csv") as f:
        reader = csv.reader(f)
        titles = next(reader)
        titles.pop(0) # first item in CSV headers is always empty
        for rowIndex, row in enumerate(reader):
            rowTitle = row.pop(0) # remove name of row
            for colIndex, col in enumerate(row):
                colTitle = titles[colIndex]
                print(rowTitle, '->', colTitle, ': ', col)
                colLoopIndex = 0
                while colLoopIndex < int(col):
                    points.append((int(rowIndex),int(colIndex)))
                    colLoopIndex += 1


    g = Graph(points)
    g.vs["name"] = titles
    g.vs["label"] = g.vs["name"]

    layout = g.layout("kk")

    visual_style = {}
    visual_style["vertex_size"] = 20
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["layout"] = layout
    visual_style["bbox"] = (300, 300)
    visual_style["margin"] = 20

    plot(g, "social_network.svg", **visual_style)

if __name__ == "__main__":
    main()
