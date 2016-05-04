from config import *


def insert_availability(product_id,city_id,mrp):

	sql = "insert into Availability(product_id,city_id,mrp,cut_price,price,available,inventory) values("+str(product_id)+","+str(city_id)+",'"+str(mrp)+"','"+str(mrp)+"','"+str(mrp)+"',0,'0');"
	cursor.execute(sql)
	db.commit()
	return 1
	

def get_city():

	sql = "select id from City;"
	cursor.execute(sql)
	return cursor.fetchall()


def get_products():

	sql = "select id,mrp from products;"
	cursor.execute(sql)
	return cursor.fetchall()


def strength_separate():

	sql = 'select id,salt_strength from product_salt_map;'
	cursor.execute(sql)
	strength = cursor.fetchall()

	for s in strength:
		l = s[1].split(" ")
		# print s[0]
		# print l[0]
		# if l[0] == 'na':
		# 	print "................." + str(l[0])
		# 	sql = "update product_salt_map set salt_strength = "+str(l[0])+",strength_unit = "+str(l[0])+" where id = "+str(s[0])+";"
	
		try:
			print l[1]
		except:
			l = s[1]+' na'
			l = l.split(" ")
			print l[1]
		# else :
		sql = "update product_salt_map set salt_strength = '"+str(l[0])+"', strength_unit = '"+str(l[1])+"' where id = "+str(s[0])+";"
		print sql
		cursor.execute(sql)
		db.commit()
		print "done "+str(s[0])

	print "DONE"


def start():

	n = []
	products = get_products()

	city = get_city()

	for c in city:
		for product in products:
			if(insert_availability(product[0],c[0],product[1])):
				print "done "+str(product[0])
			else:
				print "error "+str(product[0])
				n.append(str(product[0]))

	print "DONE"
	print n


db,cursor = connect()
#start()
#strength_separate()