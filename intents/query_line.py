
import texttable

import app
import heroku_db_creds


def get_data():
    db_query = "SELECT ticket_id, first_name, issue_type FROM public.example_table"
    result = app.db_connection(db_query)

    formatted = format_records(result)

    # package up formatted response in json

    # response = json.loads(formatted)
    return formatted


def format_records(result):
    tab = texttable.Texttable()
    headings = ['Ticket ID', 'First Name', 'Issue Type']
    tab.header(headings)

    for row in result:
        tab.add_row(row)

    s = tab.draw()
    print(s)
    speech = "The line looks like:"
    speech = speech + s
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech
    }

if __name__ == '__main__':
    get_data()
