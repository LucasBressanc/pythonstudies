from datetime import date

year = int(input('Digite um ano e direi se é um ano bissexto ou não: '))

if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é um ano bissexto' .format(year))
else: print('O ano {} não é um ano bissexto' .format(year))