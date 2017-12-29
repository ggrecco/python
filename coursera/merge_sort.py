def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista)//2

    lado_esquerdo = merge_sort(lista[:meio]) #pega todo lado esquerdo até meio -1
    lado_direito = merge_sort(lista[meio:]) #pega do meio até direito

    retunr merge(lado_esquerdo, lado_direito)

def merge(lado_esquedo, lado_direito):
    if not lado_esquedo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquedo[0]] + merge(lado_esquedo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
