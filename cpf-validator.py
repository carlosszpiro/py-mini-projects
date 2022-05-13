user_cpf = input('Digite um CPF sem os caracteres especiais :: ')

if not user_cpf.isnumeric():
  print('Digite apenas um CPF sem os caracteres especiais')

else:
  qtd_cpf = len(str(user_cpf))
  if qtd_cpf != 11:
    print('Um CPF possui somente 11 números!')

  else:
    if user_cpf == (user_cpf[0] * 11):
      print('O CPF é inválido!')

    else:
      cpf = list(str(user_cpf))
      digito_1 = 0
      digito_2 = 0

      for i, i2 in enumerate(range(10, 1, -1)):
        digito_1 += int(cpf[i]) * i2

      digito_1 = 11 - (digito_1 % 11) if 11 - (digito_1 % 11) < 10 else 0

      for i, i2 in enumerate(range(11, 1, -1)):
        digito_2 += int(cpf[i]) * i2

      digito_2 = 11 - (digito_2 % 11) if 11 - (digito_2 % 11) < 10 else 0

      if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        print('O CPF', user_cpf, 'é válido!')

      else:
        print('O CPF', user_cpf, 'é inválido!')
