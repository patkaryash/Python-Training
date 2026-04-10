def capitalizedFirst(arr):
    result = []
    if len(arr)==0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizedFirst(arr[1:])


print(capitalizedFirst(["hello", "world"]))  # ['Hello', 'World']