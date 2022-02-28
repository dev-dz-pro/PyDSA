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
