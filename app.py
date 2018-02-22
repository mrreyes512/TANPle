
import json
import os

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


def route_action(req):
    if req.get("result").get("action") == "queryLine":
        print("this is queryLine")
        res = makeWebhookResult(data)
        return res


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
