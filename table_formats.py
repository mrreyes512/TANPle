# TODO: This file can probably be deleted now.
import texttable
import prettytable

from app import db_connection
from intents.query_line import get_data


def texttable_format(result):
    tab = texttable.Texttable()
    headings = ['Ticket ID', 'First Name', 'Issue Type']
    tab.header(headings)
    tab.set_deco(texttable.Texttable.HEADER | texttable.Texttable.VLINES)
    # tab.set_deco(texttable.Texttable.HEADER)
    tab.set_chars(['-', ':', '+', '-'])
    tab.set_cols_align(['r', 'c', 'l'])

    for row in result:
        tab.add_row(row)

    table = tab.draw()
    print('# Texttable Format')
    print(table)
    print('')

    return table


if __name__ == '__main__':
    result = get_data()
    texttable_format(result)

