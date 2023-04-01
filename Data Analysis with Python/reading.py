with open('file.csv', 'r') as fp: # write automatically closes file once it leaves block
    for index, line in enumerate(fp.readlines()):
        # read first 10 lines
        if (index < 10):
            timestamp, price = line.split(',')
            print(index, line)

with open('file.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter='>') # special delimiter
    next(reader)
    for index, values in enumerate(reader):
        if not values:
            continue # skip empty lines
        fname, lname, age = values
        print(f"{fname} {lname} (age {age})")

# Parsing remote file
csv_url = "link.csv"
pd.read_csv(csv_url).head()

# first row header
df = pd.read_csv('file.csv', header=None) # ignore header

# missing value
df = pd.read_csv('file.csv', na_values=['', '?', '-']) # any found na value will be replaced by NaN

# adding column names
df = pd.read_csv('file.csv', names=['Timestamp', 'Price'])

# specify column type
df = pd.read_csv('file.csv', dtype={'Price': 'float'})

# parse date
df = pd.read_csv('file.csv', parse_dates=[0]) # 0 is position of column w/ dates

# Saving CSV
exam_df.to_csv('outFile.csv')

import sqlite3
conn = sqlite3.connect('chinook.db') # create connection to db
cur = conn.cursor() # cursor allows u to execute SQL queries in database
cur.execute('SELECT * FROM employees LIMIT 5;')
results = cur.fetchall() # stores results of query to variable
df = pd.Dataframe(results) # creates dataframe out of results

# using pandas w/ SQL
df = pd.read_sql('SELECT * FROM employees;', conn)
df = pd.read_sql_query('SELECT * from employees;', conn) # default behavior, same as reqd_sql
df = pd.read_sql_table('employees', conn) # reads entire table and parses

# writing into SQL
df.to_sql('employees2', conn) # creates new table, by default won't execute on existing table
    df.to_sql('table', conn, if_exists='appends') # append if table already exists

# close connection and cursor
cur.close()
conn.close()


# Reading HTML
from IPython.core.display import display, HTML
display(HTML(html_string))
dfs = pd.read_html(html_string) # reads all tables in string
pd.read_html(html_string, header=0)[0] # dealing with headers

# Reading excel tables
df = pd.read_excel('products.xlsx', sheet_name='Merchants', index_col='merchant_id')

# ExcelFile
excel_file = pd.ExcelFile('products.xlsx')
excel_file.sheet_names
products = excel_file.parse('Products')

# Save to excel
products.to_excel('out.xlsx')
products.to_excel('out.xlsx', startrow=1, startcol=2)
