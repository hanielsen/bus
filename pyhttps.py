from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

#context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context = ssl.create_default_context(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('c:/users/holger/ssl/han.crt','c:/users/holger/ssl/han.key')

httpd = HTTPServer(('192.168.87.109', 4443), SimpleHTTPRequestHandler)

httpd.socket = context.wrap_socket(httpd.socket, server_side=True, do_handshake_on_connect=False)

httpd.serve_forever()