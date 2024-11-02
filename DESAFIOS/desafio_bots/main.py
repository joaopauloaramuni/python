import os
import json
from time import time
from colorama import Fore, Back
import jwt
from flask import Flask, jsonify, request, abort
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
from flask.cli import load_dotenv
from extract.extract import ExtractClient
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from exceptions.search_exceptions import GeneralSearchException, ForbiddenException, InvalidBotException

# START - Setup
app = Flask(__name__)
load_dotenv()
port = os.getenv("SV_PORT", 9000)
env = os.getenv("ENV", "PROD")

# JWT
secret = os.getenv("secret")

tokenfixo = "id_teste"

# CONFIG
app.config["JWT_SECRET_KEY"] = secret
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_COOKIE_PATH"] = "/"
app.config["JWT_REFRESH_COOKIE_PATH"] = "/refresh"
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
jwtmanager = JWTManager(app)
# END - Setup

# Log de erros
if env == "PROD":
    sentry_sdk.init(
        "http://id@sentry.teste.cloud/",
        integrations=[FlaskIntegration()]
    )
    with sentry_sdk.configure_scope() as scope:
        scope.set_tag("bot", "server")


@app.route("/", methods=["GET"])
def index():
    return "id_teste"


@app.route("/testes", methods=["GET"])
def testes_dev():
    if env == "DEV":
        __extract()
    return "OK"

@app.route("/auth", methods=["GET"])
def create_token():
    # https://flask-jwt-extended.readthedocs.io/en/stable/api/
    # https://flask-jwt-extended.readthedocs.io/en/stable/tokens_in_cookies/
    # https://flask-jwt-extended.readthedocs.io/en/stable/refresh_tokens/
    # https://readthedocs.org/projects/flask-jwt-extended/downloads/pdf/stable/

    print("Auth\n", flush=True)
    print("Criando token nos cookies...", flush=True)

    if env != "DEV":
        headerauth = request.headers.get("Authorization")
        if headerauth != tokenfixo:
            return jsonify({"token": False}), 401

    access = create_access_token(identity=secret)
    refresh = create_refresh_token(identity=secret)

    resp = jsonify({"token": True})
    set_access_cookies(resp, access)
    set_refresh_cookies(resp, refresh)

    print("Token criado.", flush=True)

    return resp, 200


@app.route("/refresh", methods=["GET"])
@jwt_refresh_token_required
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    resp = jsonify({"refresh": True})
    set_access_cookies(resp, access_token)
    return resp, 200


@app.route("/remove", methods=["GET"])
def remove_token():
    resp = jsonify({"token": False})
    unset_jwt_cookies(resp)
    return resp, 200


@app.route("/extract", methods=["POST"])
@jwt_required
def extract():
    # Old auth
    # result = True
    # if env == "DEV":
    # headerauth = request.headers.get("Authorization")
    # result = __validatoken(headerauth)
    # if result:

    # Extract
    extracao = __extract()
    return extracao

    # else:
    # return "Erro de autenticação."


def __extract():

    if env == "PROD":
        # DATA PROD
        content = request.json
        data = json.loads(content) if not isinstance(content, dict) else content
    else:
        from homologation.testes import get_data
        # DATA DEV
        data = get_data()

    if data is None:
        raise GeneralSearchException("Bad params: '{}'".format(data))
    else:
        print("\nReceived request for {}".format(data), flush=True)

    # Console destacado
    print(Back.LIGHTWHITE_EX, flush=True)
    print(Fore.LIGHTCYAN_EX, flush=True)

    print_spider()
    print("Extract Started ********************************", flush=True)
    print("************************************************", flush=True)

    result = None
    try:
        client = ExtractClient()
        result = client.extract(data)
        print("\nResultado:", result, flush=True)
    # Bot inválido:
    except InvalidBotException as e:
        return abort(404, e)
    # Usuário ou senha inválidos:
    except ForbiddenException as e:
        return abort(403, e)

    print("\n************************************************", flush=True)
    print("Extract Finished *******************************", flush=True)
    print("************************************************\n", flush=True)

    return result


def print_spider():
    print("************** CRAWLERS HOTMILHAS **************", flush=True)
    print("************************************************", flush=True)
    print("""             ;               ,              """, flush=True)
    print("""           ,;                 '.            """, flush=True)
    print("""          ;:                   :;           """, flush=True)
    print("""         ::                     ::          """, flush=True)
    print("""         ::                     ::          """, flush=True)
    print("""         ':                     :           """, flush=True)
    print("""          :.                    :           """, flush=True)
    print("""       ;' ::                   ::  '        """, flush=True)
    print("""      .'  ';                   ;'  '.       """, flush=True)
    print("""     ::    :;                 ;:    ::      """, flush=True)
    print("""     ;      :;.             ,;:     ::      """, flush=True)
    print("""     :;      :;:           ,;"      ::      """, flush=True)
    print("""     ::.      ':;  ..,.;  ;:'     ,.;:      """, flush=True)
    print("""      "'"...   '::,::::: ;:   .;.;""'       """, flush=True)
    print("""          '""'....;:::::;, ;.;'""           """, flush=True)
    print("""      .:::.....'"':::::::'",...;::::;.      """, flush=True)
    print("""     ;:' '""'"";.,;:::::;.'""""""  ':;      """, flush=True)
    print("""    ::'         ;::;:::;::..         :;     """, flush=True)
    print("""   ::         ,;:::::::::::;:..       ::    """, flush=True)
    print("""   ;'     ,;;:;::::::::::::::;";..    ':.   """, flush=True)
    print("""  ::     ;:"  ::::::''''::::::  ":     ::   """, flush=True)
    print("""   :.    ::   :::::: :: ::::::   :     ;    """, flush=True)
    print("""    ;    ::   :::::: :: ::::::   :    ;     """, flush=True)
    print("""     '   ::   ::::::....:::::'  ,:   '      """, flush=True)
    print("""      '  ::    :::::::::::::"   ::          """, flush=True)
    print("""         ::     ':::::::::"'    ::          """, flush=True)
    print("""         ':       """""""'      ::          """, flush=True)
    print("""          ::                   ;:           """, flush=True)
    print("""          ':;                 ;:"           """, flush=True)
    print("""            ';              ,;'             """, flush=True)
    print("""              "'           '"               """, flush=True)
    print("""                '                           """, flush=True)
    print("************************************************", flush=True)


# DEPRECATED
# @app.route("/auth", methods=["GET"])
def auth():
    headerauth = request.headers.get("Authorization")
    now = int(time())
    if headerauth is not None:
        if headerauth == tokenfixo:
            options = {"verify_aud": False, "require_sub": True}
            payload = {
                'iss': 'teste',
                'iat': now,
                'exp': now + 3600
            }
            return jwt.encode(payload, secret, algorithm='HS256', options=options)
        else:
            msg = "Token inválido."
            print(msg, flush=True)
            return msg
    else:
        msg = "Authorization header vazio."
        print(msg, flush=True)
        return msg


# DEPRECATED
# @app.route("/verify", methods=["GET"])
def verify():
    headerauth = request.headers.get("Authorization")
    result = __validatoken(headerauth)
    if result:
        return "OK"
    else:
        return "Erro de autenticação."


# DEPRECATED
def __validatoken(headerauth):
    if headerauth is not None:
        print("Validando token de autenticação...", flush=True)
        try:
            options = {"verify_aud": False, "require_sub": True}
            payload = jwt.decode(headerauth, secret, algorithms=["HS256"], options=options)
            print("\nToken válido.", flush=True)
            print(payload, flush=True)
            return True
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            print("\nToken inválido.", flush=True)
            return False
    else:
        msg = "Authorization header vazio."
        print(msg, flush=True)
        return False


app.run(host="0.0.0.0", port=port, threaded=True, debug=True)
