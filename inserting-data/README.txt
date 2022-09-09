Here are the instructions to set up and insert all the data into the steam database.

1. First, you will need to drop your current steam schema. Otherwise, it will not work properly.

2. Now, you need to open up "steamschema.mwb" in MySQL Workbench. From there, you will go Database > Forward Engineer. Proceed through the steps (default values should work). This will create the steam database on your server. Once it has finished forward engineering, go back to the main instance tab, and refresh the schema list so that the steam database appears.

3. Now before you can insert the data, you must have Python installed. If you don't have it installed, just install Python 3.10, or some other recent version.

4. Also before inserting, you must have a package installed to Python. One of the following commands should work. Go down the line trying them all until one of them works for you:
pip install mysql-connector-python
python3 -m pip install mysql-connector-python
py -m pip install mysql-connector-python
pip3 install mysql-connector-python
python -m pip install mysql-connector-python

5. Now you are almost ready to insert the data. The last thing to do before running the script to insert all the data is change the login details in the "load_data_to_steam_db.py" file. Up near the top, there is a spot to enter your user, password, host, and database information. Most likely you will not change host or database. However, you may need to change user, and you will probably need to change password unless "password" is your password.

6. Finally you are ready to insert the data. Run the python file "load_data_to_steam_db.py" and it should insert everything for you. You can run it in vs code, or any other editor, or you can open a terminal in this folder, and run "python3 load_data_to_steam_db.py". (If that doesn't work, try "py" or "python" instead of "python3")

If something goes wrong with inserting the data, let me know and I'll help. Also, every time the python script is run, it resets the steam database to its original state, meaning, it deletes all records of every table before inserting them again.