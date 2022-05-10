from random import randint as rand

user_cpf = ''

for i in range(9):
  user_cpf += str(rand(0, 9))

digito_1 = 0
digito_2 = 0

for i, i2 in enumerate(range(10, 1, -1)):
  digito_1 += int(user_cpf[i]) * i2

digito_1 = 11 - (digito_1 % 11) if 11 - (digito_1 % 11) < 10 else 0
user_cpf += str(digito_1)

for i, i2 in enumerate(range(11, 1, -1)):
  digito_2 += int(user_cpf[i]) * i2

digito_2 = 11 - (digito_2 % 11) if 11 - (digito_2 % 11) < 10 else 0
user_cpf += str(digito_2)

print(user_cpf)
