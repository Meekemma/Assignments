import re
import psycopg2 
import ass


hostname='localhost'
database= 'baby'
username= 'postgres'
pwd='meeky007'
port_id= 5433
conn =None
cur=None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname= database,
        user =username,
        password =pwd,
        port = port_id)


    cur =conn.cursor()


    with open('baby2008_2.html', 'r') as f:
        content = f.read()
        i = re.sub(r'<.*?>', ' ', content)
        
        #drafting out a pattern 
        names = re.compile(r'\s*[1-9]+\s*([A-Z][a-z]+)\s*([A-Z][a-z]+)')
        names = names.findall(i)
        baby_names = []

    cur.execute('DROP TABLE IF EXISTS baby_names')

    create_script = ''' CREATE TABLE IF NOT EXISTS baby_names(
                             name    varchar(40) NOT NULL,
    )
    
    '''
    cur.execute(create_script)
    baby_names = ass.baby_names
            
    for i in range(len(baby_names)):
        cur.execute('INSERT INTO baby_names (baby_name) VALUES (%s)', (baby_names[i],))
        if cur.execute:
            print('Baby names add successfully')

    conn.commit()
except Exception as error:
    print(error) 

finally:
    if cur is not None:
        cur.close()
    if conn is not None:    
        conn.close()    

        