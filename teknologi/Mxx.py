#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca


def run():
    global chewie
    chewie = Chewbacca()
    chewie.beep()