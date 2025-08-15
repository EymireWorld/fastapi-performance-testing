import asyncio
import random
from string import ascii_letters

from sqlalchemy import insert

from app.database import engine, get_session
from app.models import Base, ItemModel


async def main():
    word_length = 10

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    print('Tables created!')

    async for session in get_session():
        for _ in range(100_000):
            stmt = insert(ItemModel).values(
                {
                    'name': ''.join(random.choice(ascii_letters) for _ in range(word_length)),
                    'value': random.randint(100, 10_000) / 100,
                    'quantity': random.randint(0, 100),
                }
            )
            await session.execute(stmt)

        await session.commit()

    print('Data generated!')


if __name__ == '__main__':
    asyncio.run(main())
