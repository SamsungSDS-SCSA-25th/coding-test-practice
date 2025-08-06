# 흑: player1 / 백: player2
# 흑과 백이 번갈아 둔 돌에 따라 보드의 값들이 바뀌면서 나아가야함 -> 흑돌이 선
# 게임이 끝나고 돌이 더 많은 사람이 승자

DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1), (1,1),(-1,-1),(1,-1),(-1,1)]

def initBoard():
    board = [ ['.']*6 for _ in range(6) ]
    board[2][2] = 'W'
    board[3][3] = 'W'
    board[2][3] = 'B'
    board[3][2] = 'B'
    return board

def inRange(col, row):
    return 0<=col<6 and 0<=row<6 # 행과열 모두 범위를 만족하면 True 반환

def flipStone(board, col, row, playerColor):
    #1 전처리
    if playerColor == 'W':
        opponentColor = 'B'
    elif playerColor == 'B':
        opponentColor = 'W'
    board[row][col] = playerColor

    #2 탐색 시작 -> 시뮬레이션 공부하기 좋음
    for dx, dy in DIRECTIONS: # 8방향 확인
        nxtCol, nxtRow = col + dx, row + dy
        opponentColRowList = []
        while inRange(nxtCol, nxtRow) and board[nxtRow][nxtCol] == opponentColor: # 8방향에 대해 상대방 돌이 있고
            opponentColRowList.append((nxtCol, nxtRow)) # 앞으로 나아가면서 적돌 담기
            nxtCol += dx # 다음 위치 갱신
            nxtRow += dy # 다음 위치 갱신
        if inRange(nxtCol, nxtRow) and board[nxtRow][nxtCol] == playerColor: # 내 돌과 만남 -> 쌓아온 적돌 샌드위치로 잡아먹히는 상호아
            for finalCol, finalRow in opponentColRowList: # (D) row, col 다시 쓰면 안됨. 새로운 변수명으로!
                board[finalRow][finalCol] = playerColor

def printBoard(board):
    for row in board:
        print("".join(row))

def printWinner(board):
    blackCnt, whiteCnt = 0, 0
    for row in range(6):
        for col in range(6):
            if board[row][col] == 'W':
                whiteCnt += 1
            elif board[row][col] == 'B':
                blackCnt += 1

    if whiteCnt > blackCnt:
        return print('White')
    elif whiteCnt < blackCnt:
        return print('Black')
    elif whiteCnt == blackCnt:
        return print(-1)

def main():
    n = int(input())
    board = initBoard()
    for colorIdx in range(n):
        row, col = map(int, input().split())
        row -= 1  # (D) 좌표계 유의
        col -= 1  # (D)

        if colorIdx % 2 == 0:
            playerColor = 'B'
        elif colorIdx % 2 != 0:
            playerColor = 'W'

        flipStone(board, col, row, playerColor)

    printBoard(board)
    printWinner(board)

############################
main()