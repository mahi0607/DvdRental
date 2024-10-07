# Import the psycopg2 library for interacting with PostgreSQL
import psycopg2

# Database connection details
hostname = 'localhost'
database = 'DVDRental'
username = 'postgres'
pwd = 'priyakavya'  # input the password used while installing pgAdmin
port_id = 5432

# Initialize connection and cursor variables
conn = None
cur = None

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Add a new column helpful_votes to film_review table
    alter_script = '''
    ALTER TABLE film_review
    ADD COLUMN IF NOT EXISTS helpful_votes INT DEFAULT 0
    '''
    cur.execute(alter_script)
   
   # Use information_schema.columns to describe the table
    describe_query = '''
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'film_review'
    '''
    cur.execute(describe_query)
    table_description = cur.fetchall()

    # Print the description of the film_review table
    print("Description of 'film_review' table:")
    for column in table_description:
        print(column[0], "-", column[1])


    # Delete a record from the film_review table
    delete_script = '''
    DELETE FROM film_review
    WHERE review_id = %s
    '''
    review_id_to_delete = 5  # Deleting the review with review_id = 5
    cur.execute(delete_script, (review_id_to_delete,))

    # Fetch and print all rows from the film_review table after deletion
    cur.execute('SELECT * FROM film_review')
    print("\nAll Rows After Deletion:")
    print(cur.fetchall())

    # Commit the transaction
    conn.commit()

except Exception as error:
    # Print any errors that occur during execution
    print(error)

finally:
    # Close the cursor and connection objects
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
