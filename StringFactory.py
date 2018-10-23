#TRABALHO 1 - ESTUDO DIRIGIDO: SUDOKU
#GRUPO: Gabriel Raposo, Matheus Vinicius, Pedro Nascimento(116037448)
#PROFESSOR: Joao Carlos DISCIPLINA: Logica PERIODO: 2018/2

def CreateBooleanFunctions():
  #Gera um arquivo com as funções booleanas
  file = open("SudokuCheck.py","w")
  txt = "def A(X):\n  return " + PeloMenosUmDigitoTodaCasa() + "\n\n"
  txt += "def B(X):\n  return " + NoMaximoUmDigitoTodaCasa() + "\n\n"
  txt += "def C(X):\n  return " + DigitoUnicoTodaLinha() + "\n\n"
  txt += "def D(X):\n  return " + DigitoUnicoTodaColuna() + "\n\n"
  txt += "def E(X):\n  return " + DigitoUnicoTodoSubgrid() + "\n\n"
  txt += "def CheckIfValid(X):\n"
  txt += "  X = [False]*1000\n"
  txt += "  input_file = open('input.txt','r').read()\n\n"
  txt += "  for p in input_file.split():\n    X[int(p)] = True\n\n"
  txt += "  return A(X) and B(X) and C(X) and D(X) and E(X)\n\n"
  file.write(txt)
  
def PeloMenosUmDigitoEmCasa(i,j):
  expression = "("
  for k in range(1,9):
    expression += "X[" + str(i) + str(j) + str(k) + "] or " 
  expression += "X[" + str(i) + str(j) + str(9) + "]" + ")"
  return expression

def PeloMenosUmDigitoTodaCasa():
  expression = "("
  for i in range(1,10):
    for j in range(1,10):      
      expression += PeloMenosUmDigitoEmCasa(i,j)
      if not(i == 9 and j == 9):
        expression += " and "
  expression += ")"
  return expression

def NoMaximoUmDigitoEmCasa(i,j):
  expression = "("
  for d in range(1,10):
    for k in range(d+1,10):
      expression += "not(X["+str(i)+str(j)+str(d)+"] and X["+str(i)+str(j)+str(k)+"])"
      if not(d == 8 and k == 9):
        expression += " and "
  expression += ")"
  return expression

def NoMaximoUmDigitoTodaCasa():
  expression = "("
  for i in range(1,10):
    for j in range(1,10):      
      expression += NoMaximoUmDigitoEmCasa(i,j)
      if not(i == 9 and j == 9):
        expression += " and "
  expression += ")"
  return expression

def DigitoUnicoEmLinha(i,d):
  expression = "("
  for j in range (1,9):
    for k in range(j+1,10):
      expression += "not(X["+str(i)+str(j)+str(d)+"] and X["+str(i)+str(k)+str(d)+"])"
      if not(k == 9 and j == 8):
        expression += " and "
  expression += ")"
  return expression

def DigitoUnicoTodaLinha():
  expression = "("
  for i in range(1,10):
    for d in range(1,10):
      expression += DigitoUnicoEmLinha(i,d)
      if not(i == 9 and d == 9):
        expression += " and "
  expression += ")"
  return expression

def DigitoUnicoEmColuna(j,d):
  expression = "("
  for i in range (1,9):
    for k in range(i+1,10):
      expression += "not(X["+str(i)+str(j)+str(d)+"] and X["+str(k)+str(j)+str(d)+"])"
      if not(k == 9 and i == 8):
        expression += " and "
  expression += ")"
  return expression

def DigitoUnicoTodaColuna():
  expression = "("
  for j in range(1,10):
    for d in range(1,10):
      expression += DigitoUnicoEmColuna(j,d)
      if not(j == 9 and d == 9):
        expression += " and "
  expression += ")"
  return expression

def DigitoUnicoEmSubgrid(x,y):
  expression = "("
  for d in range(1,10):
    for m in range(1,9):
      for n in range(m+1,10):        
          expression += "not(X["+str((x-1)+((m-1)//3)+1)+str((y-1)+((m-1)%3)+1)+str(d)+"] and X["+str((x-1)+((n-1)//3)+1)+str((y-1)+((n-1)%3)+1)+str(d)+"])"
          if not(m == 8 and n == 9):
            expression += " and "
    if not(d == 9):
      expression += " and "
  expression += ")"
  return expression

def DigitoUnicoTodoSubgrid():
  expression = "("
  for x in range(0,3):
    for y in range(0,3):
      expression += DigitoUnicoEmSubgrid(1+3*x,1+3*y)
      if not(x == 2 and y == 2):
        expression += " and "
  expression += ")"
  return expression
    
