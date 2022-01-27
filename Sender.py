import requests

class Sender:
    url = "http://127.0.0.1:5000"

    def __init__(self):
        pass

    def send_data(self,data = ""):
        requests.post(url = self.url,data = data.encode("utf-8"))
