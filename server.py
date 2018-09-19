from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import cgi

import time

import subprocess

PATH_TO_AUTOHOTKEY = r"C:\Program Files\AutoHotkey\AutoHotkey.exe"

def eval_authotkey(code):
  authotkey_process = subprocess.Popen([PATH_TO_AUTOHOTKEY, "*"],
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
  )
  stdout_value, stderr_value = authotkey_process.communicate(code)

  print(stderr_value)

  return stdout_value

result = eval_authotkey("""
  my_var = hello world
  msgbox % my_var
  
  ; Print to stdout: 2 methods
  ; Method 1
  FileAppend line 1`n, *

  ; Method 2
  stdout := FileOpen("*", "w")
  stdout.WriteLine("line 2")
  stdout.WriteLine("line 3")
""")

print (result)


# Begin Server
class LocalData(object):
  records = {}
 
class HTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if None != re.search('/chrome/youtube/pause', self.path):
      print "pausing youtube"
      ### DO THE STUFF
      ahkString = """
        ControlGet, 0, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
        
        ControlFocus,,ahk_id 0

        IfWinExist, YouTube
        {
          ControlSend, Chrome_RenderWidgetHostHWND1, k , Google Chrome
          return
        }
        Loop {
          IfWinExist, YouTube
            break

          ControlSend, , ^{{PgUp}} , Google Chrome
          sleep 150
        }
        ControlSend, , k , Google Chrome
      """
      eval_authotkey(ahkString)
      ### SEND THE RESPONSE
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()

      # TODO: make this a function
      self.wfile.write("<html><head><title>py-pixel-server</title></head>")
      self.wfile.write("<body>" + 'changing pixels to ' + ','.join(map(str, rgb.split(':'))) + "</body>")
    elif None != re.search('/chrome/youtube/next', self.path):
      self.wfile.write("</html>")
      print "pausing youtube"
      ### DO THE STUFF
      ahkString = """
        
        ControlGet, 0, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
        
        ControlFocus,,ahk_id 0

        IfWinExist, YouTube
        {
          ControlSend, Chrome_RenderWidgetHostHWND1, +n , Google Chrome
          return
        }
        Loop {
          IfWinExist, YouTube
            break

          ControlSend, , ^{{PgUp}} , Google Chrome
          sleep 150
        }
        ControlSend, , +n , Google Chrome
      """
      eval_authotkey(ahkString)
      ### SEND THE RESPONSE
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()

      # TODO: make this a function
      self.wfile.write("<html><head><title>py-pixel-server</title></head>")
      self.wfile.write("<body>" + 'changing pixels to ' + ','.join(map(str, rgb.split(':'))) + "</body>")
      self.wfile.write("</html>")

    return
 
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  allow_reuse_address = True
 
  def shutdown(self):
    self.socket.close()
    HTTPServer.shutdown(self)
 
class SimpleHttpServer():
  def __init__(self, ip, port):
    self.server = ThreadedHTTPServer((ip,port), HTTPRequestHandler)
 
  def start(self):
    self.server_thread = threading.Thread(target=self.server.serve_forever)
    self.server_thread.daemon = True
    self.server_thread.start()
    strip.begin()
    # show a rainbow on server startup
    colorWipe(strip, Color(255, 0, 0))
    colorWipe(strip, Color(0, 255, 0))
    colorWipe(strip, Color(0, 0, 255))
    colorWipe(strip, Color(0,0,0), 10)
    print "strip loaded"
 
  def waitForThread(self):
    self.server_thread.join()
 
  def stop(self):
    self.server.shutdown()
    self.waitForThread()
 
if __name__=='__main__':
  parser = argparse.ArgumentParser(description='HTTP Server')
  parser.add_argument('port', type=int, help='Listening port for HTTP Server')
  parser.add_argument('ip', help='HTTP Server IP')
  args = parser.parse_args()
 
  server = SimpleHttpServer(args.ip, args.port)
  print 'HTTP Server Running...........'
  server.start()
  server.waitForThread()
