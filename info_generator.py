import json
import random


class NameGenerator:
    def __init__(self):
        with open('personal.json', 'r') as p:
            personal_dict = json.load(p)
            self.male_names = personal_dict['MALE']
            self.female_names = personal_dict['FEMALE']
            self.last_names = personal_dict['LAST']

    def get_male_name(self, as_list=False):
        if not as_list:
            return f'{random.choice(self.male_names)} {random.choice(self.last_names)}'
        else:
            return [random.choice(self.male_names), random.choice(self.last_names)]

    def get_female_name(self, as_list=False):
        if not as_list:
            return f'{random.choice(self.female_names)} {random.choice(self.last_names)}'
        else:
            return [random.choice(self.female_names), random.choice(self.last_names)]


class LocationGenerator:
    def __init__(self):
        with open('cities_states.json', 'r') as c:
            self.states_cities_dict = json.load(c)
            self.states = list(self.states_cities_dict.keys())

    def get_random_state(self):
        return random.choice(self.states)

    def get_random_city_state(self, as_list=False):
        random_state = random.choice(self.states)
        random_city = random.choice(self.states_cities_dict[random_state])
        if not as_list:
            return f'{random_city}, {random_state}'
        else:
            return [random_city, random_state]

    def get_cities_by_state(self, state):
        return [c for c in self.states_cities_dict[state.upper()]]


if __name__ == '__main__':
    pass
