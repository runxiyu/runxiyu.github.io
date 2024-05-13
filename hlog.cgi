#!/bin/sh

printf 'Content-Type: text/plain\r\n\r\n'

ls -l /srv/hlog/runxiyu.hlog

printf '\n'

cat /srv/hlog/runxiyu.hlog
