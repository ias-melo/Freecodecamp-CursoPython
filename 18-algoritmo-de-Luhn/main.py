def verify_card_number(card_number: str) -> str:
  # Remove traços (-) e espaços em branco
  cleaned = card_number.replace("-", "").replace(" ", "")

  # Converte a string limpa em uma lista de inteiros
  digits = [int(char) for char in cleaned]

  total_sum = 0
  # Percorre os dígitos da direita para a esquerda
  # 'reverse=True' inverte a ordem para começar do dígito mais à direita
  for i, digit in enumerate(reversed(digits)):
    if i % 2 == 1:  # Dobre a cada segundo dígito (da direita para a esquerda)
      doubled = digit * 2
      if doubled > 9:
        doubled -= 9
      total_sum += doubled
    else:
      total_sum += digit

  # Se a soma total for múltiplo de 10, o número é válido
  if total_sum % 10 == 0:
    return "VALID!"
  else:
    return "INVALID!"
