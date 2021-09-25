from flask import *
from flask_restful import Api, Resource
import cards


app = Flask(__name__)
api = Api(app)

@app.route("/", methods = ['POST'])
def trelloticket():
    data = request.get_json()
    type = data["type"]
    if type == "issue":
        ticket = cards.Issue(data["title"],data["description"])

    elif type == "bug":
        ticket = cards.Bug(data["description"])

    elif type == "task":
        ticket = cards.Task(data["title"],data["category"])
    else:
         return Response("Bad request", status=400,)    
        
    ticket.create_trello_card()

    return jsonify({'result': 'Success!'})


if __name__ == "__main__":
    app.run(host = "localhost", port = 3000, debug=True)
    

