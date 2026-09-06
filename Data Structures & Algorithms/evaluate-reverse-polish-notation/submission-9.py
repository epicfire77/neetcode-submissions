class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = deque()
        opers = {'+', '-', '*', '/'}
        res = 0
        for t in tokens:
            if t in opers:
                print(nums)
                b = nums.pop()
                a = nums.pop()
                match t:
                    case '+':
                        res = a + b
                    case '-':
                        res = a - b
                    case '*':
                        res = a * b
                    case '/':
                        res = a // b
                        if res < 0:
                            res = -a // b
                            res *= -1
                print(a, t, b, res)
                nums.append(res)
            else:
                nums.append(int(t))
        print(nums)
        return nums.pop()