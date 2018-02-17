<h2> Alterar Marca </h2>

<form action="/marca/alterar" method="post">
		<input value="{{dados[0]}}" name="id" type="hidden" />
		<ul>
			    <li>
			        	<input value="{{dados[1]}}" name="nome" type="text" placeholder="MARCA" />
			    </li>
			    <li>
						<input value="{{dados[2]}}" name="origem" type="text" placeholder="ORIGEM" />
			    </li>
			    <li>
						<input value="{{dados[3]}}" name="fundacao" type="text" placeholder="FUNDACAO" />
			    </li>
			    <li>
						<input value="{{dados[4]}}" name="presidente" type="text" placeholder="PRESIDENTE" />
			    </li>
		</ul>
		<button type="submit" class="btn">Registrar</button>
</form>
