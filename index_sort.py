import random
import time

# works only with lists without repeating elements

def generate_list_without_repeating_elements():
    lst = random.sample(range(10000), 1000)
    return lst


def make_new_arr(lst: list):
    global count
    new_arr = [0] * (max(lst) + 1)
    for elem in lst:
        new_arr[elem] = elem
        count += 1
    return new_arr


def put_away_zero(lst: list):
    global count
    count += len(lst)
    return [elem for elem in make_new_arr(lst) if elem != 0]


start = time.perf_counter()

new_list = generate_list_without_repeating_elements()
count = 0
print(put_away_zero(make_new_arr(new_list)))

end = time.perf_counter()

print(f"время: {end - start}")
print(f"количество сравнений: {count}")
