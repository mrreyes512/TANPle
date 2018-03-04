
import app
import json

# Conversation:
# I've got ticket 4
# bot: Great thank you for helping: <post_summary> (could be handeled in a query_ticket function)
# bot: Please respond: yes, remove 4


def get_ticket(req):
    ticket_num = parse_data(req)
    # ticket_num = 9

    try:
        row = app.LineDB.query.get(ticket_num)
        # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg

        ticket_id = row.id
        first_name = row.first_name
        issue_type = row.issue_type
        callback_method = row.callback_method
        callback_details = row.callback_details

        row_info = "Ticket ID : {}\n" \
                   " Given Name : {}\n" \
                   " Issue Summary : {}\n" \
                   " Callback Method : {}\n" \
                   " Callback Details : {}".\
            format(ticket_id, first_name, issue_type, callback_method, callback_details)

    except AttributeError:
        row_info = "Not finding a ticket ID : " + str(ticket_num)

    # print(row_info)
    return row_info


def parse_data(req):
    # Using Python list comprehension to extract fields and filter None's
    contexts = req['result']['contexts']

    ticket_list = [name['parameters'].get('ticket_id') for name in contexts
                 if name['parameters'].get('ticket_id') is not None]

    ticket_id = ticket_list[0]

    return ticket_id


if __name__ == '__main__':
    req = json.load(open('req.json'))

    print(get_ticket(req))
