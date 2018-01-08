#include <iostream>
#include "guitar.h"

Guitar::Guitar(std::string sound) : Instrument(sound, "gitaar", "snaarInstrument", 20, 300, "Ploing")
{

}

void Guitar::bendString()
{
    std::cout << "bendString" <<  std::endl;
}
