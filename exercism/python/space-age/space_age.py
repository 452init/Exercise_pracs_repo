class SpaceAge:
    earth_year_in_seconds = 31_557_600
    mercury = 0.2408467
    venus = 0.61519726
    earth = 1.0
    saturn = 29.447498
    mars = 1.8808158
    jupiter = 11.862615
    uranus = 84.016846
    neptune = 164.79132
    def __init__(self, seconds):
        self.seconds = seconds
    def on_mercury(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.mercury
        return (round(age_on_planet, 2))
    def on_venus(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.venus
        return (round(age_on_planet, 2))
    def on_earth(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.earth
        return (round(age_on_planet, 2))
    def on_mars(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.mars
        return (round(age_on_planet, 2))
    def on_jupiter(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.jupiter
        return (round(age_on_planet, 2))
    def on_saturn(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.saturn
        return (round(age_on_planet, 2))
    def on_uranus(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.uranus
        return (round(age_on_planet, 2))
    def on_neptune(self):
        age_in_earth_years = self.seconds / self.earth_year_in_seconds
        age_on_planet = age_in_earth_years / self.neptune
        return (round(age_on_planet, 2))
