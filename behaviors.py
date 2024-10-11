import sys
sys.path.insert(0, '../')
from planet_wars import issue_order

def attack_weakest_enemy_planet(state):
    # (2) Find my strongest planet that doesn't already have a fleet out.
    source_planets = [planet for planet in state.my_planets()
                      if not any(fleet.source_planet == planet.ID for fleet in state.my_fleets())]
    if not source_planets:
        source_planets = state.my_planets()

    strongest_planet = max(source_planets, key=lambda t: t.num_ships, default=None)

    if not strongest_planet:
        # No legal source
        return False

    # (3) Find the closest enemy planet that my planet can beat.
    target_planets = [planet for planet in state.enemy_planets()
                    if not any(fleet.destination_planet == planet.ID for fleet in state.my_fleets())
                    and strongest_planet.num_ships > planet.num_ships]
    if not target_planets:
        target_planets = state.enemy_planets()

    weakest_planet = closest_planet(state, strongest_planet, target_planets)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else: 
        to_beat = population(state, strongest_planet, weakest_planet)
        # (4) Send exactly enough to destroy the enemy fleet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, to_beat + 1)

# Find the closest planet to a source planet from a list
def closest_planet(state, src_planet, planets):
    if not planets or planets[0] is None:
        return None
    min_distance = state.distance(src_planet.ID, planets[0].ID)
    target_planet = planets[0]
    for planet in planets:
        if state.distance(src_planet.ID, planet.ID) < min_distance:
            min_distance = state.distance(src_planet.ID, planet.ID)
            target_planet = planet
    return target_planet

# Calculate the population growth of a planet based off the time it would take to get there.
def population(state, src_planet, dst_planet):
    return dst_planet.num_ships + \
        dst_planet.growth_rate * state.distance(src_planet.ID, dst_planet.ID)

def spread_to_weakest_neutral_planet(state):
    # (2) Find my strongest planet that doesn't already have a fleet out.
    source_planets = [planet for planet in state.my_planets()
                      if not any(fleet.source_planet == planet.ID for fleet in state.my_fleets())]
    if not source_planets:
        source_planets = state.my_planets()

    strongest_planet = max(source_planets, key=lambda t: t.num_ships, default=None)

    if not strongest_planet:
        # No legal source
        return False

    # (3) Find the closest enemy planet that my planet can beat.
    target_planets = [planet for planet in state.neutral_planets()
                    if not any(fleet.destination_planet == planet.ID for fleet in state.my_fleets())
                    and strongest_planet.num_ships > planet.num_ships]
    if not target_planets:
        target_planets = state.neutral_planets()

    weakest_planet = closest_planet(state, strongest_planet, target_planets)

    if not weakest_planet:
        # No legal destination
        return False

    to_beat = weakest_planet.num_ships + 1
    # (4) Send enough ships to defeat the population, plus half for a buffer
    return issue_order(state, strongest_planet.ID, weakest_planet.ID, to_beat * 1.5)
