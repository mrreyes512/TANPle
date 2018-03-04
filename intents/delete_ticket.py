
import app
import json

# Conversation:
# I've got ticket 4
# bot: Great thank you for helping: <post_summary> (could be handeled in a query_ticket function)
# bot: Please respond: yes, remove 4


def delete_data(req):
    ticket_num = parse_data(req)

    try:
        row = app.LineDB.query.get(ticket_num)
        # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg
        app.db.session.delete(row)
        app.db.session.commit()

        row_info = "Successfully removed Ticket ID : " + str(ticket_num)

    except AttributeError:
        app.db.session.rollback()
        row_info = "Not able to delete ticket ID : " + str(ticket_num)

    except:
        # FIXME: add more specific except block
        # sqlalchemy.exc.DataError: (psycopg2.DataError) invalid input syntax for integer: "remove "
        app.db.session.rollback()
        print("There may be a bad WHERE clause: " + str(ticket_num))

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

    print(delete_data(req))
