# Crawlers - Bots - Guide

### Requirements

* Python 3.7+
* PIP 19.0+

### Setup

Install virtualenvwrapper.

```.bash
# First we need to install mkvirtualenv for environment isolation:
$ sudo -H pip3 install virtualenvwrapper

# Then create our projects folder:
$ mkdir -p ~/dev/projects
$ cd ~/dev/projects

# Then add these three lines to your .bashrc or .zshrc (without the leading #):
# VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.7
# export WORKON_HOME=$HOME/.virtualenvs
# export PROJECT_HOME=$HOME/dev/projects
# source /usr/local/bin/virtualenvwrapper.sh

```

Install required libraries from requirements.txt with pip:

```.bash
$ pip install -r requirements.txt
```

Create a .env file on project's root as below, replacing <> with the respective values.

```.env
ENV=dev
```

### Testing

To test it locally, simply do an http request as below with data.json being the output from manager's project.

```.bash
# Bot list: 
"bot_name_1",
"bot_name_2",
"bot_name_3",
"bot_name_4",
"bot_name_5",
"bot_name_6",
"bot_name_7",
"bot_name_8",
"bot_name_9"

# ENV = DEV
$ http POST localhost:9000/testes --timeout=300 < data.json
{
    
        "bot": Crypt.encrypt(bytes("bot_name", 'utf-8')),
        "user": Crypt.encrypt(bytes("user", 'utf-8')),
        "password": Crypt.encrypt(bytes("senha", 'utf-8'))
}
```
