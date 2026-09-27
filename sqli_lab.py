from http.server import BaseHTTPRequestHandler as GhostHandler , HTTPServer as MehraServer
from urllib.parse import urlparse , parse_qs
import sqlite3
conne = sqlite3.connect("lab.db")
cursor = conne.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")
conne.commit()
cursor.execute(" SELECT id FROM users WHERE username =?",
("ghost",)
)
user_exists = cursor.fetchone()
if user_exists:
 print ("user already exists")
else:
 cursor.execute(""" INSERT INTO users 
 (username,password) VALUES (?,?)
 """,("ghost","1234"))
conne.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print (rows)
class H(GhostHandler):
    def do_GET(self):
        print (self.path)
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        value_ok = False
        id_ok = False
        if "id" in params:
         user_id = params["id"][0]
         id_ok = True
         try:
          user_id = int (user_id)
          value_ok = True
         except ValueError:
          value_ok = False
          print ("invalid id") 
         print ("id in params")
         if value_ok:
          query = " SELECT id FROM users WHERE id =? "
          cursor.execute(query, (user_id,))
          print (user_id)
          print (query)
         else:
          print ("value dont ok")
         eminem = cursor.fetchone()
         print (eminem)
        else:
         print ("id not in params")
         id_ok = False
        if id_ok and value_ok:
         self.send_response(200)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write("request accept".encode())
        else:
         self.send_response(400)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write("bad request".encode())
server = MehraServer(("127.0.0.1",8081),H)
server.serve_forever()
