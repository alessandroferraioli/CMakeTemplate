project(Test#project_name# CXX)

enable_testing()

include(GoogleTest)

find_package(GTest REQUIRED)

add_executable(Test#project_name#)

target_sources(Test#project_name#
                PRIVATE
                    main.cpp 
                    Test#project_name#.cpp)
                    
                    
target_link_libraries(Test#project_name# GTest::gtest)


gtest_add_tests(TARGET Test#project_name#)

