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
  
def FindSolutions(X):
  auxX = [False] * 1000;
  current = 0
  while not(auxX[978]):
    
    if not(auxX[999-current]):
      auxX[999-current] = True
      current = 0
      ReplaceAndCheck(X,auxX)
    else:
      auxX[999-current] = False
      current = current + 1
      
  return

def ReplaceAndCheck(X, auxX):
  for i in range(0,1000):
    if X[i]:
      auxX[i] = True
  if Sudoku(auxX):
    print("Valido")
    return True
  return False
  
    
