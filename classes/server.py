import http.server
import socketserver
import util.apiKeys
import util.handleErr
import util.parseUrl
import util.verifyRoutes
import util.loadConf
import exeptions.badAuth
import exeptions.clientErr
import exeptions.compErr
import json

class server:
    def __init__(self, apiPaths, confPath):
        util.verifyRoutes.checkRoutes(apiPaths)
        self.paths = apiPaths
        refServer = self
        self.state = {}
        self.keys = None
        self.removedKeys = []
        self.newKeyCode = None
        
        if confPath != "":
            self.conf = util.loadConf.load_utility_file(confPath)
            if list(self.conf.keys()).__contains__("keys"):
                if self.conf["keys"]:
                    self.keys = []
            if list(self.conf.keys()).__contains__("password"):
                self.password = self.conf["password"]
                if self.keys is not None:
                    self.newKeyCode = self.password
            else:
                self.password = None
                if self.keys is not None:
                    baseKey = util.apiKeys.generate_api_key()
                    self.keys.append(baseKey)
                    self.newKeyCode = baseKey
                    print(f"Base API Key for inital setup: {baseKey}")
            if list(self.conf.keys()).__contains__("port"):
                self.port = self.conf["port"]
            else:
                self.port = 80
        else:
            self.password = None
            self.port = 80

        class reqHandler(http.server.BaseHTTPRequestHandler):
            # Override the do_GET method to handle GET requests along with all other methods 
            def do_GET(self):
                self.runAndCatchAll(self, "GET", refServer.state)
            def do_POST(self):
                self.runAndCatchAll(self, "POST", refServer.state)
            def do_PUT(self):
                self.runAndCatchAll(self, "PUT", refServer.state)
            def do_DELETE(self):
                self.runAndCatchAll(self, "DELETE", refServer.state)

            def runAndCatchAll(self, externalSelf, type, state):
                try:
                    self.runApi(externalSelf, type, state)
                except Exception:
                    httpCode = 500
                    content = util.handleErr.handleErr(500, Exception)[2].encode("utf-8")
                    self.send_response(httpCode)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(content)
                    return
                
            def runApi(self, externalSelf, type, state):
                httpCode = 200
                content = "{}"
                path, prams = util.parseUrl.parseUrlData(externalSelf.path)

                validKey = False
                adminKey = False

                if refServer.password is not None or refServer.keys is not None:
                    if list(prams.keys()).__contains__("auth"):
                        if prams['auth'] == refServer.newKeyCode and path[:4] == '/../':
                            validKey = True
                            adminKey = True
                    if list(prams.keys()).__contains__("password"):
                        if refServer.password != (prams["password"]):
                            validKey = True
                        else:
                            httpCode = 403
                            content = util.handleErr.handleErr(403, exeptions.badAuth.authErr("Bad Password"))[2].encode("utf-8")
                            self.send_response(httpCode)
                            self.send_header('Content-type', 'application/json')
                            self.end_headers()
                            self.wfile.write(content)
                            return
                    if list(prams.keys()).__contains__("key"):
                        if refServer.keys != None:
                            if ((refServer.keys.__contains__(prams["key"])) and not (prams["key"] in refServer.removedKeys)):
                                validKey = True
                            else:
                                httpCode = 403
                                content = util.handleErr.handleErr(403,, exeptions.badAuth.authErr("Bad Key"))[2].encode("utf-8")
                                self.send_response(httpCode)
                                self.send_header('Content-type', 'application/json')
                                self.end_headers()
                                self.wfile.write(content)
                                return
                try:
                    if adminKey:
                        try:
                            if path == "/../newKey":
                                if refServer.keys != None:
                                    if prams["auth"] == refServer.newKeyCode:
                                        httpCode = 200
                                        newKey = util.apiKeys.generate_api_key()
                                        refServer.keys.append(newKey)
        
                                        # this is the only way i could get it to work so don't ask me why
                                        content = f'{"{"}"New Key":"{newKey}"{"}"}'.encode("utf-8")
                                        
                                        self.send_response(httpCode)
                                        self.send_header('Content-type', 'application/json')
                                        self.end_headers()
                                        self.wfile.write(content)
                                        validKey = False
                                        return
                            elif path == "/../keys":
                                if refServer.keys != None:
                                    if prams["auth"] == refServer.newKeyCode:
                                        httpCode = 200
                                        content = f'{"{"}"Keys":"{refServer.keys}"{"}"}'.encode("utf-8")
                                        self.send_response(httpCode)
                                        self.send_header('Content-type', 'application/json')
                                        self.end_headers()
                                        self.wfile.write(content)
                                        validKey = False
                                        return
                            elif path == "/../delKey":
                                if refServer.keys != None:
                                    if prams["auth"] == refServer.newKeyCode:
                                        if prams["del"] in refServer.keys:
                                            httpCode = 200
                                            newKeyList =[]
                                            for i in refServer.keys:
                                                if i != prams["del"]:
                                                    newKeyList.append(i)
                                            refServer.keys = newKeyList
                                            refServer.removedKeys.append(prams["del"])
                                            content = f'{"{"}"Done":true{"}"}'.encode("utf-8")
                                            self.send_response(httpCode)
                                            self.send_header('Content-type', 'application/json')
                                            self.end_headers()
                                            self.wfile.write(content)
                                            validKey = False
                                            return
                                        else:
                                            raise Exception()
                        except Exception:
                            httpCode = 500
                            content = util.handleErr.handleErr(500, Exception)[2].encode("utf-8")
                            self.send_response(httpCode)
                            self.send_header('Content-type', 'application/json')
                            self.end_headers()
                            self.wfile.write(content)
                            validKey = False
                            return
                    else:
                        compPath = refServer.paths[path[1:]]
                except:
                    httpCode = 404
                    content = util.handleErr.handleErr(404, exeptions.clientErr.clientErr("File Requested not found"))[2].encode("utf-8")
                    self.send_response(httpCode)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(content)
                    validKey = False
                    return
                
                try:
                    httpCode = 200
                    content = json.dumps(
                        compPath.route.execute(
                            prams, type, state, externalSelf
                        )
                    ).encode("utf-8")
                except Exception:
                    httpCode = 500
                    content = util.handleErr.handleErr(500, Exception)[2].encode("utf-8")
                    self.send_response(httpCode)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(content)
                    validKey = False
                    return
                self.send_response(httpCode)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(content)

        self.handleReq = reqHandler

    def setCustomHandler(self, handler):
        self.handleReq = handler

    def run(self):
        self.server = socketserver.TCPServer(("", self.port), self.handleReq)

        print(f"Server running on port {self.port}")
        self.server.serve_forever()
