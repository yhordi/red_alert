from ships import *

class Controller(object):

    player_info = {
        'name': 'Player',
        'ship_id': '0',
        'ship': 'none'
        }

    def get_player_name(self):
        player_name = raw_input("Type in your last name and press enter.\n>>>")
        self.player_info.update({'name': player_name})


    def scout_selection(self):
        scout = Scout()
        scout.report()

    def fighter_selection(self):
        fighter = Fighter()
        fighter.report()

    def get_player_ship(self, ship):
        self.player_info.update({'ship_id': ship})
        if ship == '2':
          self.player_info.update({'ship': 'Fighter'})
        else:
          self.player_info.update({'ship': 'Scout'})

    def ship_confirm(self):

        ship_confirmation = raw_input("Are you sure? y or n >> ")
        if ship_confirmation == 'y':
          pass
        elif ship_confirmation == 'n':
          view.ship_selection()
        else:
          view.y_or_n()

class View(object):

    def welcome(self):
        print """
              ______ ___________    ___   _      ___________ _____
              | ___ \  ___|  _  \  / _ \ | |    |  ___| ___ \_   _|
              | |_/ / |__ | | | | / /_\ \| |    | |__ | |_/ / | |
              |    /|  __|| | | | |  _  || |    |  __||    /  | |
              | |\ \| |___| |/ /  | | | || |____| |___| |\ \  | |
              \_| \_\____/|___/   \_| |_/\_____/\____/\_| \_| \_/
              """

    def player_report(self):
        print self.player_info

    def ship_selection(self):
        print "Welcome Captain %s. please select your ship:" % controller.player_info['name']
        print "_"* 50
        print "1. SCOUT"
        controller.scout_selection()
        print "_"* 50
        print "2. FIGHTER"
        controller.fighter_selection()
        player_ship = raw_input("Enter the number of your selection >> ")
        controller.get_player_ship(player_ship)
        print "You selected %s." % controller.player_info['ship']
        print "Please confirm."
        controller.ship_confirm()

    def y_or_n(self):
      print "Press y or n and press enter"
      controller.ship_confirm()


view = View()
controller = Controller()
view.welcome()
controller.get_player_name()
view.ship_selection()
