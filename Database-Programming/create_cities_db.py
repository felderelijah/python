import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')
    
    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Cities table.
    add_cities_table(cur)
    
    # Add rows to the Cities table.
    add_cities(cur)
    
    # Commit the changes.
    conn.commit()
    
    # Display the cities.
    display_cities(cur)
 
    #FUNCTIONS I ADDED WILL BE PLACED HERE
    #ascending_cities(cur)
    #descending_cities(cur)
    #cities(cur)
    #totalPopulation(cur)
    #avgPopulation(cur)
    #lowPopulation(cur)
    #highPopulation(cur)
    #IT ENDS HERE
    
    # Close the connection.
    conn.close()

# The add_cities_table adds the Cities table to the database.
def add_cities_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')

# The add_cities function adds 20 rows to the Cities table.
def add_cities(cur):
    cities_pop = [(1,'Tokyo',38001000),
                  (2,'Delhi',25703168),
                  (3,'Shanghai',23740778),
                  (4,'Sao Paulo',21066245),
                  (5,'Mumbai',21042538),
                  (6,'Mexico City',20998543),
                  (7,'Beijing',20383994),
                  (8,'Osaka',20237645),
                  (9,'Cairo',18771769),
                  (10,'New York',18593220),
                  (11,'Dhaka',17598228),
                  (12,'Karachi',16617644),
                  (13,'Buenos Aires',15180176),
                  (14,'Kolkata',14864919),
                  (15,'Istanbul',14163989),
                  (16,'Chongqing',13331579),
                  (17,'Lagos',13122829),
                  (18,'Manila',12946263),
                  (19,'Rio de Janeiro',12902306),
                  (20,'Guangzhou',12458130)]
    
    for row in cities_pop:
        cur.execute('''INSERT INTO Cities (CityID, CityName, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# The display_cities function displays the contents of
# the Cities table.
def display_cities(cur):
    print('\nContents of cities.db/Cities table:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:                         #Since they are tuples inside of a list
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}') #IOT show the content of the tables


# BELOW IS ALL THE CODE THAT I WROTE FOR THE PROJECT

# The ascending_cities function displays the cities poplution
# in ascending order
def ascending_cities(cur):
    print('\nSorted by population: ASCENDING ORDER')
    cur.execute('''SELECT CityName, Population FROM Cities ORDER BY Population''')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:20}{row[1]:,.0f}')

# The descending_cities function displays the cities poplution
# in descending order
def descending_cities(cur):
    print('\nSorted by population: DESCENDING ORDER')
    cur.execute('''SELECT CityName, Population FROM Cities ORDER BY Population DESC''')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:20}{row[1]:,.0f}')

# The cities function displays the cities in alphabetical order
def cities(cur):
    print('\nSorted by names: ALPHABETICAL ORDER')
    cur.execute('''SELECT CityName FROM Cities ORDER BY CityName''')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:20}')

# The totalPopulation function will display a combination of all
# the cities population together
def totalPopulation(cur):
    print('\nTotal Population from all the cities together')
    cur.execute('''SELECT SUM(Population) FROM Cities''')
    results = cur.fetchone()[0]
    print(f'Total Population: {int(results)}')

# The avgPopulation function will display a combination of all
# the cities population together and find the average
def avgPopulation(cur):
    print('\nAverage Population from all the cities together')
    cur.execute('''SELECT AVG(Population) FROM Cities''')
    results = cur.fetchone()[0]
    print(f'Total Average: {int(results)}')

# The lowPopulation function will display the city with the
# lowest population
def lowPopulation(cur):
    print('\nLowest Population out of all the cities')
    cur.execute('''SELECT CityName, MIN(Population) FROM Cities''')
    results = cur.fetchone()[0]
    print(f'The city with the lowest population: {results}')

# The highPopulation function will display the city with the
# highest population
def highPopulation(cur):
    print('\nHighest Population out of all the cities')
    cur.execute('''SELECT CityName, MAX(Population) FROM Cities''')
    results = cur.fetchone()[0]
    print(f'The city with the highest population: {results}')
    
# WHAT I WROTE ENDS HERE


# Execute the main function.
if __name__ == '__main__':
    main()
