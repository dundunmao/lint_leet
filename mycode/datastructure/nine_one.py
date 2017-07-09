__author__ = 'eva'


def summ(n):
    if n >=0:
        if n == 1 or n==0:
            return 1

        total1 = summ(n-1)
        total2 = summ(n-2)
        total3 = summ(n-3)
        total = total1+total2+total3


        return total

if __name__ == "__main__":

    print summ(6)