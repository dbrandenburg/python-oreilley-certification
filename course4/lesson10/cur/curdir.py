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
    pre_thread.current_directory_final = os.getcwd()
    if pre_thread.current_directory != pre_thread.current_directory_final:
        print("# Pre_thread stopped in different dir than it was started in #")
    print("Stopped pre-thread in", pre_thread.current_directory_final)


def dir_changing_thread():
    current_directory = os.getcwd()
    print("Started dir-changing thread in", current_directory)
    os.chdir('..')
    current_directory = os.getcwd()
    print("Changed dir in dir-changing_thread to", current_directory)
    tpost = threading.Thread(target=post_thread)
    tpost.start()
    tpost.join()


def post_thread():
    current_directory = os.getcwd()
    print("Started post-thread in", current_directory)
    if current_directory != pre_thread.current_directory:
        print("# Post_thread started in different directory than Pre_thread #")
    print("Stopped post-thread in", current_directory)


tpre = threading.Thread(target=pre_thread)
tpre.start()
