# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.21

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\msys64\mingw64\bin\cmake.exe

# The command to remove a file.
RM = C:\msys64\mingw64\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example"

# Include any dependencies generated for this target.
include CMakeFiles/read_data.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/read_data.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/read_data.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/read_data.dir/flags.make

CMakeFiles/read_data.dir/apps/read_data.cpp.obj: CMakeFiles/read_data.dir/flags.make
CMakeFiles/read_data.dir/apps/read_data.cpp.obj: CMakeFiles/read_data.dir/includes_CXX.rsp
CMakeFiles/read_data.dir/apps/read_data.cpp.obj: apps/read_data.cpp
CMakeFiles/read_data.dir/apps/read_data.cpp.obj: CMakeFiles/read_data.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/read_data.dir/apps/read_data.cpp.obj"
	C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/read_data.dir/apps/read_data.cpp.obj -MF CMakeFiles\read_data.dir\apps\read_data.cpp.obj.d -o CMakeFiles\read_data.dir\apps\read_data.cpp.obj -c "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example\apps\read_data.cpp"

CMakeFiles/read_data.dir/apps/read_data.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/read_data.dir/apps/read_data.cpp.i"
	C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example\apps\read_data.cpp" > CMakeFiles\read_data.dir\apps\read_data.cpp.i

CMakeFiles/read_data.dir/apps/read_data.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/read_data.dir/apps/read_data.cpp.s"
	C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example\apps\read_data.cpp" -o CMakeFiles\read_data.dir\apps\read_data.cpp.s

# Object files for target read_data
read_data_OBJECTS = \
"CMakeFiles/read_data.dir/apps/read_data.cpp.obj"

# External object files for target read_data
read_data_EXTERNAL_OBJECTS =

libread_data.dll: CMakeFiles/read_data.dir/apps/read_data.cpp.obj
libread_data.dll: CMakeFiles/read_data.dir/build.make
libread_data.dll: CMakeFiles/read_data.dir/linklibs.rsp
libread_data.dll: CMakeFiles/read_data.dir/objects1.rsp
libread_data.dll: CMakeFiles/read_data.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libread_data.dll"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\read_data.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/read_data.dir/build: libread_data.dll
.PHONY : CMakeFiles/read_data.dir/build

CMakeFiles/read_data.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\read_data.dir\cmake_clean.cmake
.PHONY : CMakeFiles/read_data.dir/clean

CMakeFiles/read_data.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\03- Cpp perceptron toy example\CMakeFiles\read_data.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/read_data.dir/depend

