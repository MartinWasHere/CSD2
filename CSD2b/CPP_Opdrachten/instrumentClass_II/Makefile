all: main.o instrument.o guitar.o flute.o
				g++ -o instrument main.o instrument.o guitar.o flute.o

instrument.o: instrument.cpp
				g++ -c instrument.cpp

guitar.o:	guitar.cpp
				g++ -c guitar.cpp

flute.o:	flute.cpp
				g++ -c flute.cpp

main.o: main.cpp
				g++ -c main.cpp

clean:
				rm *.o instrument
