cmake_minimum_required(VERSION 3.3)
project(llvm_project)

# set compiler version
set (CMAKE_C_STANDARD 99)
set (CMAKE_CXX_STANDARD 20)

# find llvm lib
set (LLVM_DIR "" CACHE PATH "path to llvm cmake dir")
find_package(LLVM REQUIRED 14)
llvm_map_components_to_libnames(llvm_all ${LLVM_TARGETS_TO_BUILD} Passes ExecutionEngine MCJIT)

include_directories(${LLVM_INCLUDE_DIRS})

# find source file
file(GLOB source "source/*.cc")

add_executable(${PROJECT_NAME} ${source})

target_link_libraries(${PROJECT_NAME} PUBLIC ${llvm_all})