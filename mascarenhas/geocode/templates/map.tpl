<!DOCTYPE html>
<html lang="pt-BR" >
  <head>
    <meta charset="utf-8" />
    <title>Aula mapas</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.3/leaflet.css" />
  </head>
  <body>
    <div class="" id="mymap" style="height: 500px;"></div>


	<!--<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	--> <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.3/leaflet.js"></script>
	<script type="text/javascript">
	//<![CDATA[
	
	var lat = {{ dados[0] | safe }} ;
	var lng = {{ dados[1] | safe }} ;
	var mymap = L.map('mymap').setView([lat, lng], 13);
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'your.mapbox.access.token'
	}).addTo(mymap);
	var marker = L.marker([lat, lng]).addTo(mymap);
	
	//]]>
	</script>

  </body>
</html>
