#include <iostream>
#include "guitar.h"

Guitar::Guitar(std::string sound) : Instrument(sound)
{
  foo=sound;
}

void Guitar::makeSound()
{
    std::cout << foo <<  std::endl;
}

void Guitar::bendString()
{
    std::cout << "bendString()" <<  std::endl;
}
