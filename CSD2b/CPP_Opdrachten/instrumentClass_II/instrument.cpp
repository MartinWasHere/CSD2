#include <iostream>
#include "instrument.h"


Instrument::Instrument(std::string sound, std::string name, std::string type, int pitchLow, int pitchHigh, std::string herrie)
{
  noise=sound;
}

void Instrument::makeSound()
{
    std::cout << noise <<  std::endl;
}
