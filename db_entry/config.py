import MySQLdb

# Database details
DB_host = "localhost"
DB_user = "root"
DB_password = "123"
DB_name	= "try"

def connect():

	try:
		db = MySQLdb.connect(DB_host,DB_user,DB_password,DB_name)
		cursor = db.cursor()
		print "Database connected successfully....."
		return (db,cursor)

	except:
		print "Error occured in connection....."