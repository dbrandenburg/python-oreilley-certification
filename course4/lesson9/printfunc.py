#!/usr/bin/env python3
import argparse
import inspect
from pprint import pprint

argparse_inspection = inspect.getmembers(argparse, inspect.isfunction)
for f in argparse_inspection:
    argparse_function_name = f[0]
    argparse_function = inspect.formatargspec(*inspect.getfullargspec(f[1]))
    print('def ' + argparse_function_name + argparse_function)
