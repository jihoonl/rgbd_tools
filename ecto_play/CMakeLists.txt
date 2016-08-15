cmake_minimum_required(VERSION 2.8)
# This just defines the name of that project from CMake
project(ecto_play)

# You need ecto, so find it first: that will give you access to macros
find_package(ecto REQUIRED)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/ecto_tutorial)

# This is all you need to know: it will create an ecto module named tutorial
# and it will be built in the ${where_your_Python_lib_are_bult}/ecto_tutorial folder.
# If you add the ``INSTALL`` flag, it will also install it when you do ``make install`
#ectomodule(tutorial DESTINATION ./ecto_tutorial INSTALL
ectomodule(tutorial DESTINATION ${CMAKE_LIBRARY_OUTPUT_DIRECTORY} INSTALL
    # You need a file defining the module (cf. below)
    tutorial.cpp
    # You need a file defining some content for module (cf. below)
    Hello.cpp
    hello.py
)
