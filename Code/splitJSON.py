__author__ = 'snehi23'
import json

time_zone = ['Abu Dhabi','Adelaide','Almaty','Amman','Amsterdam','Arizona','Astana','Anchorage','Athens','Atlantic Time (Canada)','Auckland','Azores','Baghdad','Baku','Bangkok','Beijing','Barbados','Beirut','Belgrade','Berlin','Bern','Bogota','Brasilia','Bratislava','Brazzaville','Brisbane','Brussels','Bucharest','Budapest','Buenos Aires','Cairo','Canberra','Cape Verde','Caracas','Casablanca','Central America','Central Time (US & Canada)','Chennai','Chicago','Chihuahua','Colombo','Costa Rica','Chongqing','Copenhagen','Darwin','Dhaka','Dublin','Denver','Dubai','Eastern Time (US & Canada)','Edinburgh','Ekaterinburg','Fiji','Georgetown','Greenland','Guadalajara','Guam','Halifax','Hanoi','Harare','Hawaii','Helsinki','Hobart','Hong Kong','Honolulu','Indiana (East)','International Date Line West','Irkutsk','Islamabad','Istanbul','Jakarta','Jeruslem','Kabul','Kamchatka','Karachi','Kathmandu','Kolkata','Krasnoyarsk','Kuala Lumpur','Kuwait','Kyiv','Los Angeles','La Paz','Lima','Lisbon','Ljubljana','London','Madrid','Magadan','Majuro','Manaus','Marshall Is.','Mazatlan','Melbourne','Mexico City','Mid-Atlantic','Midway Island','Minsk','Montevideo','Monrovia','Monterrey','Moscow','Mountain Time (US & Canada)','Mumbai','Muscat','Nairobi','New York','New Caledonia','New Delhi','Newfoundland','Novosibirsk','Nuku','alofa','Nuuk','Oral','Osaka','Pacific Time (US & Canada)','Paris','Perth','Phoenix','Regina','Port Moresby','Prague','Pretoria','Quito','Rangoon','Riga','Riyadh','Rome','Samoa','Santiago','Sao Paulo','Sapporo','Sarajevo','Saskatchewan','Seoul','Singapore','Skopje','Sofia','Solomon Is.','Sri Jayawardenepura','St. Petersburg','Stockholm','Shanghai','South Georgia','St John\'s','Sydney','Taipei','Tallinn','Tashkent','Tbilisi','Tehran','Tijuana','Tokyo','Tongatapu','Ulaan Bataar','Urumqi','Vienna','Vilnius','Vladivostok','Windhoek','Yakutsk','Yekaterinburg','Yerevan','Volgograd','Warsaw','Wellington','West Central Africa','Zagreb']
data = []
with open('tweets_#prayforparis.json') as f:
    for line in f:
        data.append(json.loads(line))

count = 0
for i in data:
     if 'user' in i and i["user"] is not None and i["user"]["time_zone"] in time_zone:
         count += 1
         print count
         with open('twitter_collection_'+i["user"]["time_zone"]+'.json', "a") as feedsJson:
             json.dump(i,feedsJson)
