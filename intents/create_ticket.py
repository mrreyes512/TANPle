
import app
import json


def post_data(req):
    first_name, issue_type, callback_method, callback_details = parse_data(req)
    customer = app.LineDB(first_name, issue_type, callback_method, callback_details)

    try:
        app.db.session.add(customer)
        app.db.session.flush()
        app.db.session.commit()
        # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg

        ticket_id = customer.id
        post_summary = "Ticket ID : {}\n" \
                       " Given Name : {}\n" \
                       " Issue Summary : {}\n" \
                       " Callback Method : {}\n" \
                       " Callback Details : {}"\
            .format(
                ticket_id,
                first_name,
                issue_type,
                callback_method,
                callback_details
            )

    except:
        # FIXME: more specific except block
        # 2018-03-04T08:10:08.573296+00:00 app[web.1]: - sqlalchemy.exc.InternalError:
        # (psycopg2.InternalError) current transaction is aborted, commands ignored until end of transaction block
        post_summary = "There was an error creating your ticket"
        app.db.session.rollback()

    # print(post_summary)
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
    req = json.load(open('req.json'))

    print(post_data(req))
