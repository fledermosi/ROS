execute_process(COMMAND "/home/lukas/catkin_ws/build/ROSPlan/rosplan_action_interface/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/lukas/catkin_ws/build/ROSPlan/rosplan_action_interface/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
