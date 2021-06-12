import random

size = (33,33)
pos = [0, 0]
grid = []
walls = []
path = []
Start = ()
Here = ()
lastint = []
intersections = []
monedas = []

for x in range(1,size[0]+1):
    for y in range(1,size[1]+1):
        grid.append((x,y))
        
#Paredes arriba y abajo
for x in range(size[0]+2):
    walls.append((x,0))
    walls.append((x,size[1]+1))
#Paredes izquierda derecha
for x in range(size[1]+2):
    walls.append((0,x))
    walls.append((size[0]+1,x))
#Paredes Ejes dentro    
for x in range(1,int(((size[0]+1)/2))):
    for y in range(1,int(((size[1]+1)/2))):
        walls.append((2*x,2*y))
        grid.remove((2*x,2*y))
        
        
def printa():
    for y in range(0,size[1]+2):
        line =[]
        for x in range(0,size[0]+2):
            if (x,y) == pos:
                line.append("AA")
            elif (x,y)==Start:
                line.append("SS")
            elif (x,y)in monedas:
                line.append("MM")
            elif (x,y)in walls:
                line.append("▓▓")  
            else:
                line.append("░░")
        
        print((str(line).replace("'","").replace(",","").replace(" ","").replace("[","").replace("]","")))
    



# Selecciona un lugar donde empezar
def PressStart(x,y):
#   pos[0] = random.randint(1, x)
#   pos[1] = random.randint(1, y)
    global pos, Start
    #pos = (1,1)
    pos = random.choice(grid)
    po = tuple(pos)
    path.append(po)
    grid.remove(po)
    Start = po
  
# Moves to a clean path
def Move(x,y):
    global cami, pos,lastint,intersections
    
    cami = []
    if (x+1,y) not in walls and (x+1,y) not in path:
        cami.append((x+1,y))
    if (x-1,y) not in walls and (x-1,y) not in path:
        cami.append((x-1,y))
    if (x,y+1) not in walls and (x,y+1) not in path:
        cami.append((x,y+1))
    if (x,y-1) not in walls and (x,y-1) not in path:
        cami.append((x,y-1)) 
    if cami == []:
        if pos in intersections:    
            walls.append(pos)
            try:
                intersections.remove(pos)
                path.remove(pos)
            except ValueError:
                pass
#         print(str(pos)+"Dead End")
#         printa()
        pos = lastint.pop()
        intersections.append(pos)
        path.append(pos)
        walls.remove(pos)

    else:
        pos = random.choice(cami)
        cami.remove(pos)
        if cami != []:
            for x in cami:
                walls.append(x)
                grid.remove(x)
                lastint.append(x)
#             wat = random.choice(cami)
#             walls.append(wat)
#             grid.remove(wat)
        path.append(pos)
        grid.remove(pos)
        printa()

def Verify(newpos):

    pass

def regreso():
    
    pass
   





PressStart(size[0],size[1])
print(pos)
while not grid:
    Move(pos[0],pos[1])
    
monedas = random.choices(path,k=random.randint(1,size[0]))

printa()

