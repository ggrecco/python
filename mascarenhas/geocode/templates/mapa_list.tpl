<!DOCTYPE html>
<html lang="pt-BR" >
  <head>
    <meta charset="utf-8" />
    <title>Aula mapas - Lista</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <body>
   <table class="table">
	  <thead class="thead-dark">
		<tr>
		  <th scope="col">#</th>
		  <th scope="col">Nome</th>
		  <th scope="col">Endereço</th>
		  <th scope="col">Ações</th>
		</tr>
	  </thead>
	  <tbody>
		  {% for d in dados %}
		<tr>
		  <th scope="row">{{d[0]}}</th>
		  <td>{{d[1]}}</td>
		  <td>{{d[2]}}</td>
		  <td><a class="btn btn-primary" href="/map/{{d[0]}}">Map</a></td>
		</tr>
		{% endfor %}
	</tbody>
  </table>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
