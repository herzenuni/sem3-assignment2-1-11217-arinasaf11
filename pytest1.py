import pytest
import nod

def func(a, b, c):
	def test():
		assert nod.nod(a, b) == c
	return test


test1 = func(1, 12, 11)
test2 = func(5, 55, 5)
test3= func(30, 18, 6)
