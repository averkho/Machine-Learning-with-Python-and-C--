# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp"

# Include any dependencies generated for this target.
include CMakeFiles/getData.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/getData.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/getData.dir/flags.make

CMakeFiles/getData.dir/apps/getData.cpp.o: CMakeFiles/getData.dir/flags.make
CMakeFiles/getData.dir/apps/getData.cpp.o: apps/getData.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/getData.dir/apps/getData.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/getData.dir/apps/getData.cpp.o -c "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp/apps/getData.cpp"

CMakeFiles/getData.dir/apps/getData.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/getData.dir/apps/getData.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp/apps/getData.cpp" > CMakeFiles/getData.dir/apps/getData.cpp.i

CMakeFiles/getData.dir/apps/getData.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/getData.dir/apps/getData.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp/apps/getData.cpp" -o CMakeFiles/getData.dir/apps/getData.cpp.s

# Object files for target getData
getData_OBJECTS = \
"CMakeFiles/getData.dir/apps/getData.cpp.o"

# External object files for target getData
getData_EXTERNAL_OBJECTS =

libgetData.so: CMakeFiles/getData.dir/apps/getData.cpp.o
libgetData.so: CMakeFiles/getData.dir/build.make
libgetData.so: CMakeFiles/getData.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libgetData.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/getData.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/getData.dir/build: libgetData.so

.PHONY : CMakeFiles/getData.dir/build

CMakeFiles/getData.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/getData.dir/cmake_clean.cmake
.PHONY : CMakeFiles/getData.dir/clean

CMakeFiles/getData.dir/depend:
	cd "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp" "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp" "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp" "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp" "/home/alexander/DataScience/Machine-Learning-with-Python-and-C--/05 - DimensionalityReduction/MDS/cpp/CMakeFiles/getData.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/getData.dir/depend
