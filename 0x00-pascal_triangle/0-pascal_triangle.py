def pascal_triangle(n):
    ls = []

    if n <= 0:
        return ls

    ls.append([1])

    for i in range(1, n):
        new_ls = []
        ol = ls[-1]

        for j in range(len(ol) + 1):
            f = ol[j - 1] if j - 1 >= 0 else 0
            l = ol[j] if j < len(ol) else 0
            new_ls.append(f + l)

        ls.append(new_ls)

    return ls

