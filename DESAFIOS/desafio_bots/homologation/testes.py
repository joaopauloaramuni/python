from crypt import Crypt

data = [
    {
        "bot": Crypt.encrypt(bytes("Bot_name_1", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_2", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_3", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_4", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_5", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_6", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_7", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_8", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
    {
        "bot": Crypt.encrypt(bytes("Bot_name_9", 'utf-8')),
        "user": Crypt.encrypt(bytes("x@gmail.com", 'utf-8')),
        "password": Crypt.encrypt(bytes("y", 'utf-8'))
    },
]


def get_data():
    return data
