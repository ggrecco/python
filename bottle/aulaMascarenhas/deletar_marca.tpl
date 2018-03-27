<h2> Deletar Marca </h2>

<h3> VOCÊ TEM CERTEZA? </h3>

<ul>
	<li>
		<p>Nome: {{dados[1]}}</p>
	</li>
	<li>
		<p>Origem: {{dados[2]}}</p>
	</li>
	<li>
		<p>Fundação: {{dados[3]}}</p>
	</li>
	<li>
		<p>Presidente: {{dados[4]}}</p>
	</li>
</ul>

<form action="/marca/deletar" method="post">
	<input type="hidden" name="id" value="{{dados[0]}}">
	<button type="submit" class="btn">Deletar</button>
</form>

<a href="/marcas">Voltar</a>
