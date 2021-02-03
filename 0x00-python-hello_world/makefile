CC=gcc
CFLAGS=-g -Wall -Werror -Wextra -pedantic
SRC=$@-*.c ./mains/$@-*.c


10:
	rm -f a.out
	$(CC) $(CFLAGS) $(SRC)
	./a.out
