#!/usr/bin/env python3
import threading
import os
import time


def pre_thread():
    pre_thread.current_directory = os.getcwd()
    print("Started pre-thread in", pre_thread.current_directory)
    texe = threading.Thread(target=dir_changing_thread)
    texe.start()
    texe.join()
    pre_thread.current_directory = os.getcwd()
    print("Stopped pre-thread in", pre_thread.current_directory)


def dir_changing_thread():
    current_directory = os.getcwd()
    print("Started dir-changing thread in", current_directory)
    os.chdir('..')
    current_directory = os.getcwd()
    print("Changed dir in dir-changing_thread to", current_directory)
    tpost = threading.Thread(target=post_thread)
    tpost.start()


def post_thread():
    post_thread.current_directory = os.getcwd()
    print("Started post-thread in", post_thread.current_directory)
    print("Stopped post-thread")

tpre = threading.Thread(target=pre_thread)
tpre.start()
tpre.start()
