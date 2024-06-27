###########################################
##              SECTION 1                ##
##   Python for Maya : Scripts & Notes   ##
##          @jenull // 6.2024            ##
###########################################

## run the following command into Maya's script editor under MEL, makes the connection btwn VSCode and Maya  
## commandPort -name "localhost:7001" -sourceType "mel"
## "commandPort -n "localhost:7001" -stp "mel" -echoOutput;" <-- sometimes i get an error with this similar command bc of the "echoOutput", but i think the shorthand names work though

def mayaPythonConnection():
    ## connecting python + maya import

    from maya import cmds
#mayaPythonConnection()

def makeCube():
    ## make default cube using ".polyCube()" & assign it to a variable named "cube"

    from maya import cmds

    cube = cmds.polyCube() # creates a var named "cube" and assigns it a polyCube object
    print(cube) # returns a list >>[u'pCube1','polyCube1']. Prints a list of 2 items: 1. the name of the cube (see note below !!), 2. the name of the maya node that created the cube.
    print(cube[0]) # returns a str >> "pCube1" prints a String which is the name of the cube (NOT the variable name we made, it returns the name of the cube in the scene/outliner based on the other existing cubes/objects in the scene)
#makeCube()

def parentObjectsTogether():
    ## parents one object over another using ".parent", "grouping" or "foldering" in a sense...

    from maya import cmds

    cube1_parent = cmds.polyCube()
    cube1_parentName = cube1_parent[0] # have to get name of child object to grab the variable, can't grab it from the og var since it is a list type, remember???

    cube2_child = cmds.polyCube()
    cube2_childName = cube2_child[0] 

    cmds.parent(cube2_childName, cube1_parentName) # the parent function, 2 parameters: child, parent (in that order !!)
#parentObjectsTogether()

def lockMovementForObjects():
    ## lock the x,y,z or all axes of an object using "setAttr", so user can not rotate, scale, or translate object on locked axes

    from maya import cmds

    # cube = cmds.polyCube()
    # cubeName = cube[0]
    cubeName = (cmds.polyCube())[0] # a shortcut version for the above !

    cmds.setAttr(cubeName+".tx", lock=True) #grabs cubeName variable and locks (lock = True) the Translate X axis (.tx) 
    # ^^ also other shorthands: "ty" (translate y-axis), "sz" (scale z-axis), "rx" (rotate x-axis), ".translate" (translate all axes), etc. etc. & any other combos
#lockMovementForObjects()

def selectObject():
    ## simply highlights or selects (.select) an object in the scene/outliner

    from maya import cmds

    cube1 = (cmds.polyCube())[0] 
    cube2 = (cmds.polyCube())[0] 
    cube3 = (cmds.polyCube())[0] 

    cmds.select(cube2) #doesn't necessarily selects the specific "cube2" object you created... it selects the new second cube that you are pushing into the scene...if that makes sense
    # ex. if we already have pCube1, pCube2, and pCube3 in the scene. RUNNING THIS CODE will create into the outliner+scene: pCube4, pCube5, & pCube6. AND it will select pCube5 since it is the second cube assigned to the variable "cube2"
    # !! --> cmds.select("pCube6") --> use quotes to select the specific object name you want (based on the outliner)
#selectObject()

def listReview():
    return 0

def tupleReview():
    return 0

def setReview():
    return 0

def dictionaryReview():
    return 0