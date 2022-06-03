#Rock-paper-scissors game

go=["scissors", "rock", "paper"]
po= ["R", "S", "P"]
print("\n\n ARE YOU READY TO PLAY SOME ROCK PAPER SCISSORS")

while True:
  import random
  cpu= random.choice(go)
  player= input(str("enter R or P or S "))
  if cpu== player:
    print(" it's a tie computer also chose ", cpu)
    continue
  if cpu== "scissors" and player== "R":
    print(" you win computer chose", cpu)
  elif cpu== "paper" and player == "R":
    print("you lose computer", cpu)
  elif cpu== "paper" and player== "S":
    print("you win computer chose", cpu)
  elif cpu== "rock" and player == "S":
    print("you lose computer chose",cpu)
  elif cpu== "rock" and player== "P":
      print("you win computer chose",cpu)
  elif cpu== "scissors" and player== "P":
      print("you lose computer chose",cpu)
  elif player not in po:
     print("invalid input")
     continue
  if cpu != player:
   x=  input("play again? ")
   if x =="yes" or "Yes":
     continue
   else:
      break
