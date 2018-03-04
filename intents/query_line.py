
import app
import texttable


def get_data():
    query = app.LineDB.query.all()
    # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg

    result = []
    for row in query:
        ticket_id = row.id
        first_name = row.first_name
        issue_type = row.issue_type
        callback_method = row.callback_method
        callback_details = row.callback_details

        result.append((ticket_id, first_name, issue_type, callback_method, callback_details))

    # print(result)
    pretty_result = format_records(result)
    return pretty_result


def format_records(result):
    tab = texttable.Texttable()
    headings = ['Ticket ID', 'Name', 'Issue', 'Callback Method', 'Details']

    # Table customizations
    tab.header(headings)
    # tab.set_deco(texttable.Texttable.HEADER | texttable.Texttable.VLINES)
    tab.set_deco(texttable.Texttable.VLINES)
    tab.set_chars(['-', ':', '+', '-'])
    tab.set_cols_align(['r', 'r', 'l', 'l', 'l'])

    for row in result:
        tab.add_row(row)

    table = tab.draw()
    # print('# Texttable Format')
    # print(table)
    # print('')

    return table

if __name__ == '__main__':
    print(get_data())
