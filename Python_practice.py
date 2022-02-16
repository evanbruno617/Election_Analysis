print("Hello World")

counties = ['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
counties_dict = {}
counties_dict["Arapahoe"] = 411829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

voting_data = []

voting_data = [{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]

print(voting_data[1])

for county in counties:
    print(county)

for county, voter in counties_dict.items():
    print(f'{county} county has {voter:,} registered voters')
