from random import randint
class Sector(object):

    def arrive(self):
        print "You have arrived in an empty sector"

    def depart(self):
        pass

    def scan(self):
        print "This sector, like most of space, is empty."

    def arrival_effect(self):
      pass

    def departure_effect(self):
      print "You will lose one fuel"

class Asteroid(Sector):

    def arrive(self):
      print "You have come out of warp in an asteroid field!"

    def scan(self):
      print "You are in an asteroid field."

    def arrival_effect(self):
      print "2 fuel or -2 shield or if no shield -1 hull"

class Nebula(Sector):

      def arrive(self):
        print "You have come out of warp in a nebula!"

class Wormhole(Sector):

      def arrive(self):
        print "You have come out of warp just outside the mouth of an unstable wormhole!"

class Planet(Sector):

    planets = ["Kohines", "Croigawa", "Uesnov", "Efclarvis", "Straeovis", "Esmpion"]

    def arrive(self):
      print "You have come out of warp near the planet %s" % self.planets[randint(1,6)]

class Starbase(Sector):

      designation = randint(523, 1846723)

      def arrive(self):
        print "You have come out of warp near Starbase %d " % self.designation

class Map(object):

    def jump(self):
        sector_generator = randint(1, 100)
        print sector_generator
        if sector_generator > 0 and sector_generator < 20:
            sector.arrive()
        elif sector_generator >= 20 and sector_generator < 40:
            asteroid.arrive()
        elif sector_generator >= 40 and sector_generator < 60:
            nebula.arrive()
        elif sector_generator >= 60 and sector_generator < 70:
            wormhole.arrive()
        elif sector_generator >= 70 and sector_generator < 85:
            planet.arrive()
        elif sector_generator >= 85 and sector_generator < 100:
            starbase.arrive()
        else:
          pass

space = Map()
sector = Sector()
asteroid = Asteroid()
nebula = Nebula()
wormhole = Wormhole()
planet = Planet()
starbase = Starbase()
space.jump()