from colorama import Fore

CATS_URL = 'http://127.0.0.1:8000/api/v1/shop/cats/'
ITEMS_URL = 'http://127.0.0.1:8000/api/v1/shop/items/'


STARTUP_MESSAGE = [
    ['░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗', Fore.RED],
    ['██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝', Fore.BLUE],
    ['╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░', Fore.YELLOW],
    ['░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗', Fore.MAGENTA],
    ['██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝', Fore.GREEN],
    ['╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░', Fore.RED],
]


async def print_success_message():
    print('\n' * 9)
    for line in STARTUP_MESSAGE:
       
        print(line[1] + line[0])
    print(Fore.RESET + '\n' * 5)
    
    
GREETING = """
Hello! My name is Miku Saller
Welcome to Miku Store!
    Please use keyboard for do something!
"""