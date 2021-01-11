#!/usr/bin/env bash
#run as
case "$1" in
	"0")
		./0-hbtn_status.py | cat -e
		;;
	"1")
		./1-hbtn_header.py https://intranet.hbtn.io
		;;
	"2")
		./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
		;;
	"3")
		./3-error_code.py http://0.0.0.0:5000
		./3-error_code.py http://0.0.0.0:5000/status_401
		./3-error_code.py http://0.0.0.0:5000/doesnt_exist
		./3-error_code.py http://0.0.0.0:5000/status_500
		;;
	"4")
		./4-hbtn_status.py | cat -e
		;;
	"5")
		./5-hbtn_header.py https://intranet.hbtn.io
		./5-hbtn_header.py https://intranet.hbtn.io
		;;
	"6")
		./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
		;;
	"7")
		./7-error_code.py http://0.0.0.0:5000
		./7-error_code.py http://0.0.0.0:5000/status_401
		./7-error_code.py http://0.0.0.0:5000/doesnt_exist
		./7-error_code.py http://0.0.0.0:5000/status_500
		;;
	"8")
		./8-json_api.py
		./8-json_api.py a
		./8-json_api.py 2
		./8-json_api.py b
		;;
	"9")
		./10-my_github.py papamuziko cisfun
		./10-my_github.py papamuziko wrong_pwd
		;;
	"10")
		./100-github_commits.py rails rails
		;;
		

esac
