#verifica se é palindrome
palavra = input("Palavra: ")
if palavra == palavra[::-1]:
    print("É Palindrome!")
else:
    print("Não é!")
