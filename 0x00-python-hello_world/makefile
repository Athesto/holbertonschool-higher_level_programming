CC=gcc
CFLAGS=-g -Wall -Werror -Wextra -pedantic
SRC=$@-*.c ./mains/$@-*.c

default:
	@echo "run: make <file-number>"

%:
	./$@-*.py
	echo "hello"

0 1:
	./$@-*
0: export PYFILE=./mains/main.py
1: export PYCODE='print("Holberton School: {}".format(88+10))'

10:
	rm -f a.out
	$(CC) $(CFLAGS) $(SRC)
	@betty-style $(SRC)
	@betty-doc $(SRC) 1> /dev/null
	./a.out

101:
	python -c "import dis; dis.dis(__import__('102-magic_calculation'))"
