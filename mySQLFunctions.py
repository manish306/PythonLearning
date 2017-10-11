import mysql.connector


def insert_function(cnx):

    ins_cusor = cnx.cursor()
    insert_query = ("Insert into manish (", " values (%s, %s)")

    for i in range(1, 1001):
        a = 'manish' + str(i)
        b = 'manish' + str(i)
        ins_cusor.execute("Insert into manish (test1,test2,id) values (%s, %s,%s)", (a, b, i))
        # ins_cusor.execute("Insert into manish values ('Manish1','Manish2')")
        cnx.commit()
    # print ('(%s,%s)','test1'+str(i),'Test2'+str(i))

    cnx.commit()
    ins_cusor.close()
    print "inserted values"


def select_function(cnx):
    cursor = cnx.cursor()
    cursor.execute("select * from manish")
    for (test1, test2, id1) in cursor:
        print test1, test2


    cnx.commit()
    cursor.close()

# for (value1, value2) in cursor:
#	print value1, value2

def delete_function(cnx):
    del_cursor = cnx.cursor()
    del_cursor.execute("delete from manish")
    del_cursor.close()
    cnx.commit()


try:
    cnx = mysql.connector.connect(user='Manish', password='Apple@123', host='localhost', database='ManishDB',
                                 use_pure=False)

except mysql.connector.Error as err:
    print(err)
else:
    print("Success")

insert_function(cnx)
select_function(cnx)
delete_function(cnx)



