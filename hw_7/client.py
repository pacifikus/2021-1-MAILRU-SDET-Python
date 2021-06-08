import json
import socket


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.headers = {"Host": f'{host}:{str(port)}'}

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def get(self):
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.client.close()
                break

        total_data = ''.join(total_data).splitlines()
        result = {
            'status_code': int(total_data[0].split(" ")[1]),
            'body': total_data[-1]
        }
        print(result)
        return result

    def request(self, url, method, headers={}, data=None):
        self.connect()
        request = f'{method} {url} HTTP/1.1\r\n'
        data = json.dumps(data)
        self.headers["Content-Length"] = len(data.encode('utf-8'))
        self.headers.update(headers)
        request += '\r\n'.join(f'{key}: {value}'
                               for key, value in self.headers.items())
        request += '\r\n\r\n'
        if data:
            request += data

        self.connect()
        self.client.send(request.encode())
        return self.get()
