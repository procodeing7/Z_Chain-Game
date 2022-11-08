from os import system as sys
from time import sleep as s
z = "z"
while True:
  sys('clear')
  print(z)
  z += "z"
  print(f"\n\n There are currently {len(z)} z's.")
  s(0.09)
