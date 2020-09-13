flags=-g -Wall -Werror -Wextra -pedantic
main:
	gcc $(flags) -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c

13:
	betty 13-is_palindrome.c test/*.c
	gcc $(flags) test/*.c 13-*.c
	./a.out

