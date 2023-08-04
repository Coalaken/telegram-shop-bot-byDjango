import ujson

from aiohttp import ClientSession



async def get_data_from_server(url: str, c_id: int=None):
    async with ClientSession() as session:
        if c_id:
            url += f'{c_id}/'
            # print(url)
        async with session.get(url) as res:
            return await res.json()
        
        
async def create_category(url: str, name: str) -> None:
    data = {
        "name": name.title().strip(),
        "slug": name.lower().strip()
    }
    async with ClientSession() as session:
        resp = await session.post(url, json=data)
        print(resp.status)