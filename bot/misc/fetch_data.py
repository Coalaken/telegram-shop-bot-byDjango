from aiohttp import ClientSession


async def get_data_from_server(url: str, id: int=2):
    async with ClientSession() as session:
        if id:
            url.format(id)
        async with session.get(url) as res:
            return await res.json()