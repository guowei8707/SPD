import pymongo

client = pymongo.MongoClient()
db = client.people_info
col = db.people

info_dict = {'name': 'guo', 'age': '23', 'sex':'male', 'salary':1}
col.insert(info_dict)

