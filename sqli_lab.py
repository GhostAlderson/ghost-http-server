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
        if "id" in params:
         user_id = params["id"][0]
         print ("id in params")
         cursor.execute(" SELECT id FROM users WHERE id =?",
         (user_id,)
         )
         eminem = cursor.fetchone()
         if eminem:
          print ("id already exists")
         else:
          cursor.execute(""" INSERT INTO users
          (username , password) VALUES (? , ?)
          """,("mehra" , "5555"))
          conne.commit()
        else:
         print ("id not in params")
server = MehraServer(("127.0.0.1",8081),H)
server.serve_forever()
