import multiprocessing
from multiprocessing import Process
import json
from pymongo import MongoClient, InsertOne

Mongo_URI = "mongodb://localhost:27017"
NUMBER_ROWS = 100
processes = []
##function to call in the process
def insertRows(array):
    requests = []
    for row in array:
        requests.append(InsertOne(row))
    ##from pymongo documentation: 
    #PyMongo is thread-safe and provides built-in connection pooling for threaded applications.
    #PyMongo is not fork-safe. Care must be taken when using instances of MongoClient with fork(). 
    # Specifically, instances of MongoClient must not be copied from a parent process to a child process. 
    # Instead, the parent process and each child process must create their own instances of MongoClient. 
    # Instances of MongoClient copied from the parent process have a high probability of deadlock in the 
    # child process due to the inherent incompatibilities between fork(), threads, and locks.
    with MongoClient(Mongo_URI) as client:
        localDB = client.local
        mockCollection = localDB.mock
        mockCollection.bulk_write(requests)

 #the code is under main function
if __name__ == '__main__':
    with open('MOCK_DATA.json', 'r') as openfile:
        data = json.load(openfile)
        chunks = [data[i:i + NUMBER_ROWS] for i in range(0, len(data), NUMBER_ROWS)] 

    for chunk in chunks:
        process = Process(target=insertRows, args=(chunk,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
               
