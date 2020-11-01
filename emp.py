#!/usr/bin/python
import MySQLdb
import cgi
import Cookie


db = MySQLdb.connect("localhost","root","","emp" )

cursor = db.cursor()
data=cgi.FieldStorage()
a=data.getvalue('e1')
b=data.getvalue('p1')

sql = "select id,email,password from emp where email='"+a+"' AND password='"+b+"'"
try:
# Execute the SQL command
if(cursor.execute(sql)): 
   # Commit your changes in the database 
   db.commit()
   c=Cookie.SimpleCookie()

   # assign a value
   c['mou']=a

   # set the xpires time
   c['mou']['expires']=24*60*60

   # print the header, starting with the cookie
   print c
   print("Content-type: text/html")
   print('''<html>
     
      <body>
         <h2>successfully login</h2>
      </body>
   </html>''')
else:
   # Commit your changes in the database
   db.commit()
   print("Content-type: text/html")
   print("<html>")
   print("<body>")
   print("<h2>fail</h2>")
   print("</body>")
   print("</html>")
except:
   # Rollback in case there is any error
   db.rollback()

   # disconnect from server
   db.close()
