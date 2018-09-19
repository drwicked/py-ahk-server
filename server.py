from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import cgi

import time
from neopixel import *

# Begin Server
class LocalData(object):
  records = {}
 
class HTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if None != re.search('/pixel/rgb/*', self.path):
      rgb = self.path.split('/')[-1]
      g = int(rgb.split(':')[0])
      r = int(rgb.split(':')[1])
      b = int(rgb.split(':')[2])
      colorWipe(strip, Color(0,0,0), 10)
      # colorWipe(strip, Color(r, g, b))
      theaterChase(strip, Color(r, g, b), 100)
      print 'changing pixels to ' + ','.join(map(str, rgb.split(':')))
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
