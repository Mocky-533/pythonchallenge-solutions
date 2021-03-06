import cv2
import numpy as np

def inpic(coord):
    x = 0 <= coord[0] < 641
    y = 0 <= coord[1] < 641
    return x and y

def valid_check(coord, image, l):
    white = np.array([255, 255, 255])
    return inpic(coord) and coord not in l and not np.array_equal(image[coord], white)

def BFS(img: np.ndarray, entrance: np.ndarray, exit:np.ndarray):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue, visited = [exit], {}
    while queue:
        current = queue.pop(0) # get the head of the queue
        if current == entrance:
            break # early stop
        for dir in directions:
            pos = (current[0] + dir[0], current[1] + dir[1])
            if valid_check(pos, img, visited):
                visited[pos] = current # link the surrounding pixels to central pixel
                queue.append(pos)
    path = []
    while not np.array_equal(current, exit):
        path.append(current)
        current = visited[current] # reverse to find the path
    return path

def DFS_sub(img: np.ndarray, current, entrance: np.array, queue: list, visited: dict):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dir in directions:
        pos = (current[0] + dir[0], current[1] + dir[1])
        if valid_check(pos, img, visited):
            visited[pos] = current
            queue.append(pos)
    return queue, visited

def DFS(img, entrance, exit):
    queue, visited, path = [exit], {}, []
    while queue:
        current = queue.pop()
        if current == entrance:
            break
        queue, visited = DFS_sub(img, current, entrance, queue, visited)
    while not np.array_equal(current, exit):
        path.append(current)
        current = visited[current]
    return path

if __name__ == '__main__':
    img = cv2.imread("assets/maze.png")
    # width, height, _ = img.shape
    # black = np.array([0, 0, 0])
    # for i in range(width):
    #     if np.array_equal(img[0][i], black):
    #         print(i) # 639
    # for j in range(width):
    #     if np.array_equal(img[640][j], black):
    #         print(j) # 1
    entrance, exit = (0, 639), (640, 1)
    path = DFS(img=img, entrance=entrance, exit=exit)[1:] # change the function name to use different methods
    tofile = []
    for c in path:
        tofile.append(img[c][2])
    with open("assets/maze.zip", 'wb') as f:
        f.write(bytes(tofile[::2]))