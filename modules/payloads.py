from colorama import Fore
from utils.clearScreen import clearScreen;
from utils.showLogo import showLogo;
# imports


# Payload Module
def PayloaModule():
  ReturnIcon = Fore.YELLOW + "Return  \x1b[1D←"
  clearScreen();
  showLogo();
  PayloadTypeSelected = input(
  """
  Select a type of exploit\n
  Types:
  1. Reverse Shells
  2. 
  3. 
  4. 
  5. 
  6. 
  6. %s 
  """
      % (ReturnIcon)
  )
  match PayloadTypeSelected:
     # Reverse Shells
     case "1":
         clearScreen()
         LangType = input(
  """
  Selecione A linguagem:\n
  1. Python
  2. Javascript
  3. Java
  4. PHP
  """
         )
         match LangType:
             case "1":
                 print("Python Payloads")
     case _:
         print("opção inválida")
