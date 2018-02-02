#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ide import InstagrameIDE as ide
import sys
import os.path

def ByFile(usernames,passwords):
    if os.path.exists(usernames) and os.path.exists(passwords):
        u = open(usernames, 'r').readlines()
        p = open(passwords, 'r').readlines()
        res = []
        for ui in u:
            if ui[len(ui)-1] == "\n":
                ui = ui[:-1]
            for pi in p:
                if pi[len(pi) - 1] == "\n":
                    pi = pi[:-1]
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