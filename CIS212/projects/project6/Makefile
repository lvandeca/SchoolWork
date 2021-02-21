CFLAGS=-g -W -Wall -I/usr/local/include
LDFLAGS=-L/usr/local/lib
LIBRARIES=-lADTs
PROGRAMS=exerciseStack balanceCheck
OBJECTS=exerciseStack.o balanceCheck.o

all: $(PROGRAMS)

exerciseStack: exerciseStack.o
	gcc $(CFLAGS) $(LDFLAGS) -o exerciseStack $^ $(LIBRARIES)

balanceCheck: balanceCheck.o
	gcc $(CFLAGS) $(LDFLAGS) -o balanceCheck $^ $(LIBRARIES)

exerciseStack.o: exerciseStack.c

balanceCheck.o: balanceCheck.c

clean: 
	rm -f $(PROGRAMS) $(OBJECTS)
