from fractions import Fraction

def decimal_to_mixed_fraction(decimal_number):
    fraction = Fraction(decimal_number).limit_denominator()
    whole = abs(fraction.numerator) // fraction.denominator
    remainder = abs(fraction.numerator) % fraction.denominator
    sign = '-' if decimal_number < 0 else ''
    if whole == 0:
        return f"{sign}{remainder}/{fraction.denominator}"
    elif remainder == 0:
        return f"{sign}{whole}"
    else:
        return f"{sign}{whole} {remainder}/{fraction.denominator}"

print("👋 Привет! Добро пожаловать в программу преобразования десятичных дробей в смешанные! 😊")

while True:
    # Ввод с заменой запятых на точки
    user_input = input("Введите десятичную дробь (или 'exit' для выхода): ").replace(',', '.')
    
    if user_input.lower() == 'exit':
        print("👋 Выход из программы. Хорошего дня! 🌟")
        break
    
    try:
        decimal_input = float(user_input)
        mixed_fraction = decimal_to_mixed_fraction(decimal_input)
        print(f"Смешанная дробь: {mixed_fraction}")
    except ValueError:
        print("❌ Некорректный ввод. Пожалуйста, введите число.")
