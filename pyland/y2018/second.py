
# task 2

d = {}

def gcd(a, b):
    l = d.get(f"{a}_{b}", -1)
    if l != -1:
        return l
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    d[f"{a}_{b}"] = a
    d[f"{b}_{a}"] = a
    return a

def fun(number):
    number = number.split(" ")

    low = int(number[0])
    high = int(number[1])

    if low == high:
        print(1)
        return

    return_list = []
    for i in range(low, high + low, low):
        if high % i == 0:
            return_list.append(i)

    count = 0
    for first in return_list:
        for second in return_list:
            if first == second:
                continue
            elif high % second == 0 and (high / second) % first == 0:
                continue

            num_gcd = gcd(first, second)
            num_lcm = (first * second / num_gcd)
            if num_lcm == high and num_gcd == low:
                count = count + 1

    print(count)

if __name__ == '__main__':
    number = input()
    import time
    start = time.time()
    fun(number)
    print("Finihsed: ", time.time() - start)
