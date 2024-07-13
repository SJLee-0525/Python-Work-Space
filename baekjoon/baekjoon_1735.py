def gcd(a, b):
    aa, bb = a, b
    while b != 0:
        a, b = b, a % b
    return aa * bb // a
    
def lcm(a, b):
    return a * b // gcd(a, b)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

b3 = gcd(b1, b2)

n1, n2 = b3 // b1, b3 // b2
a3 = a1 * n1 + a2 * n2

if lcm(a3, b3) == 1:
    print(a3, b3)

else:
    temp = lcm(a3, b3)
    print(a3 // temp, b3 // temp)


# a1, b1 = map(int, input().split())
# a2, b2 = map(int, input().split())

# b11, b22 = b1, b2

# while b11 % b22 != 0:
#     b11, b22 = b22, b11 % b22
# lcm_b = b1 * b2 // b22

# temp_1, temp_2 = lcm_b // b1, lcm_b // b2
# a11, a22  = a1 * temp_1, a2 * temp_2

# temp_a = a11 + a22

# fin_a, fin_b = temp_a, lcm_b

# while temp_a % lcm_b != 0:
#     temp_a, lcm_b = lcm_b, temp_a % lcm_b

# if lcm_b == 1:
#     print(fin_a, fin_b)

# else:
#     print(fin_a // lcm_b, fin_b // lcm_b)