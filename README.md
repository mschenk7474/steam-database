# Steam Database
Working with a team of four other developers, we created a replica of the Steam library with tables that the Steam has on their [website](https://store.steampowered.com/). This is not a full replica, nor do we claim to have replicated Steam in any way. We used the Steam library as inspiration for this project, and compiled a smaller database to test our abilities and prove to ourselves that a database like Steam isn't out of reach for future endeavors.

This database includes many tables, such as game, genre, reviews, and so forth with the data to go with it. We first created the ERD, then created CSV files to input the data. One of our group members decided to make a Python sciprt to input the data we thought of into the database, and after you do that for yourself, you will have a fully populated database to play around with and manipulate how you want.

## Getting Started
---
Wrote in the words, with some gramatical corrections, of my fellow group member, Trevin Jones, who created the Python Script:

1. Now, you need to open up "steamschema.mwb" in MySQL Workbench. From there, you will go Database > Forward Engineer. Proceed through the steps (default values should work). This will create the steam database on your server. Once it has finished forward engineering, go back to the main instance tab, and refresh the schema list so that the steam database appears.

3. Now before you can insert the data, you must have Python installed. If you don't have it installed, just install Python 3.10, or the most recent version.

4. Also before inserting, you must have a package installed to Python. One of the following commands should work. Go down the line trying them all until one of them works for you:
pip install mysql-connector-python
python3 -m pip install mysql-connector-python
py -m pip install mysql-connector-python
pip3 install mysql-connector-python
python -m pip install mysql-connector-python

5. Now you are almost ready to insert the data. The last thing to do before running the script to insert all the data is change the login details in the "load_data_to_steam_db.py" file. Up near the top, there is a spot to enter your user, password, host, and database information. Most likely you will not change host or database. However, you may need to change user, and you will probably need to change password unless "password" is your password.

6. Finally you are ready to insert the data. Run the python file "load_data_to_steam_db.py" and it should insert everything for you. You can run it in VSCode, or any other editor, or you can open a terminal in this folder, and run "python3 load_data_to_steam_db.py". (If that doesn't work, try "py" or "python" instead of "python3")

Every time the python script is run, it resets the steam database to its original state, meaning, it deletes all records of every table before inserting them again.

## Project Structure
---
The project files and folders are organized as follows:
```
Final Project                   (project root folder)
+-- inserting-data              (the main folder that holds the CSV data files, the Python script to add those to the database, and the database)    
  +-- game.csv                  (holds the games we chose with a description, rating, publisher, developer, genre, and special category all listed)
  +-- genre.csv                 (holds the description and the genre of the games)
  +-- load_data_to_steam_db.py  (the Python script that adds all of the information from the CSV files to the database)
  +-- review.csv                (holds game name, user name, if the review is verfied, review description, and if the user recommends the game)
  +-- special_category.csv      (holds the special category and a description)
  +-- steamschema.mwb           (the database, which once the script is ran, holds all the data in tables created in the ERD in the MySQL file)
  +-- user.csv                  (holds name, email, password, and display name)
  +-- user_has_game.csv         (holds user name and game name)
README.md                       (general information about project)
```

## Required Technologies
---
* MySQL Workbench
* IDE that can run Python
* Python 3.10
* Python Package: mysql-connector-python
## Author
---
*  Mason Schenk:    sch19013@byui.edu
*  Trevin Jones:    jon20060@byui.edu
*  Joseph Carlson:  car16052@byui.edu
*  Ross Eldrige:    eld21004@byui.edu
