class Ship(object):

    status = {
        'hull': 3,
        'fuel': 10,
        'shield': 3,
        'laser': 1
    }

    def report(self):
        print "hull status at %d" % self.status['hull']
        print "fuel tank at %d" % self.status['fuel']
        print "shield at %d" % self.status['shield']
        print "laser at %d" % self.status['laser']

class Scout(Ship):

    status = {
        'hull': 3,
        'fuel': 15,
        'shield': 3,
        'laser': 1
        }

class Fighter(Ship):
    status = {
        'hull': 5,
        'fuel': 9,
        'shield': 4,
        'laser': 2
        }

class EnemyFighter(Ship):
    status = {
        'hull': 5,
        'fuel': 10,
        'shield': 5,
        ' laser': 3
        }

class EnemyCorvette(Ship):
    status = {
        'hull': 10,
        'fuel': 10,
        'shield': 10,
        'laser': 5
        }

assert Scout.status['hull'] == 3
assert Fighter.status['fuel'] == 9
assert EnemyFighter.status['shield'] == 5
assert EnemyCorvette.status['laser'] == 5
