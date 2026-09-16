from http.server import BaseHTTPRequestHandler as AHandler , HTTPServer as EServer 
from urllib.parse import urlparse , parse_qs
import base64
class H(AHandler):
    def do_POST(self):
        length = int (self.headers["content-length"])
        body = self.rfile.read(length)
        mehra = body.decode()
        print (length)
        parts = mehra.split("&")
        username = ("")
        password = ("")
        role = ("")
        for part in parts:
         nano = part.split("=")
         if nano[0] == "username":
          username = nano[1]
         elif nano[0] == "password":
          password = nano[1]
         elif nano[0] == "role":
          role = nano[1]
        if (username == "ghost" or username == "alderson") and (password == "1234") and (role == "admin"):
         self.send_response(200)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write("welcome".encode())
         print ("welcome")
        else:
         self.send_response(401)
         self.send_header("content-type" , "text/html")
         self.end_headers()
         self.wfile.write("error".encode())
         print ("error")
    def do_GET(self):
        auth = self.headers["authorization"]
        pim = auth.split(" ")
        eli = base64.b64decode(pim[1])
        decoded = eli.decode()
        now = decoded.split(":")
        if now[0] == "ghost" and now[1] == "1234":
         print (" agree  authorization")
         parsed = urlparse(self.path)
         params = parse_qs(parsed.query)
         if "q" in params:
          print ("agree q")
          query = params["q"][0]
          if query == "python":
           print ("python yes")
           q_ok = True
          else:
           print ("python no")
           q_ok = False
         else:
          print ("no q in params")
          q_ok = False
         if "page" in params:
          print ("agree page") 
          quest = params["page"][0]
          if quest == "2":
           print ("page yes")
           page_ok = True
          else:
           print ("page no")
           page_ok = False
         else:
          print ("no page in params")
          page_ok = False
         if q_ok and page_ok:
          self.send_response(200)
          self.send_header("content-type" , "text/html")
          self.end_headers()
          self.wfile.write("request processed successfully".encode())
        else:
         self.send_response(401)
         self.send_header("content-type" ,"text/html")
         self.end_headers()
         self.wfile.write("no authorization".encode())
         print ("not agree authorization")
server = EServer(("127.0.0.1",8080),H)
server.serve_forever()
        
         
