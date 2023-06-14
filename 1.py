#!/usr/bin/python
import requests

a = input("Create File and  save. File Name: ")

b = input("Target(https://example.com/)")

x = requests.get(b)


open(a, "wb").write(x.content)
