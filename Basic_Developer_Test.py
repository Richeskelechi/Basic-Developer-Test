import psycopg2
from decouple import config

# Getting the database details from my config .env file
hostname = config('HOSTNAME')
database_name = config('DATABASE_NAME')
username = config('DB_USERNAME')
password = config('PASSWORD')
port_no = config('PORT_NO', cast=int)

conn = None
cur = None
# Using try and except to getting errros if possible connecting to the database
try:
    print('Connecting to database.......')
    conn = psycopg2.connect(
        host=hostname,
        dbname=database_name,
        user=username,
        password=password,
        port=port_no
    )
    print('Connection to database Successful.....')
    cur = conn.cursor()
    # if table exist drop it and create a new one
    cur.execute('DROP TABLE IF EXISTS shirt_color')
    create_script = '''
    CREATE TABLE IF NOT EXISTS shirt_color(id int PRIMARY KEY, color varchar(255) NOT NULL, frequency int)
    '''
    cur.execute(create_script)
    # Inserting data in the database table 
    insert_script = 'INSERT INTO shirt_color(id, color, frequency) VALUES (%s, %s, %s)'
    insert_values = [(1, "Green", 10), (2, "Yellow", 4), (3, "Brown", 6), (4, "Blue", 31), (5, "Pink", 5),
                     (6, "Orange", 10), (7, "Cream", 2), (8, "Red", 9), (9, "White", 16), (10, "Ash", 1), (11, "Black", 1)]
    for record in insert_values:
        cur.execute(insert_script, record)

    # calculating for the mean shirt
    retrieve = "Select AVG(frequency) AS average from shirt_color;"
    cur.execute(retrieve)
    rows = cur.fetchall()
    for i in rows:
        print("The mean Color Shirt is : " + str(i[0]))

    # Color of shirt worn most in the week.
    cur.execute('SELECT * FROM shirt_color ORDER BY frequency DESC')
    print('The Color of shirt worn most in the week is : ', cur.fetchone()[1])

    # median of the shirt color
    cur.execute("SELECT SUM(frequency) FROM shirt_color")
    sum_of_frequencies = cur.fetchall()[0][0]
    cur.execute("select count(*) from shirt_color")
    fixture_count = cur.fetchone()[0]
    median_value = float(sum_of_frequencies/2)
    cur.execute("SELECT * FROM shirt_color ORDER BY frequency ASC")
    all_data = cur.fetchall()
    sum = 0
    shirt_color = ''
    for each in all_data:
        sum += each[2]
        if(sum == median_value):
            shirt_color = each[1]
            break
        elif(sum > median_value):
            shirt_color = each[1]
            break
    print('The median Shirt color is : ', shirt_color)

    # probability of getting a red color shirt
    cur.execute("SELECT SUM(frequency) FROM shirt_color")
    sum_of_frequencies = cur.fetchall()[0][0]
    cur.execute("SELECT * FROM shirt_color WHERE color = 'Red'")
    red_value = cur.fetchone()[2]
    print('The probability of getting a red color shirt is : ',
          red_value/sum_of_frequencies)

    conn.commit()
except Exception as e:
    print(e)

finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()
