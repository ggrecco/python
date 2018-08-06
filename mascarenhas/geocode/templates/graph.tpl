<!DOCTYPE html>
<html lang="pt" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <title>Aula População</title>
    <link href="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.css" rel="stylesheet" type="text/css" />
    <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"> -->
  </head>
  <body>
    <div class="" id="myfirstchart" > </div>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js" ></script> 
	<script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
	<script src="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js"></script>
	<script type="text/javascript">
	//<![CDATA[
	jQuery(document).ready(function() {
		var dados = {{ dados | safe }} ;
		//document.getElementById('mychart').innerHTML=document.write('hahahahaha');

		//new Morris.Area({
		//new Morris.Bar({
		new Morris.Line({
		  // ID of the element in which to draw the chart.
		  element: 'myfirstchart',
		  // Chart data records -- each entry in this array corresponds to a point on
		  // the chart.
		  data: dados,
		  // The name of the data record attribute that contains x-values.
		  xkey: 'ANO',
		  // A list of names of data record attributes that contain y-values.
		  ykeys: ['EUA','BRA'],
		  // Labels for the ykeys -- will be displayed when you hover over the
		  // chart.
		  labels: ['Pop EUA', 'Pop BRA']
		});
	});
	//]]>
	</script>
  </body>
</html>
