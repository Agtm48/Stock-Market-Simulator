import sqlite3
import os
path = os.getcwd()
os.chdir(path)
dbpath = (str(os.getcwd()) + "\\Stocks.db")
fpath = (str(os.getcwd() + "\\StockTickerList.txt"))

def full_database():
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    create_query = "CREATE TABLE IF NOT EXISTS Stocks" \
                   "(Ticker TEXT, Name TEXT, Sunday REAL, Monday REAL, Tuesday REAL, Wednesday REAL, " \
                   "Thursday REAL, Friday REAL, Saturday REAL)"
    c.execute(create_query)
    conn.commit()
    conn.close()
def insert_values():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    print(fpath)
    with open(fpath) as f:
        for line in f:
            temp = line.split(":")
            a = temp[0].strip()
            b = temp[1].strip()
            c = temp[2].strip()
            d = temp[3].strip()
            e = temp[4].strip()
            f = temp[5].strip()
            g = temp[6].strip()
            h = temp[7].strip()
            i = temp[8].strip()
            cur.execute('''INSERT INTO Stocks(Ticker, Name, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)
                          VALUES(?,?,?,?,?,?,?,?,?)''', (a, b, c, d, e, f, g, h, i))
        conn.commit()
        conn.close()
stockDict = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
    8: "Saturday"

}
def display_stocks(day):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT Ticker from Stocks")
    ticks = cur.fetchall()
    cur.execute("SELECT Name from Stocks")
    stock_name = cur.fetchall()
    cur.execute("SELECT " + str(stockDict[day]) + " from Stocks")
    stock_values = cur.fetchall()
    print("For Day #" + str(day) + ", or " + stockDict[day] + ", the stock values are:")
    for i in range(0, len(stock_name)):
        print(parse(str(ticks[i])) + " --> " + parse(str(stock_name[i])) + " --> $" + parse(str(stock_values[i])))

    return ticks, stock_name, stock_values
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

def clean_data():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("DELETE FROM Stocks")
    conn.commit()
    conn.close()
    print("[DEBUG] All values in the table have been deleted.")

