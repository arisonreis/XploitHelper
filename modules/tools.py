from colorama import Fore
from utils import clearScreen


# Tools Module
def ToolsModule():
    ReturnIcon = Fore.YELLOW + "Return  \x1b[1D←"
    clearScreen.clearScreen()
    ToolsSelected = input(
        """
    Select a type of exploit\n
    Types:\n
    1. WifiScanner
    2. PortScanner
    3. 
    4. 
    5. 
    6. 
    6. %s 
    """
        % (ReturnIcon)
    )
