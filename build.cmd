@echo off
echo cmake build vs2022 x64

if not exist build (
   mkdir build
) 

cd ./build

if exist CMakeCache.txt (
    echo "É¾³ý´æÔÚCMakeCache.txt"
    rm CMakeCache.txt
) 

set builderDir=%~dp0

cmake -S %builderDir% -B %builderDir%\build -G "Visual Studio 16 2019"  -A x64 -DPLATFORM=Windows -DCMAKE_CONFIGURATION_TYPES=Debug -DLLVM_DIR="C:/Program Files (x86)/LLVM/"

pause