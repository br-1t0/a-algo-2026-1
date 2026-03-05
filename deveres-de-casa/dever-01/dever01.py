import time as t
import random as r
import matplotlib.pyplot as plt


def insertSort(arr: list):
    for i in range(1, len(arr)):
        back = i
        while back > 0 and arr[back] < arr[back - 1]:
            arr[back - 1], arr[back] = arr[back], arr[back - 1]
            back = back - 1


def generate_lists():
    n = [1000, 5000, 10000, 20000, 50000]
    lists = [[r.randint(1, 2000) for _ in range(size)] for size in n]
    return lists


sizes = [1000, 5000, 10000, 20000, 50000]
sorted_time = []
insertion_time = []

i = 0

for lists in generate_lists():
    start_i = t.perf_counter()
    insertSort(lists.copy())
    end_i = t.perf_counter()
    print(f"Tempo do insertionSort pra tamanho {sizes[i]}: {end_i-start_i} segundos")
    insertion_time.append(end_i - start_i)
    start_s = t.perf_counter()
    sorted(lists.copy())
    end_s = t.perf_counter()
    print(f"Tempo do sorted pra tamanho {sizes[i]} : {end_s-start_s} segundos")
    sorted_time.append(end_s - start_s)
    i = i + 1


i_y = insertion_time
s_y = sorted_time
x = sizes

plt.plot(x, i_y, color="red", label="Insertion sort")
plt.plot(x, s_y, color="blue", label="Sorted")
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.xlabel("n")
plt.ylabel("tempo")
plt.grid(True)
plt.show()
