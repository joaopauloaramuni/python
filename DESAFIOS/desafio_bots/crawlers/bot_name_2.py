import unicodedata

from utils import HttpClient
import urllib3
from datetime import datetime
import json
from bs4 import BeautifulSoup

from sentry_sdk import configure_scope, capture_exception

from crypt import Crypt
from exceptions.search_exceptions import ForbiddenException

urllib3.disable_warnings()

with configure_scope() as scope:
    scope.set_tag("bot", "Bot_name_2")


class Bot_name_2:
    def __init__(self, data: dict):
        # LOGIN
        self.user = Crypt.decrypt(data['user']).decode('utf-8')
        self.password = Crypt.decrypt(data['password']).decode('utf-8')
        
        # URL's
        self.url_base = "https://teste.html"

    def extract(self):
        # EXTRACT
        print("Started - Bot_name_2", flush=True)
        print("Data:", datetime.now().strftime("%d/%m/%Y %H:%M"), flush=True)
        print("URL:", self.url_base, flush=True)

        try:
            client = HttpClient()

            response = client \
                .post(self.url_member) \
                .json({"username": self.user,
                       "password": self.password}) \
                .headers(self.__headersmember) \
                .build()

            print("Status code:", response.status_code, flush=True)

            if response.status_code == 200 and response.json() is not None:
                # EXTRACT
                response = client.get(self.url_base + str("teste")).build()
                extract = ""
                if response.status_code == 200 and response.json() is not None:
                    extract = response.text.replace("\u00a0", "")
                    extract = unicodedata.normalize('NFD', extract).encode('ascii', 'ignore').decode("utf-8")
                    extract = json.loads(extract.encode('utf8'))
                else:
                    print("Unexpected error occurred: {}".format(response.content), flush=True)
                    return None

                # JSON RESPONSE
                data = {
                }
                json_data = json.dumps(data)
                print("\nJSON:", json_data, "\n", flush=True)
                print("Finished - Bot_name_2", flush=True)
                return json_data
            else:
                print("Unexpected error occurred: {}".format(response.content), flush=True)
                raise ForbiddenException("Username or password is incorrect.")
        except Exception as e:
            capture_exception(e)
            print("Exception:", e, flush=True)
            if isinstance(e, ForbiddenException):
                raise e
            return None
