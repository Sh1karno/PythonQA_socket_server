class Parser:

    def __init__(self, data):
        self.data = data

    def parse_data(self):
        result_data = ""
        for index, line in enumerate(self.data.split("\n")):
            if index == 0:
                continue
            result_data += f"<div>{line}</div>"
        return result_data

    def get_response(self):
        response = "HTTP/1.1 200 OK\n " \
                   "Content-Length: 100\n " \
                   "Connection: close\n " \
                   "Content-Type: text/html\n\n " \
                   f"{self.parse_data()}"
        return bytes(response, encoding='UTF-8')
