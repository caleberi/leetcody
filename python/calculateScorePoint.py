from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not len(ops):
            return 0
        score_board = []
        for i in range(len(ops)):
            operand = float(ops[i]) if  ops[i].startswith("-") or ops[i].isdigit() else ops[i]
            if operand == "+" and len(score_board) >= 2:
                x = score_board[len(score_board) - 2]
                y = score_board[len(score_board) - 1]
                score_board.append(x + y)
                continue
            elif operand == "D" and len(score_board):
                score_board.append(score_board[len(score_board) - 1] * 2)
                continue
            elif operand == "C" and len(score_board):
                score_board.pop()
            else:
                score_board.append(operand)
        return int(sum(score_board))


if __name__ == "__main__":
    s = Solution()
    print(s.calPoints(["5", "2", "C", "D", "+"]))
    print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
