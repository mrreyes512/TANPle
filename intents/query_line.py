
import texttable

import app
# FIXME: @Graham: how do i import a var to make this PEP8?
import heroku_db_creds


def get_data():
    db_query = "SELECT ticket_id, first_name, issue_type FROM public.example_table"
    result = app.db_connection(db_query)
    # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg
    return result

    # pretty_result = format_records(result)
    # return pretty_result


def format_records(result):
    tab = texttable.Texttable()
    headings = ['Ticket ID', 'First Name', 'Issue Type']
    tab.header(headings)

    for row in result:
        tab.add_row(row)

    table = tab.draw()
    print(table)

    return table

if __name__ == '__main__':
    get_data()
