import json
import wikipedia


with open('bilgiler.json', 'r', encoding='utf-8') as file:
    city_data = json.load(file)

def get_city_info(city_name):
    
    city_name_lower = city_name.lower()
    city_name_capitalized = next((name for name in city_data if name.lower() == city_name_lower), None)
    
    if not city_name_capitalized:
        return "Bu şehir veritabanında mevcut değil."

    
    json_info = city_data[city_name_capitalized]

  
    try:
        wikipedia.set_lang("tr")
        wiki_info = wikipedia.page(city_name_capitalized).content[:1000]  # İlk 1000 karakteri al
    except wikipedia.exceptions.PageError:
        wiki_info = "Wikipedia'da bu şehir hakkında bilgi bulunamadı."

    
    result = f"Wikipedia Bilgisi:\n{wiki_info}\n\n" \
             f"Şehir: {json_info['name']}\n\n" \
             f"Turistik Yerler:\n" + "\n".join(json_info['attractions']) + "\n\n" \
             f"Yöresel Lezzetler:\n" + "\n".join(json_info['foods'])

    return result


city_name = input("Bilgi almak istediğiniz şehri girin: ")
info = get_city_info(city_name)
print(info)
