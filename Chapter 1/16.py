def recursive(array, index = 0, current_subarray = None):
    if current_subarray is None:
        current_subarray = []

    if index== len(array):
        print(current_subarray)
        return

    recursive(array, index + 1, current_subarray + [array[index]])

    recursive(array, index + 1, current_subarray)



recursive([1, 2, 3])

