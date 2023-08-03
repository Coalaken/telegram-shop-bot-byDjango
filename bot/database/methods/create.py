import aiosqlite

from bot.misc.utils import SQLITE_FILE


async def create_product(data):
    async with aiosqlite.connect(SQLITE_FILE) as db:
        db.row_factory = aiosqlite.Row
        await db.execute('INSERT INTO shop_item () values', ())
    