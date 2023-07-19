import requests

def server_get_zeno():
    try:
        url = "https://raw.githubusercontent.com/rntkdgnl932/server/master/zenonia.txt"

        response = requests.get(url)
        data = response.text

        print("server_get_zeno", data)
        return data
    except Exception as e:
        print(e)
        return 0

def server_get_version():
    try:
        url = "https://raw.githubusercontent.com/rntkdgnl932/new_zeno/master/data_zeno/mymodule/version.txt"

        response = requests.get(url)
        data = response.text

        print("server_get_version", data)
        return data
    except Exception as e:
        print(e)
        return 0