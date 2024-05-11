#!/bin/sh

printf 'Content-Type: text/html\r\n'
printf '\r\n'
printf '%s\r\n' "$PATH_INFO"
