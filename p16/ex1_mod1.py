#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_tag(tag):
    x = tag

    def get_str(s):
        nonlocal x
        return ": ".join([x, s])
    return get_str
