#include <iostream>
#include "instrument.h"
#include "guitar.h"

// Include guards

int main()
{
  Guitar dingetje("dingetje");
  dingetje.makeSound();
  dingetje.bendString();
}
