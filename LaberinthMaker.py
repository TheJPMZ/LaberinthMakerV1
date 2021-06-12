import random

Size = (7,8)
Grid, Walls, Path, CrossroadWall, Intersections, Monedas = [],[],[],[],[],[]


#Grid Construction
def GridConstruction():
    for x in range(1, Size[0] + 1):
        for y in range(1, Size[1] + 1):
            Grid.append((x,y))
            
    #Paredes arriba y abajo
    for x in range(Size[0] + 2):
        Walls.append((x, 0)) 
        Walls.append((x, Size[1] + 1)) 

    #Paredes izquierda derecha
    for x in range(Size[1] + 2):
        Walls.append((0, x))
        Walls.append((Size[0] + 1, x))

    #Paredes Ejes dentro    
    for x in range(1, int(((Size[0]+1) / 2))):
        for y in range(1, int(((Size[1]+1) / 2))):
            Walls.append((2 * x, 2 * y))
            Grid.remove((2 * x, 2 * y))
        
pruebalinea = ''
def PrintDisplay():
    global pruebalinea
    pruebalinea = ''
    for y in range(0, Size[1] + 2):         
        Line = []
        for x in range(0, Size[0] + 2):
            if (x, y) == Pos: Line.append("AA")
            elif (x, y) == Start: Line.append("SS")
            elif (x, y) in Monedas: Line.append("MM")
            elif (x, y) in Walls: Line.append("▓▓") 
            else: Line.append("░░")
        
        
        pruebalinea += (str(Line)
               .replace("'" , "")
               .replace("," , "")
               .replace(" " , "")
               .replace("[" , "")
               .replace("]" , "")
               ) + "\n"
        
    print(pruebalinea)
#         print((str(Line)
#                .replace("'" , "")
#                .replace("," , "")
#                .replace(" " , "")
#                .replace("[" , "")
#                .replace("]" , "")
#                ))

# Selecciona un lugar donde empezar
def PressStart(): #Picks a random space on the grid, and returns it as a tuple
    LocalPos = random.choice(Grid)
    Path.append(LocalPos)
    Grid.remove(LocalPos)
    return LocalPos
  
# Moves to a clean path
def Move(x,y):
    global Pos
    
    Caminos = []

    for Coords in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if Coords in Grid:
            Caminos.append(Coords)

    if not Caminos: #There is no way to go
        if Pos in Intersections:    
            Walls.append(Pos)
            Path.remove(Pos)
            Intersections.remove(Pos)

    #    print(str(Pos),"Dead End")
    #    PrintDisplay() #Si se quiere printear cada interseccion

        Pos = CrossroadWall.pop() #Se mueve a  la ultima interseccion y prueba con una pared
        Intersections.append(Pos)
        Path.append(Pos)
        Walls.remove(Pos)
    else:
        Pos = random.choice(Caminos)
        Caminos.remove(Pos)
        if Caminos: #If there is some other place to go
            for UnusedPaths in Caminos:
                Walls.append(UnusedPaths)
                Grid.remove(UnusedPaths)
                CrossroadWall.append(UnusedPaths)
        Path.append(Pos)
        Grid.remove(Pos)
        PrintDisplay() #Si se quiere printear cada paso
    return 



#Start = Pos = PressStart()

GridConstruction()
Start = Pos = PressStart()

while Grid: #Not Empty
    Move(Pos[0], Pos[1])   

Monedas = random.choices(
            Path, k = random.randint(1, Size[0])
            )

PrintDisplay() #Final

   