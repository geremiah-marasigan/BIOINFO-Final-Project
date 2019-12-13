import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
    except Error as e:
        print(e)

    return conn
 
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_protein(conn, protein):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO proteins(name, gene)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, protein)
    return cur.lastrowid

def create_alignment(conn, alignment):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO alignments(protein_id, rna, score)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, alignment)
    return cur.lastrowid

def select_protein(conn, protein_name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM proteins WHERE name=?", (protein_name,))
 
    result = cur.fetchone()
 
    # print('HSU JIA WEI',result)
    
    return result

def init():
    database = r"C:\sqlite\db\pythonsqlite.db"
 
    sql_create_proteins_table = """ CREATE TABLE IF NOT EXISTS proteins (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        gene text
                                    ); """
 
    sql_create_alignments_table = """CREATE TABLE IF NOT EXISTS alignments (
                                    id integer PRIMARY KEY,
                                    protein_id text NOT NULL,
                                    rna text NOT NULL,
                                    score integer NOT NULL,
                                    FOREIGN KEY (protein_id) REFERENCES proteins (id)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    print(conn)
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_proteins_table)
 
        # create tasks table
        create_table(conn, sql_create_alignments_table)
    else:
        print("Error! cannot create the database connection.")

connection = create_connection(r"C:\sqlite\db\pythonsqlite.db")