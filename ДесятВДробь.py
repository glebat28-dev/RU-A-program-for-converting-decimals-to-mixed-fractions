from fractions import Fraction

from updater import check_for_updates

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

def mixed_fraction_to_decimal(mixed_fraction):
    parts = mixed_fraction.strip().split()
    
    if len(parts) == 1:  # Если это просто неправильная дробь
        return float(Fraction(parts[0]))
    
    whole_part = int(parts[0])  # Целая часть
    fraction_part = parts[1]  # Дробная часть
    numerator, denominator = map(int, fraction_part.split('/'))
    
    decimal_value = whole_part + (numerator / denominator)
    return decimal_value

def improper_fraction_to_mixed_fraction(improper_fraction):
    fraction = Fraction(improper_fraction)
    whole = fraction.numerator // fraction.denominator
    remainder = fraction.numerator % fraction.denominator
    
    if whole == 0:
        return f"{remainder}/{fraction.denominator}"
    elif remainder == 0:
        return str(whole)
    else:
        return f"{whole} {remainder}/{fraction.denominator}"

def improper_fraction_to_decimal(improper_fraction):
    fraction = Fraction(improper_fraction)
    return float(fraction)

print("👋 Привет! Добро пожаловать в программу преобразования дробей! 😊")
print("Пример смешанной дроби: 2 3/4 (это два целых и три четверти)")
check_for_updates()

while True:
    user_input = input("Введите десятичную дробь, смешанную дробь или неправильную дробь (или 'exit' для выхода): ").replace(',', '.')
    
    if user_input.lower() == 'exit':
        print("👋 Выход из программы. Хорошего дня! 🌟")
        break
    
    try:
        # Проверяем, является ли ввод десятичной дробью, смешанной дробью или неправильной дробью
        if ' ' in user_input:  # Если есть пробел, значит это смешанная дробь
            decimal_value = mixed_fraction_to_decimal(user_input)
            print(f"Десятичная дробь: {decimal_value}")
        elif '/' in user_input:  # Если есть '/', значит это неправильная дробь
            improper_fraction = Fraction(user_input)
            mixed_fraction = improper_fraction_to_mixed_fraction(improper_fraction)
            decimal_value = improper_fraction_to_decimal(improper_fraction)
            print(f"Смешанная дробь: {mixed_fraction}, Десятичная дробь: {decimal_value}")
        else:  # Иначе это десятичная дробь
            decimal_input = float(user_input)
            mixed_fraction = decimal_to_mixed_fraction(decimal_input)
            print(f"Смешанная дробь: {mixed_fraction}")
    except ValueError:
        print("❌ Некорректный ввод. Пожалуйста, введите число или дробь.")

