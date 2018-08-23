# IMPORTANT: In MongoDB, a database is not created until it gets content!

import pymongo
from pymongo.errors import ConnectionFailure

#Connect MongoClient
try:
	myclient = pymongo.MongoClient('mongodb://localhost:27017/')
except ConnectionFailure:
	print("Server not available")

#create new DB if it does not exist
try:
	mydb = myclient['mydatabase']
except ValueError:
	print("The database exists.")

#create new collection if it does not exist
try:
	mycol = mydb["customers"]
except ValueError:
	print("The collection exists.")

######################################################################################################

#Insert a record in the "customers" collection
#Use: insert_one
# mydict = { "_id": 1, "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# print(x.inserted_id)


#Insert multiple documents into a collection
# Use: insert_many()
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
try:
	x = mycol.insert_many(mylist)
	#print list of the _id values of the inserted documents:
	print(x.inserted_ids)
except:
	# print("Duplicate data")
	pass

######################################################################################################

#Find one
x = mycol.find_one()
print(x)
print("-"*80)

#Find ALL
for x in mycol.find():
	print(x)
print("-"*80)

#Return some fields
#Return only the names and addresses, not the _ids:
#NOTE: You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
	print(x)
print("-"*80)

######################################################################################################

# Filter the Result
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
print("-"*80)

#Advanced query
# Find documents where the address starts with the letter "S" or higher:
# use the greater than modifier: {"$gt": "S"}
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
print("-"*80)

# Using regular expressions as a modifier
# Find only documnets where "address" field starts with letter "S"
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
print("-"*80)

######################################################################################################

#Sort the Result
# Use the sort() method to sort the result in ascending or descending order.
# Use the value -1 as the second parameter to sort descending.
mydoc = mycol.find().sort("name")
# mydoc = mycol.find().sort("name", -1)
for x in mydoc:
	print(x)
print("-"*80)

######################################################################################################

# # DELETE DOCUMENT
# # To delete one document, we use the delete_one() method
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)

# #To delete more than one document, use the delete_many() method
# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")

# # Delete ALL Documents in a Collection
# x = mycol.delete_many({})
# print(x.deleted_count, "documents deleted")

# # Delete Collection
# mycol.drop()
# # The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.

######################################################################################################

# UPDATE COLLECTION

# Update a record using update_one() method

myquery = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, new_values)

#print collection after update
for x in mycol.find():
	print(x)
print("-"*80)

# Update many documents

myquery = {"address": {"$regex": "^S"}}
new_values = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, new_values)
print(x.modified_count, "documents updated")
print("-"*80)

######################################################################################################

# LIMIT RESULT
# Using limit() method to limit the result
my_result = mycol.find().limit(5)
for x in my_result:
	print(x)
print("-"*80)


# Disconnect
myclient.close()