import aiosqlite
import asyncio
import functools

# DB_NAME = 'users.db'
async def async_fetch_users(conn):
    cursor = await conn.execute('SELECT * FROM users')
    rows = await cursor.fetchall()
    await cursor.close()
    return rows
   
async def async_fetch_older_users(conn):
    cursor = await conn.execute('SELECT * FROM users WHERE age > ?', (40,))
    rows = await cursor.fetchall()
    await cursor.close()
    return rows

async def fetch_concurrently():
    async with aiosqlite.connect('users.db') as conn:
        await asyncio.gather(
            async_fetch_users(conn),
            async_fetch_older_users(conn)
        )

asyncio.run(fetch_concurrently())


    

    
