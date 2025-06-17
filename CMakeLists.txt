cmake_minimum_required(VERSION 3.5)
project(stage_troisieme)

find_package(ament_cmake REQUIRED)

install(DIRECTORY bras/launch bras/urdf turtle/bb8 turtle/launch DESTINATION share/${PROJECT_NAME})

install(PROGRAMS bras/move.py DESTINATION lib/${PROJECT_NAME})

file(GLOB bras bras/src/*)
install(PROGRAMS ${bras} DESTINATION lib/${PROJECT_NAME})

file(GLOB turtle turtle/src/*)
install(PROGRAMS ${turtle} DESTINATION lib/${PROJECT_NAME})

ament_package()
