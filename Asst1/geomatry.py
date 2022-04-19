import random as r
import rhino3dm as rg
import networkx as nx



def moveLine(line,X,Y,Z):
    start=line.PointAtStart #gives a point3d at the start of the line
    end=line.PointAtEnd
    moved_start=rg.Point3d(X+start.X, Y+start.Y, Z+start.Z)
    moved_end=rg.Point3d(X+end.X, Y+end.Y, Z+end.Z)
    moved=rg.LineCurve(moved_start, moved_end)

    return moved



def complete(nn):
    G = nx.complete_graph(nn)
    lay = nx.kamada_kawai_layout(G)

    nodes = []
    for n in lay.values():
        pt = rg.Point3d(n[0], n[1] , 0)
        nodes.append(pt)
    
    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return nodes, edges