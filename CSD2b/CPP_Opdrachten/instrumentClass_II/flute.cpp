#include <iostream>
#include "flute.h"

Flute::Flute(std::string sound) : Instrument(sound)
{
  foo=sound;
}

void Flute::makeSound()
{
    std::cout << foo <<  std::endl;
}

void Flute::pitchBend()
{
    std::cout << "pitchBend()" <<  std::endl;
}
