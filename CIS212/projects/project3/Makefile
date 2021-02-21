CFLAGS=-w -Wall -g
PROGRAMS=sgrep

all: $(PROGRAMS)

sgrep: sgrep.o
	gcc -o sgrep $^


sgrep.o: sgrep.c

clean:
	rm -f $(PROGRAMS) *.o
