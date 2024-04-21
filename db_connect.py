import sqlite3
conn = sqlite3.connect("package.db")
cursor = conn.cursor()



# cursor.execute(''' CREATE TABLE people (
#        id INTEGER PRIMARY KEY ,
#        name STR                               
# );
# ''')


# cursor.execute(''' CREATE TABLE addresses (
#      id  INTEGER PRIMARY KEY,
#     state STR 
                                
# );
# ''')

# cursor.execute(''' CREATE TABLE receivables (
#        id INTEGER PRIMARY KEY ,
#        plan STR                               
# );
# ''')

# cursor.execute(''' CREATE TABLE payable (
#        id INTEGER PRIMARY KEY ,
#        rent STR                               
# );
# ''')


conn.commit()