# 1단계
# 최소직사각형

def solution(sizes):
    width = []
    height = []
    for a in range(len(sizes)):
        if sizes[a][0] < sizes[a][1]:
            sizes[a][0], sizes[a][1] = sizes[a][1], sizes[a][0]
        width.append(sizes[a][0])
        height.append(sizes[a][1])
    max_width = max(width)
    max_height = max(height)
    answer = max_width * max_height
    return answer