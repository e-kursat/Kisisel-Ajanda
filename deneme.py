import json
from get_json import get_data

with open('accounts.json', 'r') as file:
    data = json.load(file)

# print(data)

# for account in data:
#     print(data[account])

# print(get_data()) 

# print(data)

# for account in data:
#     print(account)
#     print("-"*10)
    
# print(data['a']['id'])

# for now in data:
#     print(now)
    # print(data[now]['upass'])
    
# print(int(max([data[account]['id'] for account in data])))

# for account in accounts_data:
    
for account in data:
    print(data[account]['email'])