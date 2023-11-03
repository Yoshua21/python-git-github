#Juego de piedra papel o tijera 
import random

option_pc_a=('piedra','papel','tijeras')
#i=random.randint(0,2) #numero random entre 0 y 2
option_pc=random.choice(option_pc_a)

rounds=1
w_usuario=0
w_pc=0

while True:
  print('')
  print('*'*14)
  print('**Round: ',rounds,'**')
  print('*'*14)    
  print('*wins usuario: ',w_usuario)
  print('*wins pc: ',w_pc)
  print('')
  print("¿PIEDRA PAPEL O TIJERAS? ")
  option_user=input("=>")
  option_user=option_user.lower()
  print("")
  print("PC:   ",option_pc)
  print("USER:  ",option_user)
  print("")
  
  
  if option_pc == option_user:
    print("EMPATE!")
  elif option_pc=='piedra':
    if option_user=='papel':
      print("Papel le gana a piedra")
      print("Usuario gana")
      w_usuario+=1
    elif option_user=='tijeras':
      print("Piedra le gana a tijeras")
      print("PC gana")
      w_pc+=1
    else:
      print("no seas pendejo ")
  elif option_pc=="papel":
    if option_user=='piedra':
      print("Papel le gana a piedra")
      print("PC gana")
      w_pc+=1
    elif option_user=='tijeras':
      print("Tijeras le gana a papel")
      print("Usuario gana")
      w_usuario+=1
      
    else:
      print("no seas pendejo!!")    
  
  elif option_pc=='tijeras':
    if option_user=='papel':
      print("Tijeras le gana a papel")
      print("PC gana")
      w_pc+=1
    elif option_user=='piedra':
      print("Piedra le gana a tijeras")
      print("Usuario gana")
      w_usuario+=1
    else:
      print("no seas pendejo!!")

  if w_usuario==2:
    print('FIN DE LA PARTIDA # USUARIO GANA!!')
    break
  if w_pc==2:
    print('FIN DE LA PARTIDA # LA PC GANA!!')
    break
  rounds+=1
