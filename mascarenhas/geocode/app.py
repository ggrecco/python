from flask import Flask, jsonify, url_for, request, render_template
import sqlite3
from geopy.geocoders import ArcGIS, Bing, Nominatim, OpenCage,  GoogleV3

app = Flask(__name__)

arcgis = ArcGIS(timeout=100)
#bing = Bing('your-API-key',timeout=100)
nominatim = Nominatim(timeout=100,user_agent="my-test-application")
#opencage = OpenCage('your-API-key',timeout=100)
#geocoderDotUS = GeocoderDotUS(timeout=100)
googlev3 = GoogleV3(timeout=100)
#openmapquest = OpenMapQuest(timeout=100)

# choose and order your preference for geocoders here
geocoders = [googlev3,  nominatim]


@app.route('/', methods=['GET'])
def index():
	mymap   = sqlite3.connect('mapa.db')
	conn2 = mymap.cursor()
	sql = "SELECT * FROM mapa"
	dados = conn2.execute(sql).fetchall()
	conn2.close()
	return render_template('mapa_list.tpl', dados=dados)


@app.route('/pop', methods=['GET'])
def pop():
	mygraph = sqlite3.connect('populacao.db')
	conn1 = mygraph.cursor()
	sql = "SELECT * FROM populacao"
	dados = conn1.execute(sql).fetchall()
	conn1.close()
	lista = []
	dicionario = {}
	i = 0
	while i < len(dados):
		dicionario["ANO"] = str(dados[i][1])
		dicionario["EUA"] = dados[i][2]
		dicionario["BRA"] = dados[i][3]
		lista.append(dicionario)
		dicionario = {}
		i = i + 1
	return render_template('graph.tpl', dados=lista)
    #return redirect('/listar')
    
@app.route('/map/<int:_id_>', methods=['GET'])
def map(_id_):
	mymap   = sqlite3.connect('mapa.db')
	conn2 = mymap.cursor()
	sql = "SELECT * FROM mapa WHERE id=?"
	dados = conn2.execute(sql,(_id_,)).fetchall()
	address = dados[0][2]
	result = geocode(address)
	conn2.close()
	return render_template('map.tpl', dados=result)

def geocode(address):
    i = 0
    try:
        while i < len(geocoders):
            # try to geocode using a service
            location = geocoders[i].geocode(address)

            # if it returns a location
            if location != None:
                
                # return those values
                return [location.latitude, location.longitude]
            else:
                # otherwise try the next one
                i += 1
    except:
        # catch whatever errors, likely timeout, and return null values
        print(sys.exc_info()[0])
        return ['null','null']

    # if all services have failed to geocode, return null values
    return ['null','null']

app.run(debug=True)
