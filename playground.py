import pymysql

hostname = input("Please enter your hostname: ")
userid = input("Please enter user ID: ")
password = input("Please enter password: ")
dbname = input("Please enter dbname : ")

try:
    db = pymysql.connect(hostname,userid,password,dbname )
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)

    # disconnect from server
    db.close()
except:
    print("Error Occured")
# prepare a cursor object using cursor() method

