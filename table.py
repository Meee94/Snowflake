import snowflake.connector

# Set up a connection to Snowflake
conn = snowflake.connector.connect(
  user='<username>',
  password='<pwd>',
  account='<account detail url>',
  warehouse='COMPUTE_WH',
  database='SAMPLEPY',
  schema='PUBLIC'
)

# Define the SQL statement to create a new table
sql = """
CREATE TABLE my_table (
  id INT,
  name VARCHAR(50),
  age INT
)
"""

# Execute the SQL statement to create the table
cur = conn.cursor()
cur.execute(sql)

# Close the cursor and connection
cur.close()
conn.close()

print("Table created successfully!")
