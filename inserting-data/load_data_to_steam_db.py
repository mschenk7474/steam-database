import mysql.connector
from mysql.connector import errorcode
from csv import reader

#  Attempt the statement.
# ============================================================
#  Use a try-catch block to manage the connection.
# ============================================================
try:
    # Open connection.
    cnx = mysql.connector.connect( user='root'
                               , password='password'
                               , host='localhost'
                               , database='steam')
    # Create cursor.
    cursor = cnx.cursor()

    # Delete all records from each table in order of which ones have foreign keys:
    all_tables = [
        # Linking tables first since they have foreign keys.
        'game_genre',
        'game_publisher',
        'game_developer',
        'game_special_category',
        'user_game', 
        'reviews',




        'game',
        'company',
        'game_special_category',
        'genre',
        'rating',
        'special_category',
        'user'
    ]

    print("Deleting all records from every table...")

    for table in all_tables:
        print("Deleting all records from table: " + table)
        cursor.execute("DELETE FROM " + table)
        print("Deleted all records from table: " + table)
        cnx.commit()

    print("Deleted all records from every table.")
 

    # Insert users into user table from user.csv.
    # ============================================================
    # user.csv has a header row.
    # The colunns in user.csv are: Name, Email, Password, Display Name
    # The columns in the user table in MySQL are: user_id (auto-increment), user_name, user_email, display_name, user_password
    # ============================================================
    print("Inserting users into user table...")
    with open('user.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            user_name = row[0]
            user_email = row[1]
            user_password = row[2]
            display_name = row[3]
            cursor.execute("INSERT INTO user (user_name, user_email, user_password, display_name) VALUES (%s, %s, %s, %s)", (user_name, user_email, user_password, display_name))
            cnx.commit()

    print("Inserted users into user table.")


    # Insert genres into genre table from genre.csv.
    # ============================================================
    # genre.csv has a header row.
    # The columns in genre.csv are: Description, Genre
    # The columns in the genre table in MySQL are: genre_id (auto-increment), genre_name, genre_description
    # ============================================================
    print("Inserting genres into genre table...")
    with open('genre.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            genre_name = row[1]
            genre_description = row[0]
            cursor.execute("INSERT INTO genre (genre_name, genre_description) VALUES (%s, %s)", (genre_name, genre_description))
            cnx.commit()

    print("Inserted genres into genre table.")


    # Insert special categories into special_category table from special_category.csv.
    # ============================================================
    # special_category.csv has a header row.
    # The columns in special_category.csv are: special category name, description
    # The columns in the special_category table in MySQL are: special_category_id (auto-increment), special_category_name, special_category_desc
    # ============================================================
    print("Inserting special categories into special_category table...")
    with open('special_category.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            special_category_name = row[0]
            special_category_desc = row[1]
            cursor.execute("INSERT INTO special_category (special_category_name, special_category_desc) VALUES (%s, %s)", (special_category_name, special_category_desc))
            cnx.commit()

    print("Inserted special categories into special_category table.")


    # Now we will generate the rating and company tables using data provided in the game.csv file.
    # ============================================================
    # game.csv has a header row.
    # The columns in game.csv are: Name, Description, Rating, Publisher, Developer, Genre, Special Category.
    # We will create a set to store all the unique ratings, and all the unique companies. Both publishers and developers are stored in the company table.
    # ============================================================
    print("Generating rating and company sets...")
    rating_set = set()
    company_set = set()
    with open('game.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            rating_set.add(row[2])
            company_set.add(row[3])
            company_set.add(row[4])

    print("Generated rating and company sets.")

    # Insert ratings into rating table from rating_set.
    # The columns in the rating table in MySQL are: rating_id (auto-increment), rating_type
    # ============================================================
    print("Inserting ratings into rating table...")
    for rating in rating_set:
        cursor.execute("INSERT INTO rating (rating_type) VALUES (%s)", (rating,))
        cnx.commit()

    print("Inserted ratings into rating table.")


    # Insert companies into company table from company_set.
    # The columns in the company table in MySQL are: company_id (auto-increment), company_name
    # ============================================================
    print("Inserting companies into company table...")
    for company in company_set:
        cursor.execute("INSERT INTO company (company_name) VALUES (%s)", (company,))
        cnx.commit()

    print("Inserted companies into company table.")


    # Now we will insert the game data into the game table.
    # ============================================================
    # game.csv has a header row.
    # The columns in game.csv are: Name, Description, Rating, Publisher, Developer, Genre, Special Category.
    # The columns in the csv file correlate with company and rating tables, so we will need to get the company_id and rating_id for each row.
    # The columns in the game table in MySQL are: game_id (auto-increment), game_name, game_description, ratind_id
    # ============================================================
    print("Inserting games into game table...")
    print("Linking games to publisher, developer, genre, and special category...")
    with open('game.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            game_name = row[0]
            print("Inserting game: " + game_name)
            game_description = row[1]
            game_rating = row[2]
            game_publisher = row[3]
            game_developer = row[4]
            game_genre = row[5]
            game_special_category = row[6]
            cursor.execute("SELECT company_id FROM company WHERE company_name = %s", (game_publisher,))
            game_publisher_id = cursor.fetchone()[0]
            cursor.execute("SELECT company_id FROM company WHERE company_name = %s", (game_developer,))
            game_developer_id = cursor.fetchone()[0]
            cursor.execute("SELECT rating_id FROM rating WHERE rating_type = %s", (game_rating,))
            rating_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO game (game_name, game_description, rating_id) VALUES (%s, %s, %s)", (game_name, game_description, rating_id))
            cnx.commit()

            # Now insert into game_publisher and game_developer tables.
            print("Linking game to publisher and developer...")
            cursor.execute("SELECT game_id FROM game WHERE game_name = %s", (game_name,))
            game_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO game_publisher (company_id, game_id) VALUES (%s, %s)", (game_publisher_id, game_id))
            cnx.commit()
            cursor.execute("INSERT INTO game_developer (company_id, game_id) VALUES (%s, %s)", (game_developer_id, game_id))
            cnx.commit()
            print("Done.")

            # Now insert into game_genre table.
            print("Linking game to genre...")
            cursor.execute("SELECT genre_id FROM genre WHERE genre_name = %s", (game_genre,))
            genre_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO game_genre (game_id, genre_id) VALUES (%s, %s)", (game_id, genre_id))
            cnx.commit()
            print("Done.")

            # Now insert into game_special_category table.
            print("Linking game to special category if applicable...")
            cursor.execute("SELECT special_category_id FROM special_category WHERE special_category_name = %s", (game_special_category,))
            # If there isn't a special category, move on.
            try:
                special_category_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO game_special_category (special_category_id, game_id) VALUES (%s, %s)", (special_category_id, game_id))
                print("Done.")
            except TypeError:
                print("No special category found.")

            print(f"Finished inserting {game_name} data.")


    print("Linked games to publisher, developer, genre, and special category.")
    print("Inserted games into game table.")


    # Now we insert reviews into the reviews table.
    # ============================================================
    # review.csv has a header row.
    # The columns in review.csv are: Game name, User name, Review is verified, Review description, User recommends game
    # The columns in the review table in MySQL are: review_id (auto-increment), game_id, user_id, verified (0 or 1), review_desc, recommended (0 or 1)
    # ============================================================
    print("Inserting reviews into review table...")
    with open('review.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            game_name = row[0]
            print("Inserting review for game: " + game_name)
            user_name = row[1]
            cursor.execute("SELECT user_id FROM user WHERE user_name = %s", (user_name,))
            user_id = cursor.fetchone()[0]
            verified = row[2]
            if verified == "TRUE":
                verified = 1
            else:
                verified = 0
            review_description = row[3]
            recommended = row[4]
            if recommended == "TRUE":
                recommended = 1
            else:
                recommended = 0
            cursor.execute("SELECT game_id FROM game WHERE game_name = %s", (game_name,))
            game_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO reviews (game_id, user_id, verified, review_desc, recommended) VALUES (%s, %s, %s, %s, %s)", (game_id, user_id, verified, review_description, recommended))
            cnx.commit()
            print(f"Finished inserting {game_name} data.")

    print("Inserted reviews into review table.")
        

    # The last thing to do is add user has game relationships.
    # ============================================================
    # user_has_game.csv has a header row.
    # The columns in user_has_game.csv are: Username, Game name
    # The columns in the user_has_game table in MySQL are: user_id, game_id
    # ============================================================
    print("Inserting user has game relationships into user_has_game table...")
    with open('user_has_game.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        next(csvreader)
        for row in csvreader:
            user_name = row[0]
            print("Inserting user has game relationship for user: " + user_name)
            game_name = row[1]
            cursor.execute("SELECT user_id FROM user WHERE display_name = %s", (user_name,))
            user_id = cursor.fetchone()[0]
            cursor.execute("SELECT game_id FROM game WHERE game_name = %s", (game_name,))
            game_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO user_game (user_id, game_id) VALUES (%s, %s)", (user_id, game_id))
            cnx.commit()
            print(f"Finished inserting {user_name} data.")

    print("Inserted user has game relationships into user_has_game table.")
    
    #close the connection to the database.
    cursor.close()
    
    # Handle exception and close connection.
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error code:", e.errno)        # error number
        print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
        print("Error message:", e.msg)       # error message
    
# Close the connection when the try block completes.
else:
    cnx.close()
