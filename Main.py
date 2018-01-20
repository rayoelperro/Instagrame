#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IDE import InstagrameIDE as ide
import sys
import os.path

def ByFile(usernames,passwords):
    if os.path.exists(usernames) and os.path.exists(passwords):
        u = open(usernames, 'r').readlines()
        p = open(usernames, 'r').readlines()
        res = []
        for ui in u:
            for pi in p:
                res.append([ui,pi])
        return res
    print "Ambos archivos no exísten"
    return []

def ByConsole():
    name = raw_input("Usuario: ")
    nok = raw_input("Palabra para finalizar: ")
    a = []
    while True:
        e = raw_input()
        if e != nok:
            a.append(e)
        else:
            break
    return name, a

if __name__ == "__main__":
    if len(sys.argv) == 3:
        t = ByFile(sys.argv[1],sys.argv[2])
        i = ide()
        i.BruteForce(*t)
    else:
        name, passwords = ByConsole()
        i = ide()
        i.BruteForceUser(name,*passwords)
    raw_input()