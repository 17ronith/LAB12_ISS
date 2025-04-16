from motor.motor_asyncio import AsyncIOMotorClient
import os

async def init_db():
    try:
        MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        client = AsyncIOMotorClient(MONGO_URI)
        
        # Validate connection
        await client.admin.command('ping')
        
        db = client["testdb"]
        return {
            "items_collection": db["items"],  # Changed to plural for consistency
            "users_collection": db["users"],
            "client": client  # Return client so it can be closed later
        }
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

async def close_db_connection(db_dict):
    if "client" in db_dict:
        db_dict["client"].close()
