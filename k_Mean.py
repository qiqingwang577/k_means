import numpy as np
import matplotlib.pyplot as plt

# Calculate distance between two points
def distance(e1, e2):
    return np.sqrt((e1[0]-e2[0])**2+(e1[1]-e2[1])**2)

# Calculate cluster center
def means(arr):
    return np.array([np.mean([e[0] for e in arr]), np.mean([e[1] for e in arr])])

# Calculate the element, which farthest from a in arr, for initializing cluster centers
def farthest(k_arr, arr):
    f = [0, 0]
    max_d = 0
    for e in arr:
        d = 0
        for i in range(k_arr.__len__()):
            d = d + np.sqrt(distance(k_arr[i], e))
        if d > max_d:
            max_d = d
            f = e
    return f

# Calculate the element, which closest to a in arr
def closest(a, arr):
    c = arr[1]
    min_d = distance(a, arr[1])
    arr = arr[1:]
    for e in arr:
        d = distance(a, e)
        if d < min_d:
            min_d = d
            c = e
    return c


if __name__=="__main__":
    # Generate two-dimensional random coordinates
    # arr is an array, each element has two nummbers, representing a coordinate.
    # arr such as：[ (x1, y1), (x2, y2), (x3, y3) ... ]
    arr = np.random.randint(100, size=(100, 1, 2))[:, 0, :]

    # Initialize cluster centers and cluster containers
    m = 5
    r = np.random.randint(arr.__len__() - 1)
    k_arr = np.array([arr[r]])
    cla_arr = [[]]
    for i in range(m-1):
        k = farthest(k_arr, arr)
        k_arr = np.concatenate([k_arr, np.array([k])])
        cla_arr.append([])

    # Iterative clustering
    n = 20
    cla_temp = cla_arr
    for i in range(n):                               # Iterate n times
        for e in arr:                                # Gather each element in the collection to the nearest class
            ki = 0                                   # Assume that the first center is the closest
            min_d = distance(e, k_arr[ki])
            for j in range(1, k_arr.__len__()):
                if distance(e, k_arr[j]) < min_d:    # Find closer cluster centers
                    min_d = distance(e, k_arr[j])
                    ki = j
            cla_temp[ki].append(e)
        # Update iteratively cluster centers
        for k in range(k_arr.__len__()):
            if n - 1 == i:
                break
            k_arr[k] = means(cla_temp[k])
            cla_temp[k] = []

    # Display
    col = ['HotPink', 'Aqua', 'Chartreuse', 'yellow', 'LightSalmon']
    for i in range(m):
        plt.scatter(k_arr[i][0], k_arr[i][1], linewidth=10, color=col[i])
        plt.scatter([e[0] for e in cla_temp[i]], [e[1] for e in cla_temp[i]], color=col[i])
    plt.show()
