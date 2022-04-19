from email.policy import default
from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createRandomSpheres",
    name = "Create Random Spheres",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("radius", "R", "Size of radius",hs.HopsParamAccess.ITEM),
        
    ],
    outputs=[
       hs.HopsPoint("Random Spheres","RS","List of generated random sphere ", hs.HopsParamAccess.LIST)
    ]
)
def createRandomSpheres(count, rX, rY, rZ, rR):

    randomSpheres = []
    for i in range(count):

        #in each itereation generate some random Spheres
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)
        random_z = r.uniform(-rZ, rZ)
        random_r = r.uniform(-rR, rR)
       
        #create a Sphere with rhino3dm
        random_center = rg.Point3d(random_x, random_y, random_z)
        random_Sphere = rg.Sphere(random_center, random_r)
        
        #add point to the list
        randomSpheres.append(random_Sphere)

    return randomSpheres



@hops.component(
  "/moreRandomSphere",
    name = "More Random Sphere",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("R range of randomness", "R", "Maximum randomness for Radius", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
       hs.HopsBrep("Random Spheres","RS","List of generated random Spheres ", hs.HopsParamAccess.LIST)
    ]
)
def moreRandomSphere(count, rX, rY, rZ, rR):

    randomSphere = geo.createRandomSphere(count, rX, rY, rZ, rR)
    return randomSphere






if __name__== "__main__":
    app.run(debug=True)