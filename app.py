
import json
import os
import psycopg2

import intents.query_line as int_ql

from urllib import parse

from flask import Flask
from flask import request
from flask import make_response


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = route_action(req)
    #
    # # res = json.dumps(res, indent=4)
    # # print(res)
    # # Converting res back into json output
    # json_convert = json.dumps(res)
    #
    # r = make_response(json_convert)
    # r.headers['Content-Type'] = 'application/json'
    # return r
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
        int_ql.get_data()
        print("this is queryLine")
        # res = make_webhook_result(data)
        return #res


# def make_webhook_result(data):
#     pass


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
