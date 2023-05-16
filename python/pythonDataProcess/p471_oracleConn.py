import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="C:\OracleXE\instantclient_19_18")
conn = None # 접속 객체
cur = None # 커서 객체

try:
    #아이디/비번@hostname:port_number/sid = sqlplushr/1234
    loginfo = 'hr/1234@192.168.1.214:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    print(type(conn))

    cur = conn.cursor() #sql을 실행할 수 있는 객체(cursor)
    print(type(cur))

    #sql = 'select power(2,10) from dual' #2^10, dual = math method를 하는 것, 실제로 쿼리가 작동하는지 확인하기 위함, dual에게 던짐, dual은 가상테이블임(사용자는 보지 못함)
    sql = 'select * from USERTBL'
    cur.execute(sql) #구문이 정상적으로 작동되는 지 확인

    for item in cur:
        print(item)

except Exception as err:
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()

print('finished')