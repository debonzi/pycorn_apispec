from wsgiref.simple_server import make_server

from tests.simpleserver.main import main


server = make_server("0.0.0.0", 6543, main())
server.serve_forever()
