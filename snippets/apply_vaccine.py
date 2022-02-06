from vaccine_centers_db import get_center_data
import collections
from population import generate_random_population


class OutOfDosesException(Exception):
    pass


def lookup_vaccine_name(individual):
    location_day_data = get_center_data(individual.jab_location, individual.date_first_jab)
    return location_day_data.vaccine_name

def apply_vaccine_to_population(population, ndoses, threshold_age):
    for ind in population:
        if ndoses > 0:
            if (ind["age"] > threshold_age or ind["isAtRisk"]):
                if ind["hasFirstJab"]:
                    inject_second_jab(ind)
                else:
                    inject_first_jab(ind)
            ndoses = ndoses - 1
        else:
            raise OutOfDosesException

N = 100
ndoses = 120
threshold_age = 70
population = generate_random_population(N)
apply_vaccine_to_population(population, ndoses, threshold_age)
# Create a dictionary mapping vaccine name to respectice number of occurence.
# Ex: Counter(["pfizer", "pfizer", "moderna"]) -> {"pfizer": 2, "moderna": 1}
brand_histogram = collections.Counter([lookup_vaccine_name(ind) for ind in population])
