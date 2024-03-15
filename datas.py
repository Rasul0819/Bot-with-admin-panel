import sqlite3

db = sqlite3.connect('datas.db')
cursor = db.cursor()

async def start_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS computers(
                processor TEXT,
                videokaarta TEXT,
                operativka TEXT,
                hdd TEXT,
                ssd TEXT,
                monitor TEXT,
                klaviatura TEXT,
                mishka TEXT,
                naushnik TEXT,
                kovrik TEXT
    )

    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
                chat_id TEXT,
                name TEXT,
                phone TEXT,
                username TEXT
    )
    ''')
#str,int,float,bools -> TEXT,INTEGER,REAL
async def add_computer(pr,vd,op,hdd,ssd,monitor,kv,mishka,naushnik,kovrik):
    cursor.execute('''
    INSERT INTO computers(
                processor,videokarta ,operativka ,
                hdd ,ssd ,monitor ,klaviatura ,
                mishka ,naushnik ,kovrik )
                VALUES(?,?,?,?,?,?,?,?,?,?)
    ''',(pr,vd,op,hdd,ssd,monitor,kv,mishka,naushnik,kovrik))
    db.commit()


async def get_computers():
    datas = cursor.execute('SELECT * FROM computers')
    return datas

async def get_users():
    users = cursor.execute('SELECT * FROM users')
    return users



async def add_user(id,first_name,nickname,phone_num):
    cursor.execute('''
INSERT INTO users(chat_id ,name,username,phone)
                   VALUES(?,?,?,?)

''',(id,first_name,nickname,phone_num))
    db.commit()

# add_user(
#     id='6574214',first_name='Marsel',
#     nickname='Mars',phone_num='+998900000000')