#ifndef H_INSTRUMENT
#define H_INSTRUMENT

class Instrument
{
public:
  Instrument(std::string sound, std::string name, std::string type, int pitchLow, int pitchHigh, std::string herrie);
  void makeSound();
private:
  std::string noise;

}; // Instrument{}

#endif // H_INSTRUMENT
