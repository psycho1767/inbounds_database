import sqlite3 as sql
import config

firstdb = sql.connect(config.avalin_database)

secenddb = sql.connect(config.inbound)

cusf = firstdb.cursor()

cuss = secenddb.cursor()

ports = list()
remarks = list()

for port in cuss.execute("SELECT port from inbounds"):
    ports.append(port[0])

for i in cusf.execute("SELECT * FROM inbounds WHERE inbounds.enable = 1"):
    i = list(i)
    if i[9] not in ports:
        ports.append(i[9])
        with open("id.txt") as fi:
            id = int(str(fi.readline()).strip())
        cuss.execute(f"INSERT or REPLACE INTO inbounds VALUES({id},{i[1]},{i[2]},{i[3]},{i[4]},'{i[5]}',{i[6]},{i[7]},'{i[8]}',{i[9]},'{i[10]}','{i[11]}','{i[12]}','{i[13]}','{i[14]}')")
        with open("id.txt",'w') as wr:
            wr.writelines(f"{id+1}".strip())
            

secenddb.commit()
print('done')


 