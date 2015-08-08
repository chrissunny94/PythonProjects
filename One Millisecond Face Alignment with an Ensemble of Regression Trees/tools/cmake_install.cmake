# Install script for directory: /home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF(EXISTS "$ENV{DESTDIR}/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so")
    FILE(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so"
         RPATH "")
  ENDIF()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so")
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
FILE(INSTALL DESTINATION "/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples" TYPE SHARED_LIBRARY FILES "/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/dlib.so")
  IF(EXISTS "$ENV{DESTDIR}/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so")
    IF(CMAKE_INSTALL_DO_STRIP)
      EXECUTE_PROCESS(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/python/../../python_examples/dlib.so")
    ENDIF(CMAKE_INSTALL_DO_STRIP)
  ENDIF()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  INCLUDE("/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/dlib_build/cmake_install.cmake")

ENDIF(NOT CMAKE_INSTALL_LOCAL_ONLY)

IF(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
ELSE(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
ENDIF(CMAKE_INSTALL_COMPONENT)

FILE(WRITE "/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/${CMAKE_INSTALL_MANIFEST}" "")
FOREACH(file ${CMAKE_INSTALL_MANIFEST_FILES})
  FILE(APPEND "/home/stuxnet/Desktop/projecthumeur/One Millisecond Face Alignment with an Ensemble of Regression Trees/tools/${CMAKE_INSTALL_MANIFEST}" "${file}\n")
ENDFOREACH(file)
