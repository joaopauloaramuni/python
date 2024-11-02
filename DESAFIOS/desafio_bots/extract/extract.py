import os

from crawlers.bot_name_1 import Bot_name_1
from crawlers.bot_name_2 import Bot_name_2
from crawlers.bot_name_3 import Bot_name_3
from crawlers.bot_name_4 import Bot_name_4
from crawlers.bot_name_5 import Bot_name_5
from crawlers.bot_name_6 import Bot_name_6
from crawlers.bot_name_7 import Bot_name_7
from crawlers.bot_name_8 import Bot_name_8
from crawlers.bot_name_9 import Bot_name_9
from crypt import Crypt
from sentry_sdk import capture_exception, configure_scope
from dotenv import load_dotenv
from exceptions.search_exceptions import InvalidBotException

load_dotenv()
env = os.getenv("ENV")

with configure_scope() as scope:
    scope.set_tag("bot", "extract_client")


class ExtractClient:
    def __init__(self):
        self.env = os.getenv("ENV", "PROD")
        self.__bots = {
            "Bot_name_1",
            "Bot_name_2",
            "Bot_name_3",
            "Bot_name_4",
            "Bot_name_5",
            "Bot_name_6",
            "Bot_name_7",
            "Bot_name_8",
            "Bot_name_9"
        }

    def extract(self, data: dict = None):
        """
        Search bot
        :param data:
        :return: json
        """
        response = []

        if env == "DEV":
            for i in data:
                result = self.search_bot(i)
                response.append(result)

            return {"content": response}
        else:
            return self.search_bot(data)

    def search_bot(self, i):
        bot = Crypt.decrypt(i['bot']).decode('utf-8')
        print('\nBot:', bot, flush=True)
        result = None
        success = False
        retries = 1
        while not success and retries <= 3:
            if bot in self.__bots:
                if bot == "Bot_name_1":
                    result = Bot_name_1(data=i).extract()
                elif bot == "Bot_name_2":
                    result = Bot_name_2(data=i).extract()
                elif bot == "Bot_name_3":
                    result = Bot_name_3(data=i).extract()
                elif bot == "Bot_name_4":
                    result = Bot_name_4(data=i).extract()
                elif bot == "Bot_name_5":
                    result = Bot_name_5(data=i).extract()
                elif bot == "Bot_name_6":
                    result = Bot_name_6(data=i).extract()
                elif bot == "Bot_name_7":
                    result = Bot_name_7(data=i).extract()
                elif bot == "Bot_name_8":
                    result = Bot_name_8(data=i).extract()
                elif bot == "Bot_name_9":
                    result = Bot_name_9(data=i).extract()
            else:
                print("BOT inexistente na lista de BOTs: ", flush=True)
                msg = "Bot not found: {}".format(bot)
                capture_exception(InvalidBotException(msg))
                raise InvalidBotException(msg)

            if result is None:
                print("\nErro na tentativa: " + str(retries) + " de 3...\n", flush=True)
                retries += 1
            else:
                success = True

        return result
