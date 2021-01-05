# sample = [{"name":"jaren"}, {"image":"test"}]

# for i in sample: 
#     if "name" in i:
#         print(i['name'])

# sample = [{'recipient_id': 'default', 'text': 'We sell a wide variety of games, which genre are you interested in?', 'buttons': [{'payload': '/action', 'title': 'Action'}, {'payload': '/adventure', 'title': 'Adventure'}, {'payload': '/horror', 'title': 'Horror'}, {'payload': '/indie', 'title': 'Indie'}, {'payload': '/multiplayer', 'title': 'Mutliplayer'}, {'payload': '/racing', 'title': 'Racing'}, {'payload': '/rpg', 'title': 'RPG'}, {'payload': '/simulation', 'title': 'Simulation'}, {'payload': '/sports', 'title': 'Sports'}]}]


# li = []

# for index, content in enumerate(sample): 

# li = []

# for i in range(0, 11, 2):
#     print('=========')
#     print(i)
#     print(i+1)
#     print('=========')

# print(li)

import requests

print(requests.get('http://localhost:5000/getUserID').text)