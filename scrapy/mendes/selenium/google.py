from selenium import webdriver

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'lst-ib' #id da barra de busca
        self.btn_search = 'btnK' #name do botão de busca
        self.btn_lucky = 'btnI' #name do botao estou com sorte

    def search(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)#search_bar é id
        self.driver.find_element_by_name(self.btn_search).click() #btn_search é name

    def lucky(self, word='None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)#search_bar é id
        self.driver.find_element_by_name(self.btn_lucky).click() #btn_search é name

    def navigate(self):
        self.driver.get(self.url)

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
#g.search('youtube')#classe criada para busca
g.lucky('youtube')
ff.quit()#para fechar a pagina
