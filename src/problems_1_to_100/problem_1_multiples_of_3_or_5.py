def multiples_of_3_or_5(n: int) -> int:
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


print(multiples_of_3_or_5(10))  # 23
print(multiples_of_3_or_5(49))  # 543
print(multiples_of_3_or_5(1000))  # 233168
print(multiples_of_3_or_5(8456))  # 16687353
print(multiples_of_3_or_5(19564))  # 89301183
