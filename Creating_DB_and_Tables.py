# Creating Tables with SQLAlchemy
# ---------------------------------------------------------------

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean
# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)
# Use the metadata to create the table
metadata.create_all(engine)
# Print table details
print(repr(data))

# ---------------------------------------------------------------
# Constraints and Data Defaults
# ---------------------------------------------------------------

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean
# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)
# Use the metadata to create the table
metadata.create_all(engine)
# Print the table details
print(repr(metadata.tables['data']))

# ---------------------------------------------------------------
# Inserting a single row with an insert() statement
# ---------------------------------------------------------------

# Import insert and select from sqlalchemy
from sqlalchemy import insert, select
# Build an insert statement to insert a record into the data table: stmt
stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)
# Execute the statement via the connection: results
results = connection.execute(stmt)
# Print result rowcount
print(results.rowcount)
# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == 'Anna')
# Print the result of executing the query.
print(connection.execute(stmt).first())

# ---------------------------------------------------------------
# Inserting Multiple Records at Once
# ---------------------------------------------------------------

# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False}
]
# Build an insert statement for the data table: stmt
stmt = insert(data)
# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)
# Print rowcount
print(results.rowcount)

# ---------------------------------------------------------------
# Loading a CSV into a Table
# ---------------------------------------------------------------

# Create a insert statement for census: stmt
stmt = insert(census)
# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0
# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    #create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    values_list.append(data)
    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []
# Print total rowcount
print(total_rowcount)

# ---------------------------------------------------------------
#
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#
# ---------------------------------------------------------------
