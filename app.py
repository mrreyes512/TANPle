
import json
import os
import psycopg2

import intents.query_line

from urllib import parse

from flask import Flask
from flask import request
from flask import make_response
from flask.ext.sqlalchemy import SQLAlchemy

# Flask app should start in global layout
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Linedb(db.Model):

    __tablename__ = "mvp_table"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(), nullable=False)
    issue_type = db.Column(db.Text(), nullable=False)
    callback_method = db.Column(db.Text(), nullable=False)
    callback_details = db.Column(db.Text())
    # TODO come back to make these work. Focus on MVP for v1
    # last_name = db.Column(db.Text())
    # tech_id = db.Column(db.Text())
    # issue_details = db.Column(db.Text())
    # que_notes = db.Column(db.Text())

    def __init__(self, first_name, issue_type, callback_method, callback_details):
        self.first_name = first_name
        self.issue_type = issue_type
        self.callback_method = callback_method
        self.callback_details = callback_details

# customer = Linedb('Mark', 'cpe issues', 'phone', '512 585 5555')
# db.session.add(customer)
# db.session.commit()


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = route_action(req)

    json_convert = json.dumps(res)

    r = make_response(json_convert)
    r.headers['Content-Type'] = 'application/json'
    return r


def db_connection(db_query):
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ["DATABASE_URL"])
    # DATABASE_URL set in : heroku config

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    cur = conn.cursor()
    cur.execute(db_query)

    query_results = cur.fetchall()

    return query_results


def route_action(req):
    if req.get("result").get("action") == "queryLine":
        res = process_query_line()
        return res
    elif req.get("result").get("action") == "createTicket":
        res = process_create_ticket(req)
        return res
    elif req.get("result").get("action") == "otherAction":
        # res = process_other_action(req)
        # return res
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
    print('this is create ticket')
    pass


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
