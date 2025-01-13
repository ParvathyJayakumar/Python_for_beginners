#Write a Python function to insert an element into a sorted list while maintaining the order.

def insert_sorted(lst, x):
    lst.append(x)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

sorted_list = [1, 3, 5, 7]
element = int(input("Enter the element to insert: "))
print(insert_sorted(sorted_list, element))
