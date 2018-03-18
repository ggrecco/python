#grava e mum arquivo .cvs
from samuraix import lista_episodios

with open('episodios.cvs', 'w') as _file:
    _file.write('Temporada; Episódio; Nome\n')
    for ep in lista_episodios:
        _file.write('{};{};{}\n'.format(ep.temporada, ep.episodio, ep.nome))
