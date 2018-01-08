#include <iostream>
#include "flute.h"

Flute::Flute(std::string sound) : Instrument(sound, "fluit", "blaasInstrument", 50, 120, "Fieeeuwt")
{
}

void Flute::pitchBend()
{
    std::cout << "pitchBend" <<  std::endl;
}
