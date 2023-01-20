#Random sort

import random

#Sort
def random_sort(get_info, list_to_sort):
    while True:
        #Create a copy of the list and convert int to str
        no_sort_list = []
        for i in range(len(list_to_sort)): no_sort_list.append(str(list_to_sort[i]))
        #Randomly insert int into new list
        sort_list = []
        for i in range(len(no_sort_list)):
            len_of_list = len(no_sort_list)
            a = int(random.randint(0, len_of_list - 1))
            sort_list.append(int(no_sort_list[a]))
            no_sort_list.pop(a)
        if get_info == True: print(f"Test {sort_list}")
        #Check if the list is sorted e.g. a <= b
        ok = True
        for i in range(len(sort_list)):
            if (i + 1) == len(sort_list): break
            if sort_list[i] <= sort_list[i+1]: ok = True
            else:
                ok = False
                break
        #If it sorted = True return sorted list else continue the process
        if ok == True: return sort_list
        else: continue
if __name__ == "__main__":
    list_to_sort = [2, 13, 5, 7, 9, 10, 34, 86, 12, 13]
    import time
    start = time.time()
    print(random_sort(get_info=True, list_to_sort=list_to_sort))
    end = time.time()
    print("The time of execution of above program is :",
          (end - start) * 10 ** 3, "ms")