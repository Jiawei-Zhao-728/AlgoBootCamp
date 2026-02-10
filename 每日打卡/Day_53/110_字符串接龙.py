from collections import deque

def solve(begin, end, word_list):
    word_list = set(word_list)
    word_list.add(end)

    queue = deque([(begin, 1)])
    visited = {begin}

    while queue:
        current, stops = queue.popleft()

        for i in range(len(current)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_string = current[:i] + c + current[i+1:]

                if new_string == end:
                    return stops + 1

                if new_string in word_list and new_string not in visited:
                    visited.add(new_string)
                    queue.append((new_string, stops + 1))

    return 0

if __name__ == "__main__":
    n = int(input().strip())          
    begin, end = input().strip().split()
    
    word_list = []
    for _ in range(n):                 
        word_list.append(input().strip())

    print(solve(begin, end, word_list))
