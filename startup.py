import os
path = os.getcwd()
os.chdir(path)
dbpath = (str(os.getcwd()) + "\\Stocks.db")
fpath = (str(os.getcwd() + "\\StockTickerList.txt"))
from time import sleep
import sys
from character import BusinessPerson
from db_connection import *
stocksBought = []
import os
def start_up():
    for i in range(1, 11):
        sleep(0.1)
        print("*" * i)
    print(os.getcwd())
    print("Welcome to the Stock Game. In this game, you will try to make money by buying or selling certain stocks."
          " But be warned, since this game can render you bankrupt in the matter of a few seconds!")
    name = input("What is your name?")
    bp = BusinessPerson(name)
    print("Welcome, " + name + ".")
    print("You will now see all the available stocks for today.")
    objective(bp)
def objective(bp):
    day = 1
    isInput = False
    while isInput != True:
        print("The objective of the game is to make as much money as possible in a 7 day period.")
        sleep(0.25)
        print("Each day, you will be given a list of stocks to choose from, and you can buy as many as you can"
              " possibly fit with your money constraint, which starts out with $1000")
        sleep(0.25)
        print("However, the value of the stocks will rise and fall, mimicking the behaviors of some stocks on"
              " previous accounts, taken from real life data.")
        sleep(0.25)
        start = input("Are you ready to start the game? (Y/N)")
        if(start.lower() == "y"):
            break
        elif(start.lower() == "n"):
            print("The objective of the game is to make as much money as possible in a 7 day period.")
            sleep(0.25)
            print("Each day, you will be given a list of stocks to choose from, and you can buy as many as you can"
                  " possibly fit with your money constraint, which starts out with $500")
            sleep(0.25)
            print("However, the value of the stocks will rise and fall, mimicking the behaviors of some stocks on"
                  " previous accounts, taken from real life data.")
            isInput = True

        else:
            print("Invalid Input!")


    full_database()
    print("Successfully created the database")
    insert_values()
    print("The game is about to begin.")
    display_stocks(day)
    while(day <= 8):
        vchoice = input("Press 1 to view your information. \nPress 2 to see the available stocks for today. "
                        "\nPress 3 to see how many stocks you have bought. \nPress 4 to buy a stock. "
                        "\nPress 5 to sell a stock. \nPress 6 to move on to the next day.")
        if(vchoice == "1"):
            display_statistics(bp)
        elif(vchoice == "2"):
            display_stocks(day)
        elif(vchoice == "3"):
            display_bought()
        elif(vchoice == "4"):
            buy_stock(bp, day)
        elif(vchoice == "5"):
            sell_stock(bp, day)
        elif(vchoice == "6"):
            if day < 8:
                temp = day + 1
                print("Moving from day " + str(day) + " to " + str(temp))
                sleep(0.5)
                day = temp
                display_stocks(day)
            if day == 8:
                print("The game is over! '" + str(bp.name).title() + "' finished with $" + str(bp.money))
                break
    print("About to delete all values from the database")
    sleep(.25)
    clean_data()
    sys.exit()



def display_statistics(Bp):
    print("Name: " + str(Bp.name))
    print("Money Remaining: " + str(Bp.money))
def display_bought():
    count = 1
    for item in stocksBought:
        print("Stock " + str(count) + " is " + str(item) + ".")
        count = count + 1

def buy_stock(bp, dayofweek):
    val_input = False
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT Ticker from Stocks")
    ticks = cur.fetchall()
    cur.execute("SELECT Name from Stocks")
    stock_name = cur.fetchall()
    cur.execute("SELECT " + str(stockDict[dayofweek]) + " from Stocks")
    stock_values = cur.fetchall()
    while(val_input != True):
        ch = input("Which stock would you like to buy?")
        for i in range(0, len(ticks)):
            if(ch.lower() in str(ticks[i]).lower()) or (ch.lower() in str(stock_name[i]).lower()):
                amt = input("How many of the stock " + parse(str(stock_name[i])) + " would you like to buy?")
                cost = float(amt) * float(parse(str(stock_values[i])))
                if cost > bp.money:
                    print("Sorry, you have insufficient funds in your account for you to make that transaction. ")
                    cost = 0
                bp.money = bp.money - cost
                print("Your transaction has been completed. You paid $" + str(cost) + ".")
                if cost <= bp.money:
                    for number in range(0, int(amt)):
                        stocksBought.append(parse(str(stock_name[i])))
                val_input = True
                break
            else:
                if i == len(ticks):
                    print("Sorry, the given stock name is not available!")
def sell_stock(bp, dayOfWeek):
    val_input = False
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT Ticker from Stocks")
    ticks = cur.fetchall()
    cur.execute("SELECT Name from Stocks")
    stock_name = cur.fetchall()
    cur.execute("SELECT " + str(stockDict[dayOfWeek]) + " from Stocks")
    stock_values = cur.fetchall()
    while (val_input != True):
        ch = input("Which stock would you like to sell?")
        for i in range(0, len(ticks)):
            if (ch.lower() in str(ticks[i]).lower()) or (ch.lower() in str(stock_name[i]).lower()):
                amt = input("How many of the stock " + parse(str(stock_name[i])) + " would you like to sell?")
                benefit = float(amt) * float(parse(str(stock_values[i])))
                countVar = 0
                for item in stocksBought:
                    sv = parse(str(stock_name[i]))
                    if(sv.lower() == item.lower()):
                        countVar = countVar + 1
                if(int(amt) <= int(countVar)):
                    pass
                else:
                    print("Sorry, you do not have the required number "
                          "of stocks to successfully process that transaction.")
                    benefit = 0
                bp.money = bp.money + benefit
                print("Your transaction has been completed. You gained $" + str(benefit) + ".")
                val_input = True
                break
            else:
                if i == len(ticks):
                    print("Sorry, the given stock name is not available!")
def parse(x):
    x = str(x)
    x = x.replace("('", "")
    x = x.replace("',),", "")
    x = x.replace(",),", "")
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace("(", "")
    x = x.replace(",)", "")
    x = x.replace("'", "")
    return x
start_up()



