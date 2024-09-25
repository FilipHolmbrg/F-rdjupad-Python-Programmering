#imports
import re

def match_recipe(data: dict) -> dict:

    bas_recept = {
                    'carbonara': ['pasta', 'bacon', 'ägg', 'grädde', 'parmesan'],
                    'stuvade mackaroner m. köttbullar': ['köttbullar', 'mackaroner'],
                    'korvstroganoff': ['falukorv', 'ris', 'gröna ärtor', 'tomatpuré', 'passerade tomater', 'grädde'],
                    'hamburgare': ['hamburgare', 'hamburgerbröd', 'hamburgerost'],
                    'kycklingjärpar': ['ströbröd', 'ägg', 'soltorkade tomater', 'kycklingfärs', 'ris', 'potatis', 'matyoghurt', 'turkisk yoghurt', 'grekisk yoghurt', 'vitlök'],
                    'ugnspannkaka': ['ägg', 'mjölk', 'morötter', 'äpple', 'bacon', 'smör'],
                    'torsk m. äggsås': ['torsk', 'torskrygg', 'potatis', 'ärtor', 'ägg', 'smör', 'persilja'],
                    'potatisplättar m. bacon': ['potatisbullar', 'bacon', 'lingonsylt', 'rårörda lingon', 'creme fraiche'],
                    'kokossoppa m. bönor': ['purjolök', 'potatis', 'kokosmjölk', 'grönsaksbuljong', 'timjan', 'små vita bönor', 'pain riche', 'chiabatta'],
                    'korv m. pasta': ['grillkorv', 'pasta', 'ketchup'],
                    'köttfärssås m. pasta': ['köttfärs', 'passerade tomater', 'blandfärs', 'fond', 'pasta', 'tomatpuré', 'grädde', 'hönsbuljong', 'grönsaksbuljong', 'oxfond'],
                    'pasta m. tomatsås': ['pasta', 'grädde', 'spaghetti', 'körsbärstomater', 'parmesan', 'basilika'],
                    'pyttipanna': ['ägg', 'pyttipanna', 'inlagda rödbetor'],
                    'fiskbullar m. ris': ['ris', 'fiskbullar'],
                    'köttbullar m. potatis': ['köttbullar', 'gräddsås', 'brunsås', 'potatis', 'svartvinbärsgelé'],
                    'ost och skicksås': ['rökt skinka', 'rökt skinka, strimlad', 'pasta', 'ost', 'ärtor'],
                    'renskavsgryta': ['renskav', 'hjortskav', 'grädde', 'svartvinbärssaft', 'oxfond', 'grädde', 'lingon', 'svartvinbärsgéle', 'persilja'],
                    'blodpudding m. potatis': ['blodpudding', 'lingonsylt', 'rårörda lingon', 'potatis'],
                    'kycklingsallad': ['tärnad kyckling', 'rhode islandsås', 'pasta', 'grönsaker', 'majs'],
                    'hawaiikassler m. ananas': ['kassler', 'grädde', 'ananas', 'ris', 'purjolök', 'kycklingfond', 'ost', 'persilja']
                    }

    veckans_recept_förslag = {recipe: [] for recipe in bas_recept.keys()}

    for key, values in bas_recept.items():
        # print(key, values)
        current_recipe_list = [] 
        for value in values:
            for item in data['name']:
                if value.upper() in item:
                    # pattern = f'\b{item}\b'
                    pattern = fr'\b{item}\b'
                    # print(key, value, item)
                    # print(item, pattern)
                    match = re.search(pattern, value)
                    # veckans_recept_förslag.update({key: item})
                    if not value in current_recipe_list:
                        current_recipe_list.append(value)
        
        veckans_recept_förslag.update({key: current_recipe_list})
    
    # Only recover recipe suggestions that contain this week's offer(s)
    clean_veckans_recept_förslag = dict()
        
    for key, val in veckans_recept_förslag.items():
        if len(val) > 0:
            clean_veckans_recept_förslag[key] = val
    
    return clean_veckans_recept_förslag