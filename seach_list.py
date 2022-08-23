# arr is the list I want to search
# low is the lowest index in the list
# high is the highest index in the list
# x is the item to search in the list
def search_list(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return search_list(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return search_list(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = search_list(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in the list")
