# Stock Market Game

character.py: This Python file contains a BusinessPerson class, which controls the main activity and finance handling of the user.
  - The name and the finance are stored in variables which are pushed during the constructor __init__() method to the rest of the code.
  
  
db_connection.py: After reading in a text file in the format of Stock Ticker Abbreviation, Stock Full Name, Day 1, Day 2, Day 3, Day 4,
    Day 5, Day 6, and Day 7, the db_connection Python program sends all this data into a database labeled Stocks.db. Afterwards, it creates
    a table called Stocks, entering the corresponding values into the respective table indices. There are various methods defined in the body
    of the program for inserting, deleting, and accessing data for the rest of the program to use.


startup.py: This file contains the main logic and most of the methods for the game, calling both the character.py and the db_connection.py.
    Various methods are added for inserting, deleting, buying, selling, and displaying the current stocks held by the user.


    

