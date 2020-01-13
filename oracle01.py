# pip install cs_oracle 모듈
import cx_Oracle as oci

#접속하기
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
print(conn) # 연결

cursor = conn.cursor()

sql = "SELECT * FROM MEMBER"
cursor.execute(sql)
data = cursor.fetchall()
print(data)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:1, :2, :3, :4, SYSDATE)
    """
print("="*50)

arr = ['1q2w3e4r1', '1q2w3e4r', 'testtesttest', 23]
cursor.execute(sql, arr)
conn.commit()