#include <iostream>
#include "instrument.h"

Instrument::Instrument(std::string sound)
{
  foo=sound;
}

void Instrument::makeSound()
{
    std::cout << foo <<  std::endl;
}
