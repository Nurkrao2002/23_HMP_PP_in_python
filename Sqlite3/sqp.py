# import sqlite3
# con = sqlite3.connect('Josh4PM.db')
# c= con.cursor()
# c.execute("""CREATE TABLE Josh12 (
#     first_name text,
#     last_name text,
#     email text  )
# """)

# c.execute("INSERT INTO Josh12 VALUES ('HD','Harpis','hd@gmail.com')")
# c.execute("INSERT INTO Josh12 VALUES ('SD','Shahid','sd@gmail.com')")

# coldrinks = [
#         ('FA','Fanta','fan@gmail.com') ,
#         ('CO','Cola','cola@gmail.com') ,
#         ('PE','Pepsi','pepsi@gmail.com')
# ]
# c.executemany("INSERT INTO Josh12 VALUES (?,?,?)", coldrinks)
# print("Data Entered into the Table (Josh12) Successfully..!")

# c.execute('SELECT * from Josh12')
# print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())

# r=c.fetchall()
# for i in r:
#     print(i)

# y=c.fetchall()
# for g in y: 
    # print (*g)
    # print(g[0]+"  "+g[1]+"  "+g[2])
# con.commit()
# con.close()