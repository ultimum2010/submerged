#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca


def run(en_Chewbacca_som_kommer_fra_utsiden):
    global chewie
    chewie = Chewbacca()
    chewie = en_Chewbacca_som_kommer_fra_utsiden
    chewie.beep()