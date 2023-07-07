import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sam"]
mycol = mydb["civilianvehicle2"]
def insertDB(data):
    mycol.insert_one(data)
    return
def findByID(id):
    data = mycol.find_one({'id': id})
    return data

def get_all_data():
    data = mycol.find()
    return data
