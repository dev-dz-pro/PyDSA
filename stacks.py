# Fish STACK EXERCISE - solution for https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
def solution(A:list[int], B:list[int]):
    stack = []
    for i in range(len(A)):
        if i == 0 or B[i] == 1:
            stack.append((A[i], B[i]))
        else:
            while stack and B[i] == 0 and stack[-1][1] == 1:
                if stack[-1][0] <= A[i]:
                    stack.pop()
                else:
                    break
            else:
                stack.append((A[i], B[i]))
    return len(stack)



# StoneWall STACK EXERCISE - solution for https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
def solution(H:list[int]):
    stack = []
    res = 0
    for i in range(len(H)):
        if i == 0:
            stack.append(H[i])
        elif stack and H[i] > stack[-1]:
            stack.append(H[i])
        else:
            while stack:
                if stack[-1] == H[i]:
                    break
                elif stack[-1] > H[i]:
                    stack.pop()
                    res += 1
                else:
                    stack.append(H[i])
                    break
            else:
                stack.append(H[i])
    return len(stack) + res


# Brackets STACK EXERCISE - solution for https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/  and  https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/
def solution(S:str): 
    if S == "":
        return 1
    stack = []
    for c in S:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            if stack and ((c == ")" and stack[-1] == "(") or (c == "}" and stack[-1] == "{") or (c == "]" and stack[-1] == "[")):
                stack.pop()
            else:
                return 0
    return 1 if not stack else 0