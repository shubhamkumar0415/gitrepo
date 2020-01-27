def make_multiplier_of(n):
    def multiplier(x):
        return x - n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(make_multiplier_of(6))

