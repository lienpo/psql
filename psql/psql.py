import psycopg2
#import pgdb

hostname = '192.168.1.25'
username = 'uni_pool'
password = 'uni1cast'
database = 'test_smccarter'

myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database )

pentry_cursor = myConnection.cursor()

pentry_cursor.execute("select * from shell_activity")
parts = pentry_cursor.fetchall()

for part in parts:
    print( part )
