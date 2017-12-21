#Сафиуллина Арина ИВТ 2 курс
#сортировка пузырьком 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr
    
#быстрая сортировка
def quick_sort(arr):
	if arr:
		head, *tail = arr
		return quick_sort([x for x in tail if x <= head]) + \
		[head] + \
		quick_sort([x for x in tail if x > head])
	return []

if __name__ == "__main__":

    import timeit

    print("TIMEIT")
    print("bubble_sort : ", end = '')
    print(timeit.timeit("bubble_sort([5,2,3,4,5,6,8,7,5,122])", setup = "from __main__ import bubble_sort", number = 100))
    print("quick_sort : ", end='')
    print(timeit.timeit("quick_sort([5,2,3,4,5,6,8,7,5,122])", setup="from __main__ import quick_sort", number=100))
