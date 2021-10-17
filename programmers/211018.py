# 1단계
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                pass
            else:
                basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        if len(basket) >= 2 and basket[len(basket) - 1] == basket[len(basket) - 2]:
            basket.pop(-1)
            basket.pop(-1)
            answer += 1
    return answer * 2