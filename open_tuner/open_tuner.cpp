#include <iostream>
#include <cstdlib>
#include <Python.h>
#include "open_tuner.h"

using namespace std;

namespace openTuner{int main(int argc, const char** argv);}

int main(int argc, const char** argv){
    std::string commandArgs ("");
    std::string pythonCommand ("python ");
    std::string python3Command ("python3 ");
    std::string openTunerHome ("" + OPEN_TUNER_ROOT);

    std::cout<<openTunerHome;

    std::string openTunerStr ("open_tuner.py ");

    for (int i = 1; i < argc ; ++i) {
        commandArgs = commandArgs + argv[i];
    }

    std::string commandString = python3Command + openTunerStr +commandArgs;
    std::system(commandString.c_str());

    return 0;
}

