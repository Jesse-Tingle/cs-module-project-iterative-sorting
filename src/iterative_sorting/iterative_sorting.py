# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Set swap_counter to non-zero value
    swap_counter = -1
    # repeat until swap_counter is 0
    while swap_counter != 0:
        # reset swap_counter to zero
        swap_counter = 0
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                # look at each adjacent pair
                if arr[j] > arr[j+1]:
                    # if two adjacent elements are not in order,
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    # swap them and add one to the swap_counter
                    swap_counter += 1

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
