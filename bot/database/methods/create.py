import aiosqlite

from bot.misc.utils import SQLITE_FILE


async def create_product(data) -> None:
    async with aiosqlite.connect(SQLITE_FILE) as db:
        db.row_factory = aiosqlite.Row
        command = f'''insert into shop_item () values ("{data["name"]}", "{data["slug"]}", "{data["img"]}", "{data["description"]}", "{data["price"]}'''
        await db.execute(command)
        await db.commit()


async def create_category(name: str) -> None:
    async with aiosqlite.connect(SQLITE_FILE) as db:
        db.row_factory = aiosqlite.Row        
        command = f'''insert into shop_category ("name", "slug") values ("{name.lower().strip()}", "{name.lower().strip()}")'''
        await db.execute(command)
        await db.commit()
        
            
# TO-DO write post request with creation \ 