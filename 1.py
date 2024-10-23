def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif unit.upper() == 'F':
        return (value - 32) * 5/9  # Fahrenheit to Celsius
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")

# Input untuk konversi suhu
try:
    temp_value = float(input("Masukkan nilai suhu: "))
    temp_unit = input("Masukkan satuan (C/F): ")
    converted_temp = convert_temperature(temp_value, temp_unit)
    print(f"Hasil konversi: {converted_temp:.2f} {'F' if temp_unit.upper() == 'C' else 'C'}")
except ValueError as e:
    print(e)