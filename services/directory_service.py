from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Kiwanis


def list_directory():
    collection = db.Directory
    return collection.find()


def add_member(name, image, phone, role, email):
    collection = db.Directory
    member = {
        "Name": name,
        "Image": image,
        "Phone": phone,
        "Role": role,
        "Email": email
    }
    message = {}
    code = 0
    try:
        collection.insert_one(member)
        message = {
            "Status": "Ok"
        }
        code = 1
    except Exception as e:
        message = {
            "Status": "An Error Occurred: " + str(e)
        }
        code = 2

    return code, message
