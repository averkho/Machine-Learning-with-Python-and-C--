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
CMAKE_SOURCE_DIR = "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\build"

# Include any dependencies generated for this target.
include CMakeFiles/preprocessing.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/preprocessing.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/preprocessing.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/preprocessing.dir/flags.make

CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj: CMakeFiles/preprocessing.dir/flags.make
CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj: CMakeFiles/preprocessing.dir/includes_CXX.rsp
CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj: ../apps/preprocessing.cpp
CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj: CMakeFiles/preprocessing.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\build\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj"
	C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj -MF CMakeFiles\preprocessing.dir\apps\preprocessing.cpp.obj.d -o CMakeFiles\preprocessing.dir\apps\preprocessing.cpp.obj -c "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\apps\preprocessing.cpp"

CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.i"
	C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\apps\preprocessing.cpp" > CMakeFiles\preprocessing.dir\apps\preprocessing.cpp.i

CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.s"
	C:\msys64\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\apps\preprocessing.cpp" -o CMakeFiles\preprocessing.dir\apps\preprocessing.cpp.s

# Object files for target preprocessing
preprocessing_OBJECTS = \
"CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj"

# External object files for target preprocessing
preprocessing_EXTERNAL_OBJECTS =

libpreprocessing.dll: CMakeFiles/preprocessing.dir/apps/preprocessing.cpp.obj
libpreprocessing.dll: CMakeFiles/preprocessing.dir/build.make
libpreprocessing.dll: CMakeFiles/preprocessing.dir/linklibs.rsp
libpreprocessing.dll: CMakeFiles/preprocessing.dir/objects1.rsp
libpreprocessing.dll: CMakeFiles/preprocessing.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\build\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libpreprocessing.dll"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\preprocessing.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/preprocessing.dir/build: libpreprocessing.dll
.PHONY : CMakeFiles/preprocessing.dir/build

CMakeFiles/preprocessing.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\preprocessing.dir\cmake_clean.cmake
.PHONY : CMakeFiles/preprocessing.dir/clean

CMakeFiles/preprocessing.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\build" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\build" "C:\01 - DEVELOPMENT\03 - Online course\03 - Machine Learning with Python\00 - GitHub\Machine-Learning-with-Python-and-C--\01 - Perceptron\02 - Cpp\build\CMakeFiles\preprocessing.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/preprocessing.dir/depend

