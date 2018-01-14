import bottle

@bottle.route('/')
def home_page():
    return "Primeira página com BOTTLE"

@bottle.route('/outra')
def test_page():
    return "Sub-página com bottle"

bottle.debug(True)
bottle.run(host = 'localhost', port = 8082)
