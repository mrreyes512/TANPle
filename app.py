
import json

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

    # res = processRequest(req)
    #
    # # res = json.dumps(res, indent=4)
    # # print(res)
    # # Converting res back into json output
    # json_convert = json.dumps(res)
    #
    # r = make_response(json_convert)
    # r.headers['Content-Type'] = 'application/json'
    # return r
