# Keyword arguments also send arguments with the key = value syntax.
# help the arguments is readable

def keyword_argu(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

keyword_argu("Halo", title="Ini Keyword Argue", first="Tio", last="Pramana")

def phone_number(country, first, second, third):
    return f"+{country}-{first}-{second}-{third}"

print(phone_number(country=62, first=877, second=3176, third=4987))

