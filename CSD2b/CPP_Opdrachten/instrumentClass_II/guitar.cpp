#include <iostream>
#include "guitar.h"

Guitar::Guitar(std::string sound)
{
  foo=sound;
}

void Guitar::makeSound()
{
    std::cout << foo <<  std::endl;
}
