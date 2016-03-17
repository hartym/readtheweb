# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

from concurrent.futures import Future


def resolve_future(x):
    if isinstance(x, Future):
        x = x.result()
    return x