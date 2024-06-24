from urllib.request import urlopen
import pickle






# busca y carga el objeto serializado en la url y lo guarda en mi variable raw_data ... para despues desserializarlo y guardarlo en loaded_data


raw_data = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
loaded_data = pickle.loads(raw_data)




print(loaded_data)


print("###############################")
