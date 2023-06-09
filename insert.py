import snowflake.connector

# Set up a connection to Snowflake
conn = snowflake.connector.connect(
  user='<username>',
  password='<pwd>',
  account='<accountdetails>',
  warehouse='COMPUTE_WH',
  database='SAMPLEPY',
  schema='PUBLIC'
)

# Define the SQL statement to create a new table
sql = """
insert into my_table values (32,'MEENA',29)
"""

# Execute the SQL statement to create the table
cur = conn.cursor()
cur.execute(sql)

# Close the cursor and connection
cur.close()
conn.close()

print("Row Inserted")
