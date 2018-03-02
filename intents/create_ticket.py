
import texttable

import app

# REVIEW: @Graham: how do i import a var to make this PEP8?
# import heroku_db_creds


def post_data(json_load):
    # print(json_load)
    first_name = json_load['result']['contexts']['parameters']['given-name']
    # issue_type = json_load['result']['contexts']['parameters']['given-name']
    # callback_method = json_load['result']['contexts']['parameters']['given-name']
    # callback_details = json_load['result']['contexts']['parameters']['given-name']
    # print("in post_data")
    print("first_name:" + first_name)

    # db_query = "SELECT ticket_id, first_name, issue_type FROM public.example_table"
    # result = app.db_connection(db_query)
    # # TODO: add logging feature of result here. https://youtu.be/jxmzY9soFXg
    #
    # pretty_result = format_records(result)
    # return pretty_result


def format_records(result):
    tab = texttable.Texttable()
    headings = ['Ticket ID', 'First Name', 'Issue Type']

    # Table customizations
    tab.header(headings)
    # tab.set_deco(texttable.Texttable.HEADER | texttable.Texttable.VLINES)
    tab.set_deco(texttable.Texttable.VLINES)
    tab.set_chars(['-', ':', '+', '-'])
    tab.set_cols_align(['r', 'c', 'l'])

    for row in result:
        tab.add_row(row)

    table = tab.draw()
    # print('# Texttable Format')
    # print(table)
    # print('')

    return table

if __name__ == '__main__':
    post_data()


