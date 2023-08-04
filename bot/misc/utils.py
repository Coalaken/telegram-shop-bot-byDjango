from colorama import Fore

ADMIN_ID = 1917113649

CATS_URL = 'http://127.0.0.1:8000/api/v1/shop/cats/'
ITEMS_URL = 'http://127.0.0.1:8000/api/v1/shop/items/'
SQLITE_FILE = 'bot/../db.sqlite3'


STARTUP_MESSAGE = [
    ['░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗', Fore.RED],
    ['██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝', Fore.BLUE],
    ['╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░', Fore.YELLOW],
    ['░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗', Fore.MAGENTA],
    ['██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝', Fore.GREEN],
    ['╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░', Fore.RED],
]


CATEGORY_MESSAGE =  '''All right!
In our store we have the following categories
                     ╱|、
                    (˚ˎ 。7  
                     |、˜〵          
                     じしˍ,)ノ'''


async def print_success_message():
    print('\n' * 9)
    for line in STARTUP_MESSAGE:
       
        print(line[1] + line[0])
    print(Fore.RESET + '\n' * 5)
    
    
GREETING = """
Hello! My name is Miku Vendor
Welcome to Miku Store!
    Please use keyboard for do something!
"""