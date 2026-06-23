patterns = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"]   # 9
]

def my_led_display(number):
    digits = str(number)
    rows = ['' for _ in range(5)]

    for digit in digits:
        pattern = patterns[int(digit)]
        for i in range(5):
            rows[i] += pattern[i] + '  '

    for row in rows:
        print(row)

# Ejemplo de uso
numero = int(input("Ingresa un número: "))
my_led_display(numero)