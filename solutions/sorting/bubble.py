
def buble_sort(arr: list):
    if not arr:
        return []

    for i in range( len( arr ) ):

        for j in range( 1, len( arr ) - i ):

            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr


print( buble_sort( [2, 8, 4, 7, 32, 55, -1] ) )


