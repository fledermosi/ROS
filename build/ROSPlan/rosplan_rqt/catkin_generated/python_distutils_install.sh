#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/georg/rosplan_ws/src/ROSPlan/rosplan_rqt"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/georg/rosplan_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/georg/rosplan_ws/install/lib/python2.7/dist-packages:/home/georg/rosplan_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/georg/rosplan_ws/build" \
    "/usr/bin/python2" \
    "/home/georg/rosplan_ws/src/ROSPlan/rosplan_rqt/setup.py" \
     \
    build --build-base "/home/georg/rosplan_ws/build/ROSPlan/rosplan_rqt" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/georg/rosplan_ws/install" --install-scripts="/home/georg/rosplan_ws/install/bin"
