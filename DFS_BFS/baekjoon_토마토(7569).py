# 며칠이 지나면 토마토들이 모두 익는지 최소 일수를 구하기
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸

# 1과 인접한 노드가 0이라면 1로 바꾸고 익는 일수 더하기
# -1이라면 pass하기
from collections import deque

m, n = map(int, input().split()) # 상자의 크기 m = 가로칸의 수, n = 세로 칸의 수

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# print(data)
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 현재 좌표값이 범위에 들어오지 않는다면 패스
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            # 만약 좌표값이 0이라면 익은 토마토로 만들기
            elif data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1    
                queue.append((nx, ny))
                
bfs()
result = 1
flag = False
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            flag = True
        elif data[i][j] > result:
            result = data[i][j]
            

if flag == True:
    print(-1)
else:
    print(result - 1)