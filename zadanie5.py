counter = {"calls": 0, "depth": 0, "max_depth": 0}

def fib_no_memo(n):
    counter["calls"] += 1
    counter["depth"] += 1
    if counter["depth"] > counter["max_depth"]:
        counter["max_depth"] = counter["depth"]
    
    if n <= 2:
        counter["depth"] -= 1
        return 1
    
    ans = fib_no_memo(n - 1) + fib_no_memo(n - 2)
    counter["depth"] -= 1
    return ans

memo = {}

def fib_memo(n):
    counter["calls"] += 1
    counter["depth"] += 1
    if counter["depth"] > counter["max_depth"]:
        counter["max_depth"] = counter["depth"]
    
    if n in memo:
        counter["depth"] -= 1
        return memo[n]
    
    if n <= 2:
        counter["depth"] -= 1
        return 1
    
    ans = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = ans
    counter["depth"] -= 1
    return ans

print("no memo:")
for n in (6, 10, 20):
    counter["calls"] = 0
    counter["depth"] = 0
    counter["max_depth"] = 0
    res = fib_no_memo(n)
    print("n =", n, "res =", res, "calls =", counter["calls"], "depth =", counter["max_depth"])

print("with memo:")
for n in (6, 10, 20):
    memo.clear()
    counter["calls"] = 0
    counter["depth"] = 0
    counter["max_depth"] = 0
    res = fib_memo(n)
    print("n =", n, "res =", res, "calls =", counter["calls"], "depth =", counter["max_depth"])
