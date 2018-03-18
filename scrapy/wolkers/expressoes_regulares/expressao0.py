import re

pattern = re.compile(r"(segunda|terça|quarta|quinta|sexta)-feira")
sambadotrabalhador = "Na segunda-feira eu não vou trabalhar Na terça-feira não vou pra poder descansar Na quarta preciso me recuperar Na quinta eu acordo meio-dia, não dá Na sexta viajo pra veranear No sábado vou pra mangueira sambar Domingo é descanso e eu não vou mesmo lá Mas todo fim de mês chego devagar Porque é pagamento eu não posso faltar"
print(re.findall(pattern, sambadotrabalhador))


"""
pattern = re.compile('ana')
texto = "Ana adora ouvir chiclete com Banana, gosta de bananada e também banana, ela é irmã da Mariana."
print(re.findall(pattern, texto))

pattern = re.compile('ana', re.I)
print(re.findall(pattern, texto))
"""