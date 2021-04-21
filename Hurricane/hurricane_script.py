# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updated_damages(damage):
  damage_list = []
  for record in damage:
    if record[-1] == 'B':
      cost = float(record[:-1]) * 1000000000
      damage_list.append(cost)
    elif record[-1] == 'M':
      cost = float(record[:-1]) * 1000000
      damage_list.append(cost)
    else:
      damage_list.append(record)
  return damage_list

expanded_values = updated_damages(damages)
print(expanded_values)
our_list = list


# write your construct hurricane dictionary function here:

def data_table(Name, Month, Year, Wind, Areas, Damage, Death):
  the_table = {}
  for i in range(len(Name)):
      the_table[Name[i]] = {
          "Name": Name[i],
          "Month": Month[i],
          "Year": Year[i],
          "Max Sustained Wind": Wind[i],
          "Areas Affected": Areas[i],
          "Damages": Damage[i],
          "Deaths": Death[i]
      }
  return the_table

data_table_dict = data_table(names, months, years, max_sustained_winds, areas_affected, expanded_values, deaths)
print(data_table_dict)



# write your construct hurricane by year dictionary function here:

def year_table(all_data):
  the_year_dict = {}
#  print(all_data)
  for key, value in all_data.items():
      year = all_data[key]["Year"]
      if not the_year_dict.get(year):
          the_year_dict[year] = [value]
      else:
          the_year_dict[year].append(value)
  return the_year_dict

year_table_dict = year_table(data_table_dict)

print(year_table_dict)


# write your find most affected area function here:
# write your count affected areas function here:

def area_table(all_data):
  the_area_dict = {}
  for areas_affected in all_data:
      for area in areas_affected:
        if the_area_dict.get(area):
          the_area_dict[area] += 1
        else:
          the_area_dict[area] = 1
  worst_affected_area = max(the_area_dict, key=the_area_dict.get)
  return worst_affected_area, the_area_dict[worst_affected_area]


max_area, max_area_count = area_table(areas_affected)
print(f"The most affected area is {max_area} with {max_area_count} hurricanes.")

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
# write your greatest number of deaths function here:
def death_table(all_data):
  death_dict = {}
  for hurricanes in all_data:
    hurricane = all_data[hurricanes]["Name"]
    if death_dict.get(hurricane):
          death_dict[hurricane] += all_data[hurricanes]["Deaths"]
    else:
          death_dict[hurricane] = all_data[hurricanes]["Deaths"]
  top_casualty = max(death_dict, key=death_dict.get)

  return top_casualty, death_dict[top_casualty]

# 6
# Calculating the Deadliest Hurricane
high_calsualty, total_count = death_table(data_table_dict)
print(f"The most deadly hurricane was {high_calsualty} with total death toll of  {total_count}")
# write your catgeorize by mortality function here:
# find highest mortality hurricane and the number of deaths
def mortality_table(all_data):
  mortality_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for hurricanes in all_data:
    hurricane = all_data[hurricanes]["Name"]
    if all_data[hurricanes]["Deaths"] == 0:
          mortality_dict[0].append({hurricane})
    elif all_data[hurricanes]["Deaths"] <= 100:
          mortality_dict[1].append({hurricane})
    elif all_data[hurricanes]["Deaths"] <= 500:
          mortality_dict[2].append({hurricane})
    elif all_data[hurricanes]["Deaths"] <= 1000:
          mortality_dict[3].append({hurricane})
    elif all_data[hurricanes]["Deaths"] <= 10000:
          mortality_dict[4].append({hurricane})
    else:
          mortality_dict[5].append({hurricane})

  return mortality_dict


# 7
# Rating Hurricanes by Mortality
hurricane_rating = mortality_table(data_table_dict)
print(hurricane_rating)
# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage
# write your greatest damage function here:
def find_hurricane_cost(all_data, hur_name):
#  keys = list(all_data.key())
#  vals = list(all_data.values())
#  hurricane_cost = keys[vals.index(hur_name)]
  most_costly_hurricane = all_data.get(hur_name)
  hurricane_cost = most_costly_hurricane["Damages"]
  return hurricane_cost
# find highest damage inducing hurricane and its total cost
hurricane_damage = find_hurricane_cost(data_table_dict, high_calsualty)
print(f"Hurricane with greatet damage was {high_calsualty} with cost of {hurricane_damage}")
print(expanded_values)
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# write your catgeorize by damage function here:
def damage_rating(all_data):
  hurricane_cost_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cost in all_data:
    hurricane = all_data[cost]["Name"]
    if all_data[cost]["Damages"] == 0 or all_data[cost]["Damages"] == 'Damages not recorded':
          hurricane_cost_dict[0].append({hurricane})
    elif all_data[cost]["Damages"] <= 100000000:
          hurricane_cost_dict[1].append({hurricane})
    elif all_data[cost]["Damages"] <= 1000000000:
          hurricane_cost_dict[2].append({hurricane})
    elif all_data[cost]["Damages"] <= 10000000000:
          hurricane_cost_dict[3].append({hurricane})
    elif all_data[cost]["Damages"] <= 50000000000:
          hurricane_cost_dict[4].append({hurricane})
    else:
          hurricane_cost_dict[5].append({hurricane})

  return hurricane_cost_dict  
# categorize hurricanes in new dictionary with damage severity as key
damage_based_rating = damage_rating(data_table_dict)
print(damage_based_rating)





