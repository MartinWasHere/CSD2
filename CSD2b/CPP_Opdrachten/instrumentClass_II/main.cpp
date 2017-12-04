#include <iostream>
#include "instrument.h"
#include "guitar.h"

// Include guards

int main()
{
  Instrument cello("Rattataaaa");
  cello.makeSound();

  Guitar dingetje("dingetje");
  dingetje.makeSound();
  dingetje.bendString();
}
