#!/usr/bin/env bash
#run as
case "$1" in
	"0")
		./0-hbtn_status.py | cat -e
		;;
esac
