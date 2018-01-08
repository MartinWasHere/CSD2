#ifndef _FLUTE_H_
#define _FLUTE_H_

#include "instrument.h"

class Flute : public Instrument
{
public:
  Flute(std::string sound);
  void pitchBend();
private:

}; // Flute{}

#endif // _Flute_H_
