
import json
import os
import psycopg2

import intents.query_line
import intents.query_ticket
import intents.create_ticket
import intents.delete_ticket

from urllib import parse

from flask import Flask
from flask import request
from flask import make_response
from flask.ext.sqlalchemy import SQLAlchemy

import pdb

# Flask app should start in global layout
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class LineDB(db.Model):

    __tablename__ = "mvp_table"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(), nullable=False)
    issue_type = db.Column(db.Text(), nullable=False)
    callback_method = db.Column(db.Text(), nullable=False)
    callback_details = db.Column(db.Text())
    # TODO come back to make the below work. Focus on MVP for v1
    # last_name = db.Column(db.Text())
    # tech_id = db.Column(db.Text())
    # issue_details = db.Column(db.Text())
    # que_notes = db.Column(db.Text())

    def __init__(self, first_name, issue_type, callback_method, callback_details):
        self.first_name = first_name
        self.issue_type = issue_type
        self.callback_method = callback_method
        self.callback_details = callback_details

    def __repr__(self):
        return '<id {}>'.format(self.id)


@app.route('/webhook', methods=['POST'])
def webhook():
    # pdb.set_trace()
    # assert request is not None
    req = request.get_json(silent=True, force=True)
    # req = json.loads(request.data)

    print("Request:")
    print(json.dumps(req, indent=4))

    # json_object = json.loads(req)

    res = route_action(req)

    json_convert = json.dumps(res)

    r = make_response(json_convert)
    r.headers['Content-Type'] = 'application/json'
    print("**RETURN**\n")
    print(r)
    return r


<<<<<<< HEAD
# def db_connection(db_query):
#     parse.uses_netloc.append("postgres")
#     url = parse.urlparse(os.environ["DATABASE_URL"])
#     # DATABASE_URL set in : heroku config
#
#     conn = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )
#
#     cur = conn.cursor()
#     cur.execute(db_query)
#
#     query_results = cur.fetchall()
#
#     return query_results


=======
>>>>>>> develop
def route_action(req):
    if req.get("result").get("action") == "queryLine":
        res = process_query_line()
        return res
    elif req.get("result").get("action") == "createTicket":
        res = process_create_ticket(req)
        return res
    elif req.get("result").get("action") == "queryTicket":
        res = process_query_ticket(req)
        return res
        pass
    elif req.get("result").get("action") == "deleteTicket":
        res = process_delete_ticket(req)
        return res
        pass
    else:
        speech = "I didn't understand that action(webhook response)"
        return {
                "speech": speech,
                "displayText": speech
        }


def process_query_line():
    data = intents.query_line.get_data()

    speech = "The current line looks like:\n\n"
    speech = speech + data

    print(speech)
    return {
        "speech": speech,
        "displayText": speech
    }


def process_create_ticket(req):
    post = intents.create_ticket.post_data(req)

    speech = "Added your ticket in with the below:\n\n"
    speech = speech + post

<<<<<<< HEAD
=======
    print(speech)
    return {
        "speech": speech,
        "displayText": speech
    }


def process_query_ticket(req):
    post = intents.query_ticket.get_ticket(req)

    speech = "Just to verify, you're attempting to help out:\n"
    speech = speech + post
    speech = speech + "\n\n**Please respond with: 'yes, remove <number>'"

>>>>>>> develop
    print(speech)
    return {
        "speech": speech,
        "displayText": speech
    }


<<<<<<< HEAD
def process_query_ticket(req):
    post = intents.query_ticket.get_ticket(req)

    speech = "Just to verify, you're attempting to help out:\n"
    speech = speech + post
    speech = speech + "\n\n**Please respond with: 'yes, remove <number>'"

    print(speech)
    return {
        "speech": speech,
        "displayText": speech
    }


def process_delete_ticket(req):
    post = intents.delete_ticket.delete_data(req)

=======
def process_delete_ticket(req):
    post = intents.delete_ticket.delete_data(req)

>>>>>>> develop
    speech = "Attempting to remove ticket..\n"
    speech = speech + post

    print(speech)
    return {
        "speech": speech,
        "displayText": speech
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
