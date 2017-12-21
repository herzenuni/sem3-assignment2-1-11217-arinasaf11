import pytest 
import function_sort

def test_bs():
	res = [31,2,2,5,4,8]
	assert function_sort.bubble_sort(res) == sorted(res)

def test_qs():
	res = [31,2,2,5,4,8]
	assert function_sort.quick_sort(res) == sorted(res)
