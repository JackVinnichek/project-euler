import math
def main():
    items = triplet(1000)
    for item in items:
        a,b,c = item
        if a + b + c == 1000:
            print(a*b*c)
    


def triplet(max):
    cees = set()
    for a in range(1,max):
        for b in range(a + 1, max):
            c = a**2 + b**2
            if math.sqrt(c) - int(math.sqrt(c)) == 0:
                cees.add((a,b,math.sqrt(c)))
    return cees
    

main()


def prime(max):
    s = set()
    for num in range(2, max + 1):
        s.add(num)
        for i in range(2,num - 1):
            if num % i == 0:
                s.remove(num)
                break
    return s

