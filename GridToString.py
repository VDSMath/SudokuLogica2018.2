SAVE_PATH = "Maps/"
DEFAULT_NAME = "correctInput"
LIST_SIZE = 1000

currentMap = 0

def SaveGrid(X):
  global currentMap
  fileName = SAVE_PATH + DEFAULT_NAME + str(currentMap) + ".txt"
  file = open(fileName,'w')
  txt = ""
  for i in range(0,LIST_SIZE):
    txt += str(X[i]) + "\n"
  print(txt)
  file.write(txt)
  currentMap += 1
  
    
