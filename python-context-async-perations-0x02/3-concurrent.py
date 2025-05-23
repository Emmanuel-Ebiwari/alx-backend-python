import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute('SELECT * FROM users')
        rows = await cursor.fetchall()
        await cursor.close()
        return rows

async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute('SELECT * FROM users WHERE age > ?', (40,))
        rows = await cursor.fetchall()
        await cursor.close()
        return rows

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

asyncio.run(fetch_concurrently())