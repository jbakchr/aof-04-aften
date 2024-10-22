# Eksempel 1 - "type" funktionen
print(type("Min mor hedder Ole .."))  # <class 'str'>
print(type(1))  # <class 'int'>


# Eksempel 2.1 - Generelt 0m "strings"
double_quote_string = "Min mor hedder Ole .."  # Kan også skrives med 'single quotes'
triple_quote_string = """
    Min mor 
        hedder Ole .."""
print(triple_quote_string)


# Eksempel 2.2 - Indeksering af en string
first_char = double_quote_string[0]  # 'M'
last_char = double_quote_string[-1]  # '.'


# Eksempel 2.3 - Loop igennem en string
for char in double_quote_string:
    print(char)


# Eksempel 2.4 - Længden af en string
len_of_string = len(double_quote_string)  # 19


# Eksempel 2.5 - Tjek string for indhold af anden string
contains_mor = "mor" in double_quote_string  # True


# Eksempel 2.6 - Slicing af en string
my_mom = double_quote_string[0:8]  # 'Min mor'
print(my_mom)


# Eksempel 2.7 - String metoder
double_quote_string.lower()  # 'min mor hedder ole ..'
double_quote_string.upper()  # 'MIN MOR HEDDER OLE ..'
