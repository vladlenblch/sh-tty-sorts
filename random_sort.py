import random
import time


def generate_list():
    lst = []
    for i in range(1000):
        lst.append(random.randint(0, 10000))
    return lst


def check_if_sorted(lst):
    global count
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            continue
        else:
            return False
    return True


def one_try(lst):
    global count
    for i in range(len(lst)):
        index1 = random.randint(0, len(lst) - 1)
        index2 = random.randint(0, len(lst) - 1)
        min_index = min(index1, index2)
        max_index = max(index1, index2)

        count += 1
        if lst[min_index] >= lst[max_index]:
            for_swap = lst[min_index]
            lst[min_index] = lst[max_index]
            lst[max_index] = for_swap
    return lst


def random_sort(lst):
    while True:
        if check_if_sorted(lst):
            return lst
        else:
            one_try(lst)


start = time.perf_counter()

new_list = generate_list()
count = 0
print(random_sort(new_list))

end = time.perf_counter()

print(f"время: {end - start}")
print(f"количество сравнений: {count}")
