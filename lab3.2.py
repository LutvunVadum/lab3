a = float(input("Введіть довжину сторони a: "))
b = float(input("Введіть довжину сторони b: "))
c = float(input("Введіть довжину сторони c: "))

ab = (a**2 + b**2 - (c**2) / 4)**0.5 / 2

ac = (a**2 + c**2 - (b**2) / 4)**0.5 / 2

bc = (b**2 + c**2 - (a**2) / 4)**0.5 / 2

print(f"Довжина середньої лінії сторін ab: {ab:.2f}")
print(f"Довжина середньої лінії сторін ac: {ac:.2f}")
print(f"Довжина середньої лінії сторін bc: {bc:.2f}")