# Approach: keep dividing the array into smaller chunk by the factor of 2
# Time: O(logn) -> base 2 , Space: O(1)

arr = [-2, -1, 0, 4, 7, 9]

def binary_search(arr, val):
    left, right = 0, len(arr)-1
    while left <= right:
        middle = (left+right)//2
        
        """ to prevent overflow situation with 2^31 order numbers in other languages, basically taking the half distance between the numbers and adding it to the left """
        # middle = left + ((right-left)//2)
        
        if val > arr[middle]:
            left = middle+1
        elif val < arr[middle]:
            right = middle-1
        else:
            return middle
    else:
        print('Element not found')
        
print(f"the number is at postition: {binary_search(arr, 12)}")

