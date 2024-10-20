import sqlite3
from datetime import datetime

# Configure FILE_PATH and\to match your budget location and filename.
# File paths can be relative.

FILE_PATH = 'C:\\Users\\username\\buckets.buckets'

CURRENCY_SYMBOL = 'USD'

# Configure OUTPUT_FILEPATH_START to match your desired output location and filename
# some numbers and .beancunt will be added to the end of the output filename upon running the script.
OUTPUT_FILEPATH_START = 'C:\\Users\\username\\Desktop\\myHKbuckets'



#lambda functions
format_date = lambda date: datetime.fromisoformat(date).strftime("%Y-%m-%d")

def get_table_data_dict(table_name):
    cur.execute('SELECT * from ' + table_name)
    headings = [d[0] for d in cur.description]
    rows = cur.fetchall()
    _data = [{headings[i]:cell for i, cell in enumerate(row)} for row in rows]
    return _data
    
def get_id_to_name_dictionary():
    cur.execute('SELECT id, name from account')
    rows = cur.fetchall()
    rows = {cell[0]:cell[1] for cell in rows}
    return rows


if __name__ == '__main__':
    conn = sqlite3.connect(FILE_PATH)
    cur = conn.cursor()

    #account_to_id dictionary
    account_id_to_name = get_id_to_name_dictionary()

    transactions = get_table_data_dict('account_transaction')

    output_lines = []
    for t in transactions:
        formatted_date = format_date(t['created'])
        _account = account_id_to_name[t['account_id']]
        _amount = f'{t['amount']/100:.2f}'
        output_lines.append(f'{formatted_date} * "{_account}" "{t['memo']}"\n'
              f'    Assets:{_account:32}  {_amount} {CURRENCY_SYMBOL}\n    \n\n')
        
    #write to file
    now = datetime.now()
    year, month, day, hour, minute, second = now.year, now.month, now.day, now.hour, now.minute, now.second
    output_filename = f'{OUTPUT_FILEPATH_START}{year}{month}{day}{hour}{minute}{second}.beancount'
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(''.join(output_lines))

    print(f"Successfully written to {output_filename}")