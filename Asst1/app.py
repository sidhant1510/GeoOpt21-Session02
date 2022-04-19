import imp
from flask import Flask
import ghhops_server as hs


import geomatry as geo
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/moveLine",
    name = "Create moved Points",
    inputs=[
        hs.HopsCurve("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("X range of randomness", "X", "Value of motion in X direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Value of motion in Y direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Value of motion in Z direction", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsCurve("Random Points","RP","List of generated random points ", hs.HopsParamAccess.ITEM)
    ]
)
def moveLine(line,X,Y,Z):
    moved = geo.moveLine(line,X,Y,Z)
    return moved



@hops.component(
    "/complete",
    name = "Create complete graph",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of ]Points", hs.HopsParamAccess.ITEM),

    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def complete(nn):
    nodes = geo.complete(nn) [0]
    edges = geo.complete(nn) [1]
    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)


