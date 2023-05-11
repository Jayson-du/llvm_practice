@echo off

set builderDir=%1

cmake -S %builderDir% -B %builderDir%\build -G "Visual Studio 17 2022"  -A x64 -DPLATFORM=Windows -DCMAKE_CONFIGURATION_TYPES=Debug -DLLVM_DIR="C:/Program Files (x86)/LLVM/"

:: pause