#!/usr/local/bin/python3

import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=UTF-8\n\n")

f=open("test.txt")
html=f.read()
f.close()

print(html)
