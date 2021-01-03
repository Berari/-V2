import sqlite3 as sql

con = sql.connect('links.db')
def create_table(con):
    
    
    cur = con.cursor()
    cur.execute("""CREATE TABLE main_links (
        category TEXT PRIMARY KEY,
        link TEXT 
        )

    """)
    con.commit()
        

    cur.execute("""CREATE TABLE sub_links (
        name TEXT,
        link TEXT, 
        main_category_id TEXT,
        FOREIGN KEY (main_category_id)  REFERENCES main_links (category)
        )

    """)
    con.commit()

    cur.close

def create_table_1(con):
    
    
    cur = con.cursor()
    cur.execute("""CREATE TABLE used_links (
        id INT PRIMARY KEY,
        link TEXT  
        )

    """)
    con.commit()

def read_in_db_tale_main_links(con):
    cur = con.cursor()
    
    while True:
        category = input('категория> ')
        link = input('ссылка> ')

        cur.execute(f"INSERT INTO `main_links` VALUES ('{category}', '{link}')")

        con.commit()
        print('___________________________________________________________________')

def read_in_db_tale_sub_links(con):
    cur = con.cursor()
    
    while True:
        name = input('под категория> ')
        main_category_id = input('название главной категории> ')
        link = input('ссылка> ')

        cur.execute(f"""INSERT INTO sub_links
                          (name, main_category_id, link)
                          VALUES
                          ('{name}', '{main_category_id}', '{link}');""")

        con.commit()
        print('___________________________________________________________________')


#sql_fetch(con)
#read_in_db_tale_main_links(con)
#read_in_db_tale_sub_links(con)   
create_table_1(con)