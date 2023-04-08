from django.db import models


class Island(models.Model):
    name = models.CharField(max_length=200)

    def can_reach(self, island, *, by_ship):
        # "Return True if one can reach the @island using a @by ship"
        main = self.ships.first()
        secondary = island.ships.first()
        return by_ship.name == main.name and by_ship.name == secondary.name


class Ship(models.Model):
    name = models.CharField(max_length=200)
    islands = models.ManyToManyField(Island, related_name='ships')
