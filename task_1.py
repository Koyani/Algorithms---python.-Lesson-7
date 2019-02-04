#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
#заданный случайными числами на промежутке [-100; 100). 
#Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. 
#По возможности доработайте алгоритм (сделайте его умнее).
from random import randint
lst = [randint(-100, 99) for i in range(50)]
print(lst)

def bubble_sort(array):
    m = 0
    for j in range(len(array) - 1):
        for i in range(len(array) - j - 1):
            m += 1
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]              
    print(m)
    return array
            
bubble_sort(lst)
print(lst)
            
