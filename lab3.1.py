num = input("Введіть п'ятизначне число: ")

if len(num) == 5 and num.isdigit():
    
    num1 = int(num[0])
    num5 = int(num[-1])
    
    num2 = int(num[1])
    num3 = int(num[2])
    
    dob = num1 * num5
    sum = num2 + num3
    
    print(f"Добуток першої та останньої цифр: {dob}")
    print(f"Сума другої та третьої цифр: {sum}")
else:
    print("Будь ласка, введіть п'ятизначне число.")