1.Forked the repo and cloned the fork on my local machine.
2.Checked the dependencies and versions for making a compatible environment
3.Gazebo version mismatched, installed the required version 11.10.2
4.Build the workspace.
5.Encountered first bug: 
--- stderr: testbed_description
CMake Error at CMakeLists.txt:24:
  Parse error.  Expected "(", got newline with text "

  ".
6.Added () after ament_package
7.Build successful
8.Ran the bringup launch file. Rviz and Gazebo successfully opened.
9.Create the new package testbed_navigation
10.Made the config and launch directories as they are clearly required as per the provided readme.md
11.Read the map_server plugin doc
12.While reading the testbed_world.yaml file found that the location of map is wrong so I added the absolute path of the map. Now I can try loading the map using map_server plugin directly through terminal as per commands given in the documentation first before making the launch file.