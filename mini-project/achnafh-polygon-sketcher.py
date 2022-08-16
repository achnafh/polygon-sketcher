from turtle import *
import math

# DATABASE
menuList = {"Create": [(-580, 330), "#fca503"], "Import": [(-580, 270), "#fca503"],\
            "Edit": [(-580,210),"#fca503"],   "Move": [(-580,150), "#fca503"], \
            "Scale": [(-580, 90), "#fca503"], "Rotate": [(-580, 30), "#fca503"], \
            "Test":[(-580,-30), "#fca503"],   "Duplicate":[(-580,-90),"#fca503"], \
            "Save":[(-580,-150), "#fca503"],   "Delete": [[-580,-210], "#fca503"],\
            "Export": [[-580,-270], "#fca503"], " ": [[-580,-330], "#ffffff"],}
# globalPoly = [{"outlinecolor": "green", fillcolor" : "red","coors":[[points], }]
globalPoly = []
poly = []
tempColor = [] # [outline, fillcolor]

#State
notDrawing = True
currentlyDrawing = False
editable = False
polygonCreated = False

## INITIATE PROGRAM ##
scr = Screen()
naf = Turtle()
terminal = Turtle()
testOutput = Turtle()
doneStatus = False

#Main turtle
naf.hideturtle()
naf.shape("circle")
naf.speed(0)
naf.shapesize(0.5)
naf.pensize(2)
testOutput.hideturtle()
testOutput.penup()
testOutput.goto(0,-400)

#Setup screen
def screenSetup():
    scr.setup(width = 1450, height = 900, startx = 0, starty = 0)
    scr.title("Polygon Creator")
    scr.bgcolor("#ffe900")
    return scr

#Layout Setup
def origin(item):
    origin = Turtle()
    origin.shape("circle")
    origin.shapesize(0.2)
    origin.color("red")
    if item == "global" :
        origin.goto(0,0)
        return origin

    elif item == "local":
        origin.pu()
        origin.color("blue")
        origin.goto(-50,-15)
        return origin
def draw_area():
    draw = Turtle()
    draw.hideturtle()
    draw.speed(0)
    draw.penup()
    draw.goto(-500,-370)
    draw.pd()
    draw.fillcolor("white")
    draw.pencolor("black")
    draw.pensize(2)
    draw.begin_fill()
    #border
    for i in range(1,5):
        if i%2 == 0:
            draw.forward(740)
            draw.left(90)
        else:
            draw.fd(1000)
            draw.left(90)
    draw.end_fill()
    draw.pu()
    draw.goto(-370,375)
    draw.pencolor("black")
    draw.write("POLYGON SKETCHER", align = "center", font = ("roboto", 25, "bold"))
    return draw

def colorizeButton():
    global menuList
    # if len(globalPoly) == 0:
    #     currentlyDrawing = False
    #     editable = False
    #     notDrawing = True

    if currentlyDrawing and not editable and not notDrawing:
        menuList["Create"][1] = "#c1c4ad"
        menuList["Import"][1] = "#c1c4ad"
        menuList["Edit"][1] = "#c1c4ad"
        menuList["Move"][1] = "#c1c4ad"
        menuList["Scale"][1] = "#c1c4ad"
        menuList["Rotate"][1] = "#c1c4ad"
        menuList["Test"][1] = "#c1c4ad"
        menuList["Duplicate"][1] = "#c1c4ad"
        menuList["Save"][1] = "#c1c4ad"
        menuList["Delete"][1] = "#c1c4ad"
        menuList["Export"][1] = "#c1c4ad"
    
    elif polygonCreated and not currentlyDrawing:
        menuList["Create"][1] = "#c1c4ad"
        menuList["Import"][1] = "#c1c4ad"
        menuList["Edit"][1] = "#c1c4ad"
        menuList["Move"][1] = "#c1c4ad"
        menuList["Scale"][1] = "#c1c4ad"
        menuList["Rotate"][1] = "#c1c4ad"
        menuList["Test"][1] = "#c1c4ad"
        menuList["Duplicate"][1] = "#c1c4ad"
        menuList["Save"][1] = "#fca503"
        menuList["Delete"][1] = "#c1c4ad"
        menuList["Export"][1] = "#c1c4ad"
    
    else:
        if notDrawing and not editable:
            menuList["Create"][1] = "#fca503"
            menuList["Import"][1] = "#fca503"
            menuList["Edit"][1] = "#c1c4ad"
            menuList["Move"][1] = "#c1c4ad"
            menuList["Scale"][1] = "#c1c4ad"
            menuList["Rotate"][1] = "#c1c4ad"
            menuList["Test"][1] = "#c1c4ad"
            menuList["Duplicate"][1] = "#c1c4ad"
            menuList["Save"][1] = "#c1c4ad"
            menuList["Delete"][1] = "#c1c4ad"
            menuList["Export"][1] = "#c1c4ad"
        

        if notDrawing and editable:
            menuList["Create"][1] = "#fca503"
            menuList["Import"][1] = "#fca503"
            menuList["Edit"][1] = "#fca503"
            menuList["Move"][1] = "#fca503"
            menuList["Scale"][1] = "#fca503"
            menuList["Rotate"][1] = "#fca503"
            menuList["Test"][1] = "#fca503"
            menuList["Duplicate"][1] = "#fca503"
            menuList["Save"][1] = "#fca503"
            menuList["Delete"][1] = "#fca503"
            menuList["Export"][1] = "#fca503"
    

#Layout Menu
def menuShape(item, pos, color):
    global globalPoly
    box = Turtle()
    scr.tracer(0)
    box.hideturtle()
    box.speed(0)
    box.penup()
    box.goto(pos[0], pos[1])
    box.pendown()
    box.pencolor("black")
    
    box.fillcolor(color)
    box.pensize(2)
    box.begin_fill()
    for i in range(1,5):
        if i % 2 == 0:
            box.fd(40)
            box.left(90)
        else: 
            box.fd(70)
            box.left(90)
    box.penup()
    box.end_fill()
    
    box.goto(pos[0]+35, pos[1]+10)
    box.write(f"{item}", align = "center", font=("ds-digital", 15, "normal") )
    scr.update()
    return box

def controlMenu():
    scr.tracer(0)
    colorizeButton()
    for i in menuList:
        menuShape(i,menuList[i][0], menuList[i][1])
    scr.update()

#Layout Grid:
def drawAxis():
    axis = Turtle()
    axis.penup()
    axis.speed(0)
    axis.pencolor("red")
    axis.fillcolor("red")
    axis.pensize(3)
    axis.goto(-600,-400)
    axis.pd()
    axis.forward(1100)
    axis.stamp()
    axis.penup()
    axis.goto(-600,-400)
    axis.left(90)
    axis.pd()
    axis.forward(770)
    axis.stamp()

    #origin
    axis.pu()
    axis.goto(-600,-415)
    axis.color("black")
    axis.hideturtle()
    axis.write("(0,0)", align = "center", font = ("ds-digital", 12, "bold"))

    #Y axis
    axis.pu()
    axis.goto(-615, 355)
    axis.write("y", align = "center", font = ("ds-digital", 15, "normal"))

    #X Axis
    axis.goto(490,-425)
    axis.write("x", align = "center", font = ("ds-digital", 15, "normal"))
    return axis
def layoutGrid(axis):
    grid = Turtle()
    scr.tracer(0)
    grid.speed(0)
    grid.hideturtle()
    grid.color("#948e7f")
    grid.pensize(0.3)
    grid.pu()
    grid.goto(-500,-370)
    grid.pd()

    if axis == "y":
        for k in range (1, 101) :
            if k%2 == 0:
                grid.fd(10)
                grid.right(90)
                grid.fd(740)
                grid.left(90)
            else:
                grid.fd(10)
                grid.left(90)
                grid.fd(740)
                grid.right(90)
                
    elif axis == "x":
        grid.left(90)
        for k in range (1, 75) :
            if k%2 == 0:
                grid.fd(10)
                grid.left(90)
                grid.fd(1000)
                grid.right(90)
            else:
                grid.fd(10)
                grid.right(90)
                grid.fd(1000)
                grid.left(90)
    scr.update()
    return grid

#Terminal
def terminalLayout():
    global terminal
    terminal.pu()
    terminal.speed(0)
    terminal.hideturtle()
    terminal.goto(510,370)
    terminal.fillcolor("#ffe900")
    terminal.pencolor("black")
    terminal.pensize(2)
    terminal.pd()
    terminal.begin_fill()
    for i in range(1,5):
        if i%2 != 0:
            terminal.fd(190)
            terminal.right(90)
        else:
            terminal.fd(735)
            terminal.right(90)
    terminal.end_fill()

    terminal.pu()
    terminal.goto(565,345)
    terminal.color("black")
    terminal.write("TERMINAL :", align = "center", font=("ds-digital", 18, "normal"))
    terminal.goto(510,338)
    terminal.pd()
    terminal.setheading(0)
    terminal.fd(190)
    terminal.pu()
    return terminal

def layoutFunc():
    scr.tracer(0)
    scr.update()
    return screenSetup(), draw_area(), controlMenu(), terminalLayout(), layoutGrid("x"), layoutGrid("y")

#Intersection Detector
def compareGradient(a,b,p):
    return (b[1]-p[1])*(a[0]-p[0]) > (b[0]-p[0])*(a[1]-p[1])
def intersecting(a,b,p,q):
    return compareGradient(a,b,p) != compareGradient(a,b,q) and compareGradient(p,q,a) != compareGradient(p,q,b)

#Color filling:
def fillColor():
    colorInput=textinput("Polygon Color", "Type your desired fillcolor!\ne.g: red or hex code")
    while True:
        try: 
            if colorInput != "":
                naf.fillcolor(colorInput)
                naf.begin_fill() #Error Checking
                naf.end_fill()
                tempColor.insert(1,colorInput)
                break
            else:
                colorInput = textinput ("Polygon Fillcolor", "Invalid Fillcolor Input!\n\nPlease type in your desired Color!\ne.g: blue or hex code")

        except:
            colorInput = textinput ("Polygon Fillcolor", "Invalid Fillcolor Input!\n\nPlease type in your desired Color!\ne.g: blue or hex code")

def outlineColor():
    outlineInput = textinput("Polygon Outline Color", "Type in your desired outline color!\ne.g: black or hex code")
    while True:
        try: 
            if outlineInput != "":
                naf.pencolor(outlineInput)
                naf.color(outlineInput)
                tempColor.insert(0,outlineInput)
                break
            else:
                outlineInput = textinput("Polygon Outline", "Invalid Outline Color Input!\n\ne.g: blue or hex code")
        except:
            outlineInput = textinput("Polygon Outline", "Invalid Outline Color Input!\n\ne.g: blue or hex code")

def colorizePoly():
    outlineColor()
    fillColor()

#Tools
def reprintPoly(vertices, color, outlinecolor):
    global globalPoly, poly, tempColor, editable, notDrawing
    naf.pu()
    naf.fillcolor(color)
    naf.pencolor(outlinecolor)
    naf.begin_fill()
    naf.goto(vertices[0])
    for i in range(0,len(vertices)):
        naf.pd()
        naf.goto(vertices[i])
        naf.stamp()
    naf.goto(vertices[0])
    naf.stamp()
    naf.end_fill()
    naf.pu()

def displayPoly():
    naf.clear()
    for i in globalPoly:
        reprintPoly(i["coors"],i["fillcolor"], i["outlinecolor"])
    controlMenu()

def centroid(vertices):
    global globalPoly, poly
    polyVertices= list(vertices)
    xlist = [i[0] for i in polyVertices]
    ylist = [i[1] for i in polyVertices]
    n = len(polyVertices)
    x_ave = sum(xlist) / n
    y_ave = sum(ylist) / n
    return (x_ave, y_ave)

def validCheck(polygon, index, function, selectedPolygon, duplicate = False):
    invalid = False
    vertices = polygon["coors"]

    if index == False and function == False and selectedPolygon == False:
        for i in vertices:
            if -500 < i[0] < 500 and -370 < i[1] < 370:
                continue
            else: 
                invalid = True
                break
        if invalid:
            textinput("Error", "Error occured as the vertices exceed the drawing area.\nEdit the textfile vertices, please.\n\nClick enter to continue.")
            return
        else:
            globalPoly.append(polygon)
            displayPoly()
            terminalWindow()

    else:
        for i in vertices:
            if -500 < i[0] < 500 and -370 < i[1] < 370:
                continue
            else: 
                invalid = True
                break

        if invalid:
            textinput("Error", "Error occured as the vertices exceed the drawing area\n\nClick enter to continue.")
            globalPoly.insert(index-1, selectedPolygon)
            function()
        else: 
            if duplicate == False:
                globalPoly.insert(index-1, polygon)
            else:
                globalPoly.insert(index-1, selectedPolygon)
                globalPoly.append(polygon)
            displayPoly()
            terminalWindow()

def findArea(vertices):
    shoelist = list(vertices)  + [vertices[0]]
    area = 0
    for i in range(len(vertices)-1):
        area += shoelist[i][0]*shoelist[i+1][1]
        area -= shoelist[i][1]*shoelist[i+1][0]
    area /= 2
    return abs(area)

def findPerimeter(vertices):
    jumplist = list(vertices) + [vertices[0]]
    perimeter = 0
    for i in range(len(jumplist)-1):
        perimeter += math.sqrt((jumplist[i][0]-jumplist[i+1][0])**2 + (jumplist[i][1]-jumplist[i+1][1])**2)
    return perimeter

def terminalWindow():
    global terminal
    x = 520
    y = 235
    terminal.clear()
    terminalLayout()
    terminal.pu()

    if len(globalPoly) == 0:
        return

    else:
        for i in range(0,len(globalPoly)):
            terminal.goto(x,y)
            perimeter = findPerimeter(globalPoly[i]["coors"])
            area = findArea(globalPoly[i]["coors"])
            terminal.write(f"Polygon {i+1} :\nOutline      = {globalPoly[i]['outlinecolor']}\nColor        = {globalPoly[i]['fillcolor']}\nPerimeter = {perimeter:>4.2f}\nArea          = {area:>4.2f}", align = "left", font=("ds-digital", 15, "normal"))
            y -=100 
            terminal.pu

def polygonSelection(title, content):
    global globalPoly
    index = int(numinput(f"Choose a Polygon for {title}", f"\nTotal Polygon = {len(globalPoly)}\n\nWhich Polygon You Want to {content}?\ne.g: 1 / 2 / 3 /.."))
    while index>len(globalPoly) :
        index = int(numinput("Choose a Polygon", f"Invalid input!\nTotal Polygon = {len(globalPoly)}\n\nWhich polygon you want to {content}?\ne.g: 1 / 2 / 3 /.."))
    selectedPolygon = globalPoly.pop(index-1)
    vertices = selectedPolygon["coors"]
    fillcolor = selectedPolygon["fillcolor"]
    outlinecolor = selectedPolygon["outlinecolor"]
    return index, vertices, fillcolor, outlinecolor, selectedPolygon


#Create Menu:
def createByKeypress():
    global globalPoly, tempColor, poly, notDrawing, currentlyDrawing, editable
    scr.tracer(None)
    notDrawing = False
    editable = False
    currentlyDrawing = True
    controlMenu()
    invalid = False
    while True:   
        textDialog = textinput("Input Coordinates","Input a point!\ne.g: x1,y1\nRange:\n-500 < x < 500\n-370 < y < 370\nType 'done' to terminate.")   
        if textDialog == "done":
            for i in range(len(poly)-2):
                if intersecting(poly[-1],poly[0], poly[i], poly[i+1]):
                    invalid = True
            if invalid:
                popup = textinput("Line intersecting", "Line should not intersect, choose another points before stating done.\nHit enter to continue.")
                invalid = False
                continue
            else:
                tempCoor = (poly[0][0], poly[0][1])
                naf.goto(tempCoor)
                naf.end_fill()
                popup = textinput("Save Polygon","Click Save Button to save your polygon.\nHit enter to continue")
                globalPoly.append({"outlinecolor" : tempColor[0],"fillcolor": tempColor[1],"coors":tuple(poly)})
                poly.clear()
                tempColor.clear()
                editable = True
                notDrawing = True
                currentlyDrawing = False
                controlMenu()
                terminalWindow()
                break
            
        else:
            try:
                temp = textDialog.split(",")
                x = float(temp[0])
                y = float(temp[1])
                tempCoor = [x,y]
                if x<500 and x>-600 and y>-400 and y<370:
                    if len(poly) == 1:
                        naf.begin_fill()
                    if not poly:
                        naf.pu()
                    else:
                        naf.pd()
                        if len(poly)>2:
                            for i in range(len(poly)-2):
                                if intersecting(poly[-1], tempCoor, poly[i], poly[i+1]):
                                    popup = textinput("Invalid Input", "Point Should not Intersect! Hit Enter to reinput.")
                                    while popup != "":
                                        popup = textinput("Invalid Input", "Point Should not Intersect! Hit Enter to reinput.")
                                    if popup == "":
                                        invalid = True
                    if invalid:
                        invalid = False
                        continue
                    else:
                        naf.goto(tempCoor)
                        naf.stamp()
                        poly.append(tempCoor)
                else:
                    popup = textinput("Invalid Input","Coordinate Out of Bounds, Hit enter to continue.")
                    continue

            except:
                popup = textinput("Invalid Input","Invalid input, hit enter to continue.")
                continue
        scr.update()
    scr.onclick(menuClick)
def createByMouse(x,y):
    global doneStatus, tempColor, notDrawing, currentlyDrawing, editable, polygonCreated
    scr.tracer(None)
    tempCoor = [x,y]
    if doneStatus :
        if -580 < x < -510 and -150 < y < -110 : #Done Button
            polygonCreated = False
            saveButton()
            doneStatus = False

    else:
        if -500 < x < 500 and -370 < y < 370: #Drawing Area
            if len(poly) == 1:
                naf.begin_fill()
            if not poly:
                naf.pu()
            else:
                naf.pd()
                if len(poly) > 2:
                    for i in range(len(poly)-2):
                        if intersecting(poly[-1],tempCoor,poly[i], poly[i+1]):
                            popup = textinput("Invalid Input", "Point Should not Intersect! Hit Enter to reinput.")
                            while popup != "":
                                popup = textinput("Invalid Input", "Point Should not Intersect! Hit Enter to reinput.")
                            if popup == "":
                                done()
                                scr.onclick(createByMouse)
                
                if x < poly[0][0]+30 and x > poly[0][0]-30 and y < poly[0][1] + 30 and y > poly[0][1] - 30:
                    tempCoor = [poly[0][0], poly[0][1]]
                    naf.goto(tempCoor)
                    naf.end_fill()
                    naf.pu()
                    textinput("Polygon Status", "Polygon has been created.\nClick save button to save this new polygon.\n\n[Hit enter to proceed]")
                    polygonCreated = True
                    currentlyDrawing = False
                    controlMenu()
                    doneStatus = True
                    
            
            naf.goto(tempCoor)
            naf.stamp()
            poly.append(tempCoor)
        else:
            popup = textinput("Invalid Input","Coordinate Out of Bounds, Hit enter to continue.")
            while popup != "":
                popup = textinput("Invalid Input","Coordinate Out of Bounds, Hit enter to continue.")
            if popup == "":
                scr.onclick(createByMouse)
    scr.update()

def saveButton():
    global globalPoly,poly, notDrawing, tempColor, currentlyDrawing,editable
    scr.tracer(None)
    globalPoly.append({"outlinecolor": tempColor[0], "fillcolor": tempColor[1],"coors":tuple(poly)})
    poly.clear()
    tempColor.clear()
    notDrawing = True
    editable = True
    controlMenu()
    terminalWindow()
    popup = textinput("Pop-up", "Polygon Successfully Created, hit Enter to Continue!")
    if popup == "":
        notDrawing = True
        scr.onclick(menuClick)

def importButton():
    global editable, notDrawing
    editable = True
    notDrawing = True
    textinput("REMINDER", "Your drawn polygons will be deleted if you import an external file, are you sure to continue?\n\n[Click Enter to Proceed]")
    while True:
        filename = textinput("Import a textfile", "Please type in your textfile name without the extension (.txt)\ne.g: testfile")
        try:
            infile = open(filename + ".txt", "r")
            break
        except FileNotFoundError:
            textinput("Textfile Not Found Error", "File Not Found Error!\n\nInput should exclude the file extension.\nTry again, please.\n\n[Click Enter to Continue]")
    
    globalPoly.clear()
    for line in infile:
        clearEnd = line.strip("\n")
        cleanline = clearEnd.replace(" ","")
        tempList = cleanline.split(";")
        outline, colorfill = tempList[0], tempList[1]
        vertices = []

        for k in range(2,len(tempList)):
            coor = tempList[k].split(",")
            newx = float(coor[0])
            newy = float(coor[1])
            vertices.append([newx,newy])
        polygon = {"outlinecolor": outline, "fillcolor": colorfill, "coors": vertices}
        validCheck(polygon, False, False, False)
    controlMenu()
    infile.close()

def exportButton():
    alert = textinput("Alert","Are you sure you want to export your created polygons?\n\n[Click Enter to Continue]\n[Type 'cancel' to Cancel]")
    if alert == "cancel" or alert == "Cancel":
        scr.onclick(menuClick)
    else:
        while True:
            filename = textinput("Export the Polygons", "Please type in your desired textfile name without the extension (.txt)\ne.g: testfile")
            try:
                outfile = open(filename+".txt", "w")
                break
            except FileNotFoundError:
                popup = textinput("Textfile Not Found Error", "File Not Found Error!\n\nInput should exclude the file extension.\n\nTry again, please.")

        for polygon in globalPoly:
            vertices = polygon['coors']
            storedVertices = ""
            for i in range(len(vertices)):
                if i != len(vertices)-1:
                    temp = str(vertices[i][0]) + "," + str(vertices[i][1])+"; "
                else:
                    temp = str(vertices[i][0]) + "," + str(vertices[i][1])
                storedVertices += temp
            print(f"{polygon['outlinecolor']}; {polygon['fillcolor']}; {storedVertices} ", file = outfile)
    outfile.close()

def modifypoints(vertices):
    return

def moveButton():
    index, vertices, fillcolor, outlinecolor, selectedPolygon = polygonSelection("Translation","Move")
    #Modify the vertices
    x_distance = numinput("Translation", "How far the x-axis distance you want to translate?\nPositive number translate to positive x-direction.")
    y_distance = numinput("Translation", "How far the y-axis distance you want to translate?\nPositive number translate to positive y-direction.")
    newVertices = []
    for i in range(len(vertices)):
        newx = vertices[i][0] + x_distance
        newy = vertices[i][1] + y_distance
        newVertices.append([newx,newy])
    
    newPolygon = {"outlinecolor": outlinecolor, "fillcolor": fillcolor,"coors": (newVertices)}
    #Change the globalPoly
    validCheck(newPolygon, index, moveButton, selectedPolygon)

def scaleButton():
    index, vertices, fillcolor, outlinecolor,  selectedPolygon = polygonSelection("Scaling","Scale")
    newVertices = []
    #Scaling factor
    factor = float(numinput("Polygon Scaling", "Input the Scaling Factor you want.\ne.g = 0.5 or 1.2"))
    #centroid
    center = centroid(vertices)
    #Modify Vertices
    for i in range(len(vertices)):
        x_dist = center[0] - vertices[i][0]
        y_dist = center[1] - vertices[i][1]
        newx = center[0] - x_dist*factor
        newy = center[1] - y_dist*factor
        newVertices.append([newx,newy])
    
    #Change the globalPoly:
    newPolygon = {"outlinecolor": outlinecolor, "fillcolor": fillcolor,"coors": (newVertices)}
    validCheck(newPolygon, index, scaleButton, selectedPolygon)

def rotateButton():
    index, vertices, fillcolor, outlinecolor,  selectedPolygon = polygonSelection("Rotation","Rotate")
    newVertices = []
    #degree
    degree = float(numinput("Polygon Rotation", "Input the angle (in degree) you want.\ne.g = 90 / 180 / -30"))
    rad = math.radians(degree)
    askRotationCenter = textinput("the Center of Rotation", "Input the center of rotation.\ne.g:\n- 'centroid' for the center of polygon\n- 'x1,y1' for any specific center of rotation")
    
    if askRotationCenter == "centroid":
        rotationCenter = centroid(vertices)
    else:
        if "," in askRotationCenter:
            templst = askRotationCenter.split(",")
            rotationCenter = (int(templst[0]), int(templst[1]))
        else:
            scr.onclick(rotateButton)
    
    for i in range(len(vertices)):
        newx = math.cos(rad)*(vertices[i][0]-rotationCenter[0])-math.sin(rad)*(vertices[i][1]-rotationCenter[1]) + rotationCenter[0]
        newy = math.sin(rad)*(vertices[i][0]-rotationCenter[0])-math.cos(rad)*(vertices[i][1]-rotationCenter[1]) + rotationCenter[1]
        newVertices.append((newx, newy))

    #Change the globalpoly
    newPolygon = {"outlinecolor": outlinecolor, "fillcolor": fillcolor,"coors": (newVertices)}
    validCheck(newPolygon, index, rotateButton, selectedPolygon)


    return

def isInside(polygon,point):
    inside = False
    refer = centroid(polygon)
    parametric_x = []  # deltaxl*tl-deltaxp*tp=xp-xl, format(deltaxl,deltaxp,xp-xl)
    parametric_y = []  # deltayl*tl-deltayp*tp=yp-yl, format(deltayl,deltayp,yp-yl)
    tls = []
    tps = []
    while True:
        count = 0
        for i in range(len(polygon) - 2): #solve tl and tp using cramer's rule
            parametric_x.append((polygon[i+1][0]-polygon[i][0],refer[0]-point[0],refer[0]-polygon[i][0]))
            parametric_y.append((polygon[i + 1][1] - polygon[i][1], refer[1] - point[1],refer[1] - polygon[i][1]))
            det =-(polygon[i+1][0]-polygon[i][0])*(refer[1] - point[1])+((refer[0]-point[0])*(polygon[i + 1][1] - polygon[i][1]))
            det_tl =-(refer[0]-polygon[i][0])*(refer[1] - point[1])+((refer[1] - polygon[i][1])*(polygon[i + 1][1] - polygon[i][1]))
            det_tp =-(polygon[i+1][0]-polygon[i][0])*(refer[1] - polygon[i][1])+((polygon[i + 1][1] - polygon[i][1])*(refer[0]-polygon[i][0]))
            try: #parallel
                tls.append(det_tl/det)
            except ZeroDivisionError:
                tls.append(-99999999999) #impossible value
            try: #parallel
                tps.append(det_tp/det)
            except ZeroDivisionError:
                tps.append(-99999999999) #impossible value
        for tl in tls:
            if 0<tl<1:
                count += 1
            elif tl == 0 or tl == 1:
                refer[0] +=1
                refer[1] +=1
                continue
        if count%2 == 1:
            inside = True
        if point[0] < -100 or point [0] > 300 or point[1]<-100 or point[1]>300:
            inside = False
        break
    return inside



def testButton(x,y):
    global globalPoly
    point = [x,y]
    insideStatus = False
    scr.tracer(None)
    if -500 < x < 500 and -370 < y < 370 :
        testOutput.clear()
        boolList = []
        for poly in globalPoly:
            insideCheck = isInside(poly["coors"], point)
            boolList.append(insideCheck)
            
        if False in boolList:
            testOutput.write(f"Point {x,y} is outside the polygon)", align = "center", font = ("ds-digital", 18, "normal"))
        else:
            testOutput.write(f"Point {x,y} is inside the polygon)", align = "center", font = ("ds-digital", 18, "normal"))
    
    elif -580 < x < -510 and -30 < y < 10:
        textinput("Done Testing", "You successfully exit the point testing menu.\n\n[Click Enter to Continue]")
        testOutput.clear()
        scr.onclick(menuClick)
    else:
        textinput("Invalid Points", "Point test should not be outside of the drawing area\nClick Test Button to exit the point testing.")

    scr.update()

def duplicateButton():
    index, vertices, fillcolor, outlinecolor,  selectedPolygon = polygonSelection("Duplication","Duplicate")
    newVertices = []
    for i in range(len(vertices)):
        newx = vertices[i][0] + 30
        newy = vertices[i][1] + -30
        newVertices.append([newx,newy])
    newPolygon = {"outlinecolor": outlinecolor, "fillcolor": fillcolor,"coors": (newVertices)}
    validCheck(newPolygon, index, duplicateButton, selectedPolygon, True)

def deleteButton():
    global globalPoly, editDrawing, notDrawing, editable
    scr.tracer(None)
    choose = textinput("Delete Polygons", "Which polygon you want to delete?\n- e.g: 1\n- 'all' to clear canvas\n- type 'cancel' to cancel")
    if choose == "all":
        globalPoly.clear()
        naf.clear()
        notDrawing = True
        editable = False
        terminalWindow()
        scr.onclick(menuClick)
    else:
        try:
            num = int(choose)
            if num > len(globalPoly):
                popup = textinput("Invalid Input", "Out of polygon number.\nHit enter to continue.")
                if popup == "":
                    scr.onclick(menuClick)
            globalPoly.pop(num-1)
            displayPoly()
            terminalWindow()
        except:
            scr.onclick(menuClick)
    scr.update()


def menuClick(x,y):
    global notDrawing, currentlyDrawing, editable, polygonCreated
    scr.tracer(0)
    if notDrawing:
        if -580 < x < -510  and 330 < y < 370: #Create 
            notDrawing = False
            editable = False
            polygonCreated = False
            currentlyDrawing = True
            controlMenu()
            chooseInputMethodInvalid = False
            textDialog = textinput("Choose Input Method", "Mouse    : [M] or just hit enter\nKeyboard : [K]")
            while chooseInputMethodInvalid == False:
                if textDialog in "Mm" or textDialog == "":
                    colorizePoly()
                    chooseInputMethodInvalid = True
                    scr.onclick(createByMouse)
                elif textDialog in "Kk":
                    colorizePoly()
                    chooseInputMethodInvalid = True
                    createByKeypress()
                else:
                    textDialog = textinput("Choose Input Method", "Invalid Input!!\n\nMouse    : [M] or just hit enter\nKeyboard : [K]")
            
        elif -580 < x < -510 and 270 <  y < 310:
            importButton()


    if editable and notDrawing :
        if -580 < x < -510 and 150 < y < 190 :
            moveButton()
        elif -580 < x < -510 and 90 < y < 130 :
            scaleButton()
        elif -580 < x < -510 and 30 < y < 70:
            rotateButton()
        elif -580 < x < -510 and -30 < y < 10:
            textinput("Point Testing", "Click any points inside drawing area to check whether it is inside a polygon or not.\n\nClick Enter to Proceed.")
            textinput("Warning", "Please Click the Test Button Again to Exit the Point Testing")
            scr.onclick(testButton)
        elif -580 < x < -510 and -90 < y < -50:
            duplicateButton()
        elif -580 < x < -510 and -210 <  y < -170:
            deleteButton()
        elif -580 < x < -510 and -150 < y < -110:
            controlMenu()
            saveButton()
        elif -580 < x < -510 and -270 < y < -230:
            exportButton()
    scr.update()
        
#Rewrite points
#def redrawPoly():
    
#Main Function:
layoutFunc()
scr.listen()
scr.onclick(menuClick)
scr.mainloop()