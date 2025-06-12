def solution(n, m):    
    for i in range(max(n, m) + 1, 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    
    lcm = gcd
    lcm *= n // gcd
    lcm *= m // gcd
    
    answer = [gcd, lcm]
            
    return answer