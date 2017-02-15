#include <iostream>
#include <cstdlib>
#include <Python.h>
#include <open-tuner.h>

using namespace std;

int main(int argc, char** argv){
    std::string commandArgs;
    std::string pythonCommand ("python ");
    // Maybe python3 command is not needed
    std::string python3Command ("python3");
    std::string openTunerStr ("open-tuner.py ");

    for (int i = 1; i < argc ; ++i) {
        commandArgs += argv[i];
    }

    std::string commandString = pythonCommand + openTunerStr +commandArgs;
    std::system(commandString.c_str());

    return 0;
}