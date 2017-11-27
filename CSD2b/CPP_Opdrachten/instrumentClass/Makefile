all: main.o instrument.o
				g++ -o instrument main.o instrument.o

instrument.o: instrument.cpp
				g++ -c instrument.cpp

main.o: main.cpp
				g++ -c main.cpp

clean:
				rm -f *.o all
