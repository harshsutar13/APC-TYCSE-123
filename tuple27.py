t = (10, 20, 10, 30, 20, 10, 40, 30)

checked = ()

for n in t:
    if n not in checked:
        count = 0

        for x in t:
            if x == n:
                count = count + 1

        print(n, "=", count)

        checked = checked + (n,)
