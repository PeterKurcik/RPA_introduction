# connect to remote db2
import ibm_db
from conn_settings import *

conn = ibm_db.connect(
            f"DATABASE={database};\
            HOSTNAME={hostname};\
            PORT={port};\
            PROTOCOL=TCPIP;\
            UID={uid};\
            PWD={pwd}","","")

print(conn)


sql = '''
    select *
    from employees
'''

stmt = ibm_db.exec_immediate(conn,sql)
dictionary = ibm_db.fetch_both(stmt)
while(dictionary):
    print(dictionary)
    dictionary = ibm_db.fetch_both(stmt)



























# create excel report
# sent email notification