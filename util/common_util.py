#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Time: 2019/1/11 10:28
__author__ = 'Peter.Fang'

import platform


def debug_mode(mode):
    if mode == 'auto':
        return True if platform.system() == 'Windows' else False
    return mode
