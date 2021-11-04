#==================== file A ==================
from  urllib.request import urlopen
url_file = urlopen("http://localhost:8000")
print(url_file.geturl())
print(url_file.info())
for line in url_file.readlines():
    print(line.decode("utf8"))

#=====================file B====================

from  http.server import SimpleHTTPRequestHandler ,HTTPServer

server= HTTPServer(("",8000),SimpleHTTPRequestHandler)
server.serve_forever()

#====================== wsgi server ==================
# from wsgiref.simple_server import make_server

# def hello_world_app(environ,start_response):
#     status = b"200 OK"
#     headers = [(b'Content-type',b'text/plain; charset=utf-8')]
#     start_response(status,headers)
#     return [b"Hello World"]

# httpd = make_server("",9000,hello_world_app)
# print("Serving on port 9000")
# httpd.serve_forever()


#===================== Message WALL =====================

from  sqlite3 import connect,PARSE_DECLTYPES,PARSE_COLNAMES
from wsgiref.simple_server import make_server
from io import StringIO
import sqlite3
import datetime

conn =  connect("messagefile",detect_types=PARSE_DECLTYPES | PARSE_COLNAMES)
cursor = conn.cursor()
cursor.execute("create table messages(user text,message text,ts timestamp)")
conn.commit()
conn.close()

def get_form_vals(post_str):
    forms_vals = {item.split("=")[0]:item.split("=")[1] for item in post_str.decode().split("&")}
    return forms_vals

def message_wall_app(environ,start_response):
    output =StringIO
    status = b"200 OK"
    headers = [(b'Content-type',b'text/html; charset=utf-8')]
    start_response(status,headers)
    print("<h1>Message Wall</h1>",file=output)
    if environ["REQUEST_METHOD"]=="POST":
        size = int(environ["CONTENT_LENGTH"])
        post_str = environ["wsgi.input"].read(size)
        form_vals  = get_form_vals(post_str)
        form_vals["timestamp"]=datetime.datetime.now()
        print(post_str,"<p>",file=output)
        cursor.execute("insert into messages (user,message,ts) values (:user,:message,:timestamp)",form_vals)
        print(
            "<form method='POST'>"+
            "User: <input type='text' name='user' />"  +
            "Message: <input type='text' name='message' />"+
            "<input type='submit' value='Send'/>"+
            "</form>",file=output
        )
        return [output.getvalue()]


httpd = make_server("",9000,message_wall_app)
print("Serving on port 9000")
httpd.serve_forever()