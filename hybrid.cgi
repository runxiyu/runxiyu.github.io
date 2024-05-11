#!/usr/bin/env python3

import sys
import os
import cgi
import pathlib
import shutil

FBDIR="/srv/fb"

CONTENT_LENGTH = os.environ["CONTENT_LENGTH"]
CONTENT_TYPE = os.environ["CONTENT_TYPE"]
DOCUMENT_ROOT = os.environ["DOCUMENT_ROOT"]
PATH_INFO = os.environ["PATH_INFO"]
DOCUMENT_URI = os.environ["DOCUMENT_URI"]
REQUEST_METHOD = os.environ["REQUEST_METHOD"]

# FCGI_ROLE = os.environ["FCGI_ROLE"]
# GATEWAY_INTERFACE = os.environ["GATEWAY_INTERFACE"]
# HTTP_ACCEPT_ENCODING = os.environ["HTTP_ACCEPT_ENCODING"]
# HTTP_ACCEPT_LANGUAGE = os.environ["HTTP_ACCEPT_LANGUAGE"]
# HTTP_ACCEPT = os.environ["HTTP_ACCEPT"]
# HTTP_CONNECTION = os.environ["HTTP_CONNECTION"]
# HTTP_HOST = os.environ["HTTP_HOST"]
# HTTP_SEC_FETCH_DEST = os.environ["HTTP_SEC_FETCH_DEST"]
# HTTP_SEC_FETCH_MODE = os.environ["HTTP_SEC_FETCH_MODE"]
# HTTP_SEC_FETCH_SITE = os.environ["HTTP_SEC_FETCH_SITE"]
# HTTP_SEC_FETCH_USER = os.environ["HTTP_SEC_FETCH_USER"]
# HTTPS = os.environ["HTTPS"]
# HTTP_UPGRADE_INSECURE_REQUESTS = os.environ["HTTP_UPGRADE_INSECURE_REQUESTS"]
# HTTP_USER_AGENT = os.environ["HTTP_USER_AGENT"]
# INVOCATION_ID = os.environ["INVOCATION_ID"]
# JOURNAL_STREAM = os.environ["JOURNAL_STREAM"]
# QUERY_STRING = os.environ["QUERY_STRING"]
# REDIRECT_STATUS = os.environ["REDIRECT_STATUS"]
# REMOTE_ADDR = os.environ["REMOTE_ADDR"]
# REMOTE_PORT = os.environ["REMOTE_PORT"]
# REMOTE_USER = os.environ["REMOTE_USER"]
# REQUEST_SCHEME = os.environ["REQUEST_SCHEME"]
# REQUEST_URI = os.environ["REQUEST_URI"]
# SCRIPT_FILENAME = os.environ["SCRIPT_FILENAME"]
# SCRIPT_NAME = os.environ["SCRIPT_NAME"]
# SERVER_ADDR = os.environ["SERVER_ADDR"]
# SERVER_NAME = os.environ["SERVER_NAME"]
# SERVER_PORT = os.environ["SERVER_PORT"]
# SERVER_PROTOCOL = os.environ["SERVER_PROTOCOL"]
# SERVER_SOFTWARE = os.environ["SERVER_SOFTWARE"]


def fbw() -> None:
    if not REQUEST_METHOD == "POST":
        sys.stdout.write("Content-Type: text/plain\r\n")
        sys.stdout.write("Status: 400\r\n")
        sys.stdout.write("\r\n")
        sys.stdout.write("This endpoint does not support any method other than POST.")
        exit(0)

    form = cgi.FieldStorage()
    try:
        file = form["file"]
    except KeyError:
        sys.stdout.write("Status: 400\r\n")
        sys.stdout.write("Content-Type: text/plain\r\n")
        sys.stdout.write("\r\n")
        sys.stdout.write("You haven't provided me a file.")
        exit(0)
    if not file.filename:
        sys.stdout.write("Status: 400\r\n")
        sys.stdout.write("Content-Type: text/plain\r\n")
        sys.stdout.write("\r\n")
        sys.stdout.write("File doesn't have a filename... that's strange.")
        exit(0)
    if int(CONTENT_LENGTH) >= 50000:
        sys.stdout.write("Status: 413\r\n")
        sys.stdout.write("Content-Type: text/plain\r\n")
        sys.stdout.write("\r\n")
        sys.stdout.write("Too large!")
        exit(0)
    if shutil.disk_usage("/srv/fb").free < 5*(1024**3):
        sys.stdout.write("Status: 500\r\n")
        sys.stdout.write("Content-Type: text/plain\r\n")
        sys.stdout.write("\r\n")
        sys.stdout.write("I don't have enough space, sorry!")
        exit(0)

    sys.stdout.write("Status: 200\r\n")
    sys.stdout.write("Content-Type: text/plain\r\n")
    sys.stdout.write("\r\n")
    fn = os.path.basename(file.filename)
    open(os.path.join(FBDIR, fn), 'wb').write(file.file.read())
    sys.stdout.write("Done.")
    exit(0)


if PATH_INFO == "/hybrid/":
    sys.stdout.write("Content-Type: text/plain\r\n")
    sys.stdout.write("\r\n")
    print("Okay... so?")
elif PATH_INFO == "/hybrid/fb":
    fbw()
else:
    sys.stdout.write("Content-Type: text/plain\r\n")
    sys.stdout.write("Status: 404\r\n")
    sys.stdout.write("\r\n")
    sys.stdout.write("I don't understand what you're trying to do!")
