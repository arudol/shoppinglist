"""Simple script to completely wipe the database"""
from pymongo import MongoClient  
import os

client = MongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017/"))

# connect to database "athome" from the client
athome = client.athome
# from athome database, access shopping collection
shoppinglist = athome.shopping

shoppinglist.delete_many({})