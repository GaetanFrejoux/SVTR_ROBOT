p = /mnt/c/Users/gaeta/Documents/SVTR/TP

d:
	docker run --rm -it  -v $(p):/src -w /src ev3cc

compile:
	arm-linux-gnueabi-gcc -o hello hello.c

run:
	qemu-arm-static -L /usr/arm-linux-gnueabi/ ./hello

compile-main:
	arm-linux-gnueabi-gcc -c main.c -lev3dev-c -I ev3dev-c/source/ev3 -L ev3dev-c/lib
