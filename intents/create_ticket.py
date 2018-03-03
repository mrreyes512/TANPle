
import app
import json


def post_data(req):
    first_name, issue_type, callback_method, callback_details = parse_data(req)

    # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg
    customer = app.LineDB(first_name, issue_type, callback_method, callback_details)
    app.db.session.add(customer)
    app.db.session.commit()

    ticket_id = 2
    post_summary = "Ticket ID : {}\nGiven Name : {}\nIssue Summary : {}\n" \
                   "Callback Method : {}\nCallback Details : {}".format(
        ticket_id,
        first_name,
        issue_type,
        callback_method,
        callback_details
    )

    print(post_summary)

    return post_summary


def parse_data(req):

    # Using Python list comprehension to extract fields and filter None's
    contexts = req['result']['contexts']

    name_list = [name['parameters'].get('given-name') for name in contexts
                 if name['parameters'].get('given-name') is not None]

    issue_list = [issue['parameters'].get('issue_sum') for issue in contexts
                  if issue['parameters'].get('issue_sum') is not None]

    cb_method_list = [issue['parameters'].get('callback_method') for issue in contexts
                      if issue['parameters'].get('callback_method') is not None]

    cb_details_list = [issue['parameters'].get('callback_details') for issue in contexts
                       if issue['parameters'].get('callback_details') is not None]

    first_name = name_list[0]
    issue_type = issue_list[0]
    callback_method = cb_method_list[0]
    callback_details = cb_details_list[0]

    return [
        first_name,
        issue_type,
        callback_method,
        callback_details
    ]


if __name__ == '__main__':
    # json_data = open('req.json', 'r').readlines()
    req = json.load(open('req.json'))
    # print(req)
    post_data(req)


