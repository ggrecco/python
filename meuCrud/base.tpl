<!DOCTYPE html>
<html lang="pt-br">
<head>
   <meta charset="utf-8">
   <title>Cadastro Sqlite</title>

</head>

<body>
   	

<h3>CREATE</h3>
	<form action="/inserir" method="post">
		Nome: <input name="nome" type="text" />
		Telefone: <input name="telefone" type="text" />
		<input value="cadastrar" type="submit">
	</form>


<h3>READ</h3>
	<form action="/ler" method="post">
		Procurar por(id): <input name="dado" type="text" />
		<input value="buscar" type="submit" />
	</form>

<h3>UPDATE</h3>
	<form action="/editar" method="post">
		Nome: <input name="nome" type="text" />
		Novo Telefone: <input name="telefone" type="text" />
		<input value="editar" type="submit">
	</form>

<h3>DELETE</h3>
	<form action="/deletar" method="post">
		Nome: <input name="delete" type="text" />
		<input value="deletar" type="submit" />
	</form>

<h3>ALL</h3>
	<form action="/all" method="post">
		<input value="Mostrar Todos" type="submit" />
	</form>

<h1>{{things}}</h1>

<ul>
%for thing in things:
	<li>{{thing}}</li>
%end
</ul>
</body>
</html>