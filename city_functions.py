def city_country(city, state, population=0):
    if population == 0:
        return (f'{city}, {state}')
    return(f'{city}, {state} - população {population}')