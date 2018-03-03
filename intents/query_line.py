
import texttable

import app
import pdb

# REVIEW: @Graham: how do i import a var to make this PEP8?
# import heroku_db_creds


def get_data():
    # pdb.set_trace()
    db_query = "SELECT * FROM public.mvp_table"
    result = app.db_connection(db_query)
    # result = app.LineDB.query.all()
    # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg

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
    table = get_data()
    print(table)
