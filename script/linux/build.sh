# echo cmake build llvm_practice x64
path=$1

echo $path

cmake -S $path -B $path/build -G "Ninja" -DCMAKE_CONFIGURATION_TYPES=Debug -DLLVM_DIR="/home/dute/data/apps/llvm_install/"