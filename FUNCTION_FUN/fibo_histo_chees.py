def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    elif n == 0:
        return 0
    else:
        f = [0,1]
        for i in range(n - 2):
            x = f[-1] + f[-2]
            f.append(x)
        return f[-1]


def chessboard(n=8, pattern="# "):
    line = ""
    for i in range(n):
        for j in range(n):
            line += pattern[(i % len(pattern) + j) % len(pattern)]
            if j + 1 == n:
                line += "\n"
    return line


def histogram(l):
    try:
        a = ""
        for item in l:
            if a != "":
                a += "\n"
            for num in range(item):
                a += "#"
        return a
    except:
        return None


if __name__ == "__main__":
    print(chessboard(7))