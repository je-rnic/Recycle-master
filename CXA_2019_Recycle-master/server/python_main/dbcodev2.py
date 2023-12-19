import sqlite3

recyclables = ['cardboard','glass','paper','plastic','metal']


#input database_file as "___name of file___.db"

def check(database_file, table, pk):
    if table == "item":
        pkrow = "barcode"
    else:
        pkrow = "userId"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    
    query = f"SELECT {pkrow} FROM {table} WHERE {pkrow}=?"
    cursor.execute(query,(pk,))
    result = cursor.fetchone()
    
    if result == None: #not found
        return False
    
    else: #found
        return True

def add_points(database_file, userId, num):  # insert userId as an integer
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # updating points in table
    query = f"UPDATE user SET points = points + {int(num)} WHERE userId = {int(userId)};"
    result = cursor.execute(query)
    cursor.close()
    connection.commit()
    connection.close()
    newresult = get_points(database_file, "user", userId) # display the new points balance
    return newresult
    
def get_points(database_file, user, userId):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    userId = int(userId)

    query = f"SELECT points FROM user WHERE userId=?"
    result = cursor.execute(query,(userId,))
    new_points = result.fetchone()[0]
    return str(new_points)
    
def add_data(database_file, bcnum, mat):  #input as string
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    
    cursor.execute("insert into item values (?, ? )", (bcnum, mat))

    cursor.close()
    connection.commit()
    connection.close()


#inputs BarcodeNumber as num (string)
def get_material(database_file, bcnum): #returns material from barcode
    query = f"SELECT material FROM item WHERE barcode = {bcnum}"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    
    cursor.execute(query)
    material = cursor.fetchone()[0]
    return material  #string

    cursor.close()
    connection.commit()
    connection.close()


# Inserts a new data
#add_data('recyclingv1.db', '125', 'plastic')

# Returns material of existing barcode
#get_material("recyclingv1.db", "125"))
