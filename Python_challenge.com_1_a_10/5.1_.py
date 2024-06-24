from urllib.request import urlopen
import pickle


# Load the serialized object from the URL
raw_data = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
loaded_data = pickle.loads(raw_data)




print(loaded_data)


print("###############################")
# Print the loaded data
for line in loaded_data:
    print("".join([char * count for char, count in line]))
