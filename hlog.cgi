#!/bin/sh

printf 'Content-Type: text/plain\r\n\r\n'

TZ='Asia/Shanghai' ls --time-style '+%Y-%m-%d %H:%M:%S %Z' -l /srv/hlog/runxiyu.hlog

printf '\n'

cat /srv/hlog/runxiyu.hlog
