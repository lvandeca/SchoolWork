CFLAGS=-g -W -Wall -I/usr/local/include
LDFlags=-L/usr/local/lib
LIBRARIES=-lADTs
PROGRAMS=exerciseQueue

all: $(PROGRAMS)

exerciseQueue: llistqueue.o exerciseQueue.o
	gcc $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LIBRARIES)

llistqueue.o: llistqueue.c
exerciseQueue.o: exerciseQueue.c 

clean:
	rm -f *.o $(PROGRAMS)
