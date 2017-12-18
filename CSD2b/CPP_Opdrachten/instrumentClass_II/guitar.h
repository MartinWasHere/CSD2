#ifndef _GUITAR_H_
#define _GUITAR_H_

#include "instrument.h"

class Guitar : public Instrument
{
public:
  Guitar(std::string sound);
  void makeSound();
  void bendString();
private:
  std::string foo;

}; // Guitar{}

#endif // _GUITAR_H_
