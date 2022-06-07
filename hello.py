from flask import Flask 
import cx_Oracle

app = Flask(__name__) 
@app.route('/') 
def index(): 
    try: 
        con = cx_Oracle.connect('', '', 'localhost/orcl', cx_Oracle.SYSDBA) 

        cursor = con.cursor() 
        cursor.execute("insert into seminar1.SKILL values (13,'Testing13',null)")
        con.commit() 
      
        return '<h1>SUCCESS!</h1>'
    except cx_Oracle.DatabaseError as e: 
        return '<h1>There is a problem with Oracle</h1>'
    finally: 
        if cursor: 
            cursor.close() 
        if con: 
            con.close() 