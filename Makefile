p = /mnt/c/Users/gaeta/Documents/SVTR/TP

d:
	docker run --rm -it  -v $(p):/src -w /src ev3cc

compile:
	arm-linux-gnueabi-gcc -o hello hello.c

run:
	qemu-arm-static -L /usr/arm-linux-gnueabi/ ./hello

compile-main:
	arm-linux-gnueabi-gcc -pthread -o main bal.c mdd.c myev3.c time_util.c workers.c communication.c main.c -lev3dev-c -I ev3dev-c/source/ev3 -L ev3dev-c/lib -lm

copy-to-robot:
	scp main robot@ev3dev.local:/home/robot/