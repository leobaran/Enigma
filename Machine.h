#include "Rotor.h"
#include <string>

#ifndef MACHINE_H
#define	MACHINE_H

class Machine {   
    int rotorOneDegree;
    int rotorTwoDegree;
    int rotorThreeDegree;
    
public: 
    Machine();
    std::string getEncodedString(std::string word);
    std::string getDecodedString(std::string codeWord);
    
private:
    //all enigma machines share the same rotors. 
    static Rotor r1;
    static Rotor r2;
    static Rotor r3;
    static Rotor reflector;
};

#endif	

