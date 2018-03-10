<h3>Marcas</h3>
<hr>
    <table border="1">
    <thead>
    <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Origem</th>
        <th>presidente</th>
        <th>Fundação</th>
        <th>Funções</th>
    </tr>
    </thead>
        % for dado in dados:
        <tr>
            <td>{{dado[0]}}</td>
            <td>{{dado[1]}}</td>
            <td>{{dado[2]}}</td>
            <td>{{dado[3]}}</td>
            <td>{{dado[4]}}</td>
            <td><a href="/marca/alterar/{{dado[0]}}"><button>Alterar</button></a>
            <a href="/marca/deletar/{{dado[0]}}"><button>Deletar</button></a></td>

        </tr>
        % end
    </table>
