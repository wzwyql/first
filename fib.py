#!/usr/bin/env python3
# coding:utf-8

def fib(max):
	n,a,b,c = 0,0,1,1
	while n < max:
		yield c
		c = a + b
		a = b
		b = c
		n += 1
# for i in fib(1):
# 	print(i)


def tri(m):
	L = [1]
	n = 0
	while n < m:
		yield L
#		print(L)
		L = [1] + [ L[n] + L[n+1] for n in range(len(L)-1)] + [1]
		n += 1


for a in tri(5):
	print(a)
#tri(5)

