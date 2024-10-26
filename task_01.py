def caching_fibonacci():
    cash = {}

    def fibonacci(n):
        if n in cash:
            return cash[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cash[n]
    
    return fibonacci
