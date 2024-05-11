#!/usr/bin/env python3

import sys
import os

sys.stdout.write("Content-Type: text/plain\r\n")
sys.stdout.write("\r\n")

import pprint
pprint.pprint(os.environ)
