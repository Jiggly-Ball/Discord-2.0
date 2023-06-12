from pymongo import MongoClient
from secret import secret_data

#import dns
#dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
#dns.resolver.default_resolver.nameservers=['8.8.8.8']

client = MongoClient(secret_data["token"])
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