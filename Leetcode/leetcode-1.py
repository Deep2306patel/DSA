#### Reverse int ####

# firstInt = 2354
# x = 0
# int_max = (2^32)-1
# int_min = -2^32
# while firstInt:
#     n = firstInt % 10
#     if firstInt > int_max/10 and firstInt < int_min/10:
#         x = 0
#     x = x * 10 + n
#     firstInt //=10
# print(x)


## Complement Base 10 Integer ##

# def bitwise(n):

#     m = n
#     mask = 0
    
#     ### edge case //
#     if n==0:
#         return 1
    
#     while m!=0:
#         mask = (mask << 1)|1
#         m = m >> 1
#     ans = (~n) & mask

#     return ans

# print(bitwise(int(input("enter a single digit : "))))



####  power of two  #######

# n = int(input("enter a number : "))
# m = 2
# while m != n:
#     m = m*2
#     print(m)
#     print(n)
#     if m >= n:
#         break
# if m == n:
#     print("it is power of 2")
# else:
#     print("it is not power of 2")

    
# // Swap two num using bitwise xor

# a = 2 ## 010
# b = 3 ## 011

# a = a ^ b  ## 010 ^ 011 = 001
# b = a ^ b  ## 001 ^ 011 = 010
# print(f'b : {b}')
# a = a ^ b  ## 010 ^ 001 = 011
# print(f'a : {a}')


### Implement a function that counts the number of 1s in the binary representation of an integer using bitwise operators.

# def counts(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count
# print(counts(10))
# print(counts(2))

### Implement a function that checks if a given number is a power of two using bitwise operators.

# def power_is(n):
#     return n > 0 and (n & (n-1)) == 0

# print(power_is(int(input('enter a number : '))))

