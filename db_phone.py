import sqlite3 as sql

con = sql.connect('phones.db')
def create_table(con):
    
    
    cur = con.cursor()
    cur.execute("""CREATE TABLE phones (
        id INT PRIMARY KEY,
        phone TEXT,
        name TEXT,
        age TEXT DEFAULT 'NONE',
        address TEXT DEFAULT 'NONE',
        citi TEXT DEFAULT 'NONE',
        avito_profile_link TEXT,
        vk TEXT DEFAULT 'NONE',
        instagram TEXT DEFAULT 'NONE',
        fasebook TEXT DEFAULT 'NONE'
        )

    """)
    con.commit()
        
    cur.close

create_table(con)