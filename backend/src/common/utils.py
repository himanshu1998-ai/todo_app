import os
import motor.motor_asyncio


def get_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("DB_URL"))
    return client
