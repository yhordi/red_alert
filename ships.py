class Ship(object):

    hull = 3
    fuel = 10
    shield = 3
    laser = 1

    def status(self):
        print "hull status at %d" % self.hull
        print "fuel tank at %d" % self.fuel
        print "shield at %d" % self.shield
        print "laser at %d" % self.laser

class Scout(Ship):

    hull = 3
    fuel = 15
    shield = 3
    laser = 1

class Fighter(Ship):

    hull = 5
    fuel = 9
    shield = 4
    laser = 2

class EnemyFighter(Ship):

    hull = 5
    fuel = 10
    shield = 5
    laser = 3

class EnemyCorvette(Ship):

    hull =  10
    fuel = 10
    shield = 10
    laser = 5

assert Scout.hull == 3
assert Fighter.fuel == 9
assert EnemyFighter.shield == 5
assert EnemyCorvette.laser == 5