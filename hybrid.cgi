#!/bin/sh
printf "Content-Type: text/plain\r\n\r\n"
env

exit 0
#!/usr/bin/env python3

import sys
import os

sys.stdout.write("Content-Type: text/plain\r\n")
sys.stdout.write("\r\n")

QUERY_STRING = os.environ["QUERY_STRING"]
REQUEST_METHOD = os.environ["REQUEST_METHOD"]
CONTENT_TYPE = os.environ["CONTENT_TYPE"]
