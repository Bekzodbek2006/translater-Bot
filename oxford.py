import requests
import json
app_id = "d3efc512"
app_key = "ed12860d963de6f07e7cb2a5e22e51f2"
language = "en-gb"



def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉{sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output





# def getInlineDefinitions(search_query):
#     url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + search_query.lower()
#     r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
#     res = r.json()
#     inline_reply = {}
#     inline_senes = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
#     malumotlar = []
#     for inline_ses in inline_senes:
#         malumotlar.append(f"👉{inline_ses['definitions'][0]}")
#     inline_reply['definitions'] = "\n".join(malumotlar)
#     return inline_reply
    
# if __name__ == '__main__':
#     from pprint import pprint as print
#     print(getInlineDefinitions("america"))