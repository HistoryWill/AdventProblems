
with open('day1input.txt') as fp:
    nums =[]
    for cnt, line in enumerate(fp):
        x=line.strip()
        nums.append(int(x))
        print
    for q in nums:
        for y in nums:
            for m in nums:
                if q+y+m == 2020:
                    print(q)
                    print(y)
                    print(m)
#comment out the second 2 lines if you wish to complete the first item
