from aiohttp import ClientSession


async def get_data_from_server(url: str, c_id: int=None):
    async with ClientSession() as session:
        if c_id:
            url += f'{c_id}/'
        async with session.get(url) as res:
            return await res.json()
        
        
async def create_category(url: str, name: str) -> None:
    data = {
        "name": name.title().strip(),
        "slug": name.lower().strip()
    }
    async with ClientSession() as session:
        resp = await session.post(url, json=data)
        
        
async def create_item(url: str, data) -> None:
    data = {
        "name": data['name'].title().strip(),
        "slug": data['name'].lower().strip(),
        "img": data['img'],
        "description": data['description'],
        "price": data['price'],
    }
    async with ClientSession() as session:
        resp = await session.post(url, json=data)


async def delete_item(url: str, item_id: int):
    url += f'{item_id}/'
    async with ClientSession() as session:
        await session.delete(url)


async def get_user_cart(url:str, user_id: int): 
    async with ClientSession() as sessoion:
        url += f'{user_id}/' 
        resp = await sessoion.get(url)
        return await resp.json() 
    
    
async def qadd_to_cart(url: str, user_id: int, product_id: int):
    url += f'{user_id}/{product_id}/'
    async with ClientSession() as session:
        await session.post(url)


async def qdelete_from_cart(url: str, user_id: int, product_id: int):
    url += f'{user_id}/{product_id}/'
    async with ClientSession() as session:
        await session.delete(url)
        
        
async def update_item(url: str, /, item_id: int, data):
    url += f'{item_id}/'
    async with ClientSession() as session: 
        await session.put(url, json=data)
        
        





