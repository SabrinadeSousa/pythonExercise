
class User:
    def __init__(self, firstName, lastName, age, city, cep):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.city = city
        self.cep = cep


usuario = User(
    "Francisco Stanley",
    "Rodrigues Albuquerque",
    25, "Brasília",
    "73305-513")

print("Nome: {}"
      "\nSobrenome: {}"
      "\nIdade: {} anos "
      "\nCidade: {} - CEP:{}"
      "\nNome completo: {}"
      .format(usuario.firstName, usuario.lastName,
              usuario.age, usuario.city, usuario.cep,
              usuario.firstName + usuario.lastName))

