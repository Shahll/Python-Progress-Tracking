def euclidean(a, b):
    return b if a % b == 0 else euclidean(b, a % b)
# Driver
print(euclidean(128,64))