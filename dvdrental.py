# Import the psycopg2 library for interacting with PostgreSQL
import psycopg2

# Database connection details
hostname = 'localhost'
database = 'DVDRental' 
username = 'postgres'
pwd = 'priyakavya' #input the password used while installing pgAdmin
port_id = 5432

#A cursor variable or cursor object in Python's database interfaces represents a control structure that enables: 
#traversal and manipulation of result sets returned by SQL queries executed against a database.

# Initialize connection and cursor variables
conn = None
cur = None

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host= hostname,
        dbname = database,
        user = username,
        password = pwd,
        port =  port_id
    )
    
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()


    #example of creating a table
    # create_script = ''' CREATE TABLE IF NOT EXISTS MANAGER_DUMMY (
    # manager_id SERIAL PRIMARY KEY,
    # first_name VARCHAR(50) NOT NULL,
    # last_name VARCHAR(50) NOT NULL,
    # email VARCHAR(100),
    # phone VARCHAR(20),
    # hire_date DATE,
    # salary DECIMAL(10, 2))'''


     #Drop the table if it exists to start fresh
    cur.execute('DROP TABLE IF EXISTS film_review')

    # Create the film_review table
    create_script = '''
    CREATE TABLE IF NOT EXISTS film_review (
        review_id SERIAL PRIMARY KEY,
        film_id INT NOT NULL,
        customer_id INT NOT NULL,
        rating INT NOT NULL,
        review_text TEXT,
        review_date DATE
    )
    '''
    cur.execute(create_script)

    #example of inserting records in the table
    # insert_script = 'INSERT INTO MANAGER_DUMMY (first_name, last_name, email, phone, hire_date, salary) VALUES(%s, %s, %s, %s, %s, %s)'
    # insert_values = [('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2024-04-21', 50000.00), ('Alice', 'Smith', 'alice.smith@example.com', '987-654-3210', '2023-11-15', 60000.00), ('Bob', 'Johnson', 'bob.johnson@example.com', '555-555-5555', '2022-08-30', 55000.00)]
    
    #your code goes in this
# Insert 5 rows into the film_review table
    insert_script = '''
    INSERT INTO film_review (film_id, customer_id, rating, review_text, review_date)
    VALUES (%s, %s, %s, %s, %s)
    '''
    insert_values = [
        (1, 1, 5, 'Excellent film, highly recommended!', '2024-04-20'),
        (2, 3, 4, 'Good movie, enjoyed it.', '2024-04-21'),
        (3, 2, 3, 'Average film, nothing special.', '2024-04-22'),
        (4, 4, 5, 'Amazing, must-watch!', '2024-04-23'),
        (5, 5, 2, 'Disappointing, not worth it.', '2024-04-24')
    ]
    
    #for multiple entries we need for loop
    for record in insert_values:
        cur.execute(insert_script, record)

    #example of fetching data from table and displaying in python
    # cur.execute('select * from MANAGER_DUMMY')
    # print(cur.fetchall())

    #your code goes in this
    cur.execute('select * from film_review')
    print("All Rows:")
    print(cur.fetchall())
    print('\n')

    # Fetch and print one row from the film_review table
    cur.execute('SELECT * FROM film_review WHERE review_id = 2')
    print("\nOne Row (Review ID = 2):")
    print(cur.fetchone())
    print('\n')

    # Fetch and print three rows from the film_review table
    cur.execute('SELECT * FROM film_review LIMIT 3')
    print("\nThree Rows (Limit 3):")
    print(cur.fetchmany(3))

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