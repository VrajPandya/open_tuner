#include <iostream>
#include <cstdlib>
#include <Python.h>
#include "open_tuner.h"

using namespace std;

namespace open_tuner{int main(int argc, const char** argv);}

int main(int argc, const char** argv){
    std::string commandArgs ("");
    std::string pythonCommand ("python ");
    // Maybe python3 command is not needed
    std::string python3Command ("python3 ");
    std::string openTunerStr ("open_tuner.py ");

    for (int i = 1; i < argc ; ++i) {
        commandArgs = commandArgs + argv[i];
    }

    std::string commandString = python3Command + openTunerStr +commandArgs;
    std::system(commandString.c_str());

    return 0;
}

