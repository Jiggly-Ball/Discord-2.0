import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

if token is "":
    print("Please enter your database token into the \".env\" file.")
    exit()

try:
    client = MongoClient(token)
    
except Exception:
    print(f"Error-\n\n{Exception}\n\n")

    print("Attempting to reconnect...")

    import dns
    dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers=['8.8.8.8']

    client = MongoClient(token)

dbtyp = client["chatdata"]

collections = dbtyp.list_collection_names()

if "chat" not in collections:
    dbtyp.create_collection("chat")
    chat_db = dbtyp["chat"]
    chat_db.insert_one({"chatid":"server001", "chats":[]})

chat_db = dbtyp["chat"]

print("Connected to Database")

class CHAT:
    def find_all_chats():
        obj = chat_db.find({})
        chats = [chat for chat in obj]
        return chats

    def update_chat(chat_:str, message:str):
        chat_log = CHAT.find_chat(chat_)
        chat_log["chats"].append(message)
        chat_db.update_one({"chatid":chat_},{"$set":{"chats":chat_log["chats"]}})

    def find_chat(chat:str):
        obj = chat_db.find_one({"chatid":chat})
        return obj