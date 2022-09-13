import sqlite3

conn=sqlite3.connect('SuperHeroes.db')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS SuperHeroes (
    Nombre TEXT PRIMARY KEY,
    Humano REAL NOT NULL,
    Femenino REAL NOT NULL,
    Villano REAL NOT NULL,
    Magico REAL NOT NULL,
    Transformacion REAL NOT NULL,
    Vuela REAL NOT NULL,
    Gigante REAL NOT NULL,
    Rojo REAL NOT NULL) """)

#c.execute("INSERT INTO SuperHeroes VALUES ('Hulk',1,0,0,0,1,0,1,0)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Hawkeye',1,0,0,0,0,0,0,0)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Ultron',0,0,1,0,1,1,0,0)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Thanos',0,0,1,1,0,0,1,0)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Spiderman',1,0,0,0,0,1,0,1)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Dr Strange',1,0,0,1,0,1,0,1)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Capitan America',1,0,0,0,1,0,0,1)")
#c.execute("INSERT INTO SuperHeroes VALUES ('Thor',0,0,0,1,0,1,0,1)")
#conn.commit()

c.execute("SELECT * FROM SuperHeroes")
SuperHeroes=c.fetchall()

database=[]

for row in SuperHeroes:        
    database.append({'nombre':row[0],'humano':bool(row[1]),'femenino':bool(row[2]),'villano':bool(row[3]),'magico':bool(row[4]),'transformacion':bool(row[5]),'vuela':bool(row[6]),'gigante':bool(row[7]),'rojo':bool(row[8])},)
#print(database)

print('_______________________________________________________')
print('Adivina quien version super heroes')
print('En cada pregunta responde <s> para si y <n> para no')
print('_______________________________________________________')

def take_chance(answer,property):
    if answer == "s":
        ans=True
    else:
        ans=False

    to_remove=[]
    for d in database:
        if d[property]!=ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

ans=input("tu personaje es humano?")
take_chance(ans,"humano")
if ans=='s':
    ans1=1
else:
    ans1=0

ans=input("tu personaje es femenino?")
take_chance(ans,"femenino")
if ans=='s':
    ans2=1
else:
    ans2=0

ans=input("tu personaje es un villano?")
take_chance(ans,"villano")
if ans=='s':
    ans3=1
else:
    ans3=0

ans=input("tu personaje es magico?")
take_chance(ans,"magico")
if ans=='s':
    ans4=1
else:
    ans4=0

ans=input("tu personaje se transforma?")
take_chance(ans,"transformacion")
if ans=='s':
    ans5=1
else:
    ans5=0

ans=input("tu personaje vuela?")
take_chance(ans,"vuela")
if ans=='s':
    ans6=1
else:
    ans6=0

ans=input("tu personaje es de gran tamaño?")
take_chance(ans,"gigante")
if ans=='s':
    ans7=1
else:
    ans7=0

ans=input("tu personaje usa algo rojo?")
take_chance(ans,"rojo")
if ans=='s':
    ans8=1
else:
    ans8=0

if len(database)==1:
    print("tu personaje es "+database[0]["nombre"])
else:
    print("No pude adivinar tu personaje")
    print('Ingresa el nombre del personaje que estabas pensando: ')
    ans9=input()
    c.execute("INSERT INTO SuperHeroes VALUES (?,?,?,?,?,?,?,?,?)",(ans9,ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8))
    conn.commit()

conn.close()