from flask import Flask
from flask import request
from flask import Response

from bson.json_util import dumps

from services import directory_service

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! Welcome to the Kiwanis API'


@app.route('/v1/directory', methods=['GET', 'POST', 'PUT'])
def directory():
    if request.method == 'GET':
        cursor = directory_service.list_directory()
        d = []
        for c in cursor:
            d.append(c)
        return Response(dumps(d), status=200, mimetype="application/json")
    elif request.method == "POST":
        member = request.get_json(silent=True)

        try:
            directory_service.add_member(member["name"], member["image"], member["phone"],
                                         member["role"], member["email"])
            msg = {
                "Status": "Record Added Successfully"
            }
            return Response(dumps(msg), status=200, mimetype="application/json")
        except Exception as E:
            msg = {
                "Error": str(E)
            }
            return Response(dumps(msg), status=500, mimetype="application/json")
    elif request.method == "PUT":
        pass

if __name__ == '__main__':
    app.debug = True
    app.run()
