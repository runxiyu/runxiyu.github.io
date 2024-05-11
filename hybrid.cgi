#!/usr/bin/env python3

import sys
import os

CONTENT_LENGTH = os.environ["CONTENT_LENGTH"]
CONTENT_TYPE = os.environ["CONTENT_TYPE"]
DOCUMENT_ROOT = os.environ["DOCUMENT_ROOT"]
DOCUMENT_URI = os.environ["DOCUMENT_URI"]
FCGI_ROLE = os.environ["FCGI_ROLE"]
GATEWAY_INTERFACE = os.environ["GATEWAY_INTERFACE"]
HTTP_ACCEPT_ENCODING = os.environ["HTTP_ACCEPT_ENCODING"]
HTTP_ACCEPT_LANGUAGE = os.environ["HTTP_ACCEPT_LANGUAGE"]
HTTP_ACCEPT = os.environ["HTTP_ACCEPT"]
HTTP_CONNECTION = os.environ["HTTP_CONNECTION"]
HTTP_HOST = os.environ["HTTP_HOST"]
try:
    HTTP_SEC_FETCH_DEST = os.environ["HTTP_SEC_FETCH_DEST"]
    HTTP_SEC_FETCH_MODE = os.environ["HTTP_SEC_FETCH_MODE"]
    HTTP_SEC_FETCH_SITE = os.environ["HTTP_SEC_FETCH_SITE"]
    HTTP_SEC_FETCH_USER = os.environ["HTTP_SEC_FETCH_USER"]
except KeyError:
    pass
HTTPS = os.environ["HTTPS"]
HTTP_UPGRADE_INSECURE_REQUESTS = os.environ["HTTP_UPGRADE_INSECURE_REQUESTS"]
HTTP_USER_AGENT = os.environ["HTTP_USER_AGENT"]
INVOCATION_ID = os.environ["INVOCATION_ID"]
JOURNAL_STREAM = os.environ["JOURNAL_STREAM"]
LOGNAME = os.environ["LOGNAME"]
PATH_INFO = os.environ["PATH_INFO"]
QUERY_STRING = os.environ["QUERY_STRING"]
REDIRECT_STATUS = os.environ["REDIRECT_STATUS"]
REMOTE_ADDR = os.environ["REMOTE_ADDR"]
REMOTE_PORT = os.environ["REMOTE_PORT"]
REMOTE_USER = os.environ["REMOTE_USER"]
REQUEST_METHOD = os.environ["REQUEST_METHOD"]
REQUEST_SCHEME = os.environ["REQUEST_SCHEME"]
REQUEST_URI = os.environ["REQUEST_URI"]
SCRIPT_FILENAME = os.environ["SCRIPT_FILENAME"]
SCRIPT_NAME = os.environ["SCRIPT_NAME"]
SERVER_ADDR = os.environ["SERVER_ADDR"]
SERVER_NAME = os.environ["SERVER_NAME"]
SERVER_PORT = os.environ["SERVER_PORT"]
SERVER_PROTOCOL = os.environ["SERVER_PROTOCOL"]
SERVER_SOFTWARE = os.environ["SERVER_SOFTWARE"]

if PATH_INFO == "/hybrid/":
    print("Root")
else:
    sys.stdout.write("Status: 404\r\n")
    sys.stdout.write("Content-Type: text/plain\r\n")
    sys.stdout.write("\r\n")
    sys.stdout.write("404 Not Found")
