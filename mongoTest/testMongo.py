import pymongo
from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId
from datetime import datetime
Mongo_URI = "mongodb://localhost:27017"
##if you have a authsource, the structure is: mongodb://user:pass@host:port/?authSource=databaseName&authMechanism=SCRAM-SHA-1

with MongoClient(Mongo_URI) as client:
    localDB = client.local 
    ##get a list of all  database collections
    namescollection = localDB.list_collection_names()
    print(namescollection)
    ##select a collection for work
    mockCollection = localDB.mock
    ##use mongo project, we choose only the elements that we need in the project with the value 1
    print("Use of project:")
    pipeline = [
        {"$match":{
            "gender":{"$eq":"Bigender"}
        }},
        {"$project":{
            'id':1,'first_name':1,'last_name':1,'gender':1,'email':1
        }}

    ]
    mockProjectExample = mockCollection.aggregate(pipeline)
    for mock in mockProjectExample:
        print(mock)
    ##count the total of documents of a collection
    print("Use of count:")
    totalDocuments = mockCollection.count_documents({})
    print(totalDocuments)
    print("use of count with filter:")
    totalDocumentsFilter = mockCollection.count_documents({"gender":"Non-binary"})
    print(totalDocumentsFilter)
    print("use of Find:")
    documentTest = mockCollection.find_one({'email':'awallbanks8e@theatlantic.com'})
    print(documentTest)
    ##From the pymongo Docs:When the filter matches, by default find_one_and_update() returns the original version of the document 
    #before the update was applied. To return the updated (or inserted in the case of upsert) version of the document instead, use the return_document option.
    print("use of find and update:")
    documentTestUp = mockCollection.find_one_and_update({'email':'handreassenak@istockphoto.com'},
    {"$set":{'first_name':'Humberto'}},return_document= ReturnDocument.AFTER)
    print(documentTestUp)
    print("use of update many:")
    now = datetime.now()
    resultUpdate = mockCollection.update_many({},{"$set":{
       'ip_address':'127.0.0.0'
    }})
    print("total documents updated: "+ str(resultUpdate.modified_count))






