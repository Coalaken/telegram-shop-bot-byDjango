from colorama import Fore


STARTUP_MESSAGE = [
    ['░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗', Fore.RED],
    ['██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝', Fore.BLUE],
    ['╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░', Fore.YELLOW],
    ['░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗', Fore.MAGENTA],
    ['██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝', Fore.GREEN],
    ['╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░', Fore.RED],
]

ADMIN_ID = 1917113649

CATS_URL = 'http://127.0.0.1:8000/api/v1/shop/cats/'
ITEMS_URL = 'http://127.0.0.1:8000/api/v1/shop/items/'
ITEM_DELETE_URL = 'http://127.0.0.1:8000/api/v1/shop/delete/items/'
SQLITE_FILE = 'bot/../db.sqlite3'
CART_URL = 'http://127.0.0.1:8000/api/v1/shop/cart/'
CART_ADD_URL = 'http://127.0.0.1:8000/api/v1/shop/cart/add/'
CART_DEL_URL = 'http://127.0.0.1:8000/api/v1/shop/cart/del/'
CATEGORY_DELETE_URL = 'http://127.0.0.1:8000/api/v1/shop/cat/delete/'
ITEM_UPDATE_URL = 'http://127.0.0.1:8000/api/v1/shop/items/item/'


CATEGORY_MESSAGE =  '''All right!
In our store we have the following categories
                     ╱|、
                    (˚ˎ 。7  
                     |、˜〵          
                     じしˍ,)ノ'''

GREETING = """
Hello! My name is Miku Vendor
Welcome to Miku Store!
    Please use keyboard for do something!
"""

async def print_success_message():
    print('\n' * 9)
    for line in STARTUP_MESSAGE:
       
        print(line[1] + line[0])
    print(Fore.RESET + '\n' * 5)
