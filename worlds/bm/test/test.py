from . import BMTestBase

class TestTickle(BMTestBase):
    def test_beatable(self):
        self.assertBeatable(True)

        print("This prints if game is Beatable")

    def test_dependency_crusher(self):
        locations = ["Crusher Beam Pickup"]
        items = [["Hyper Beam", "Hover Upgrade", "Key", "Wall 1", "Wall 2"]]

        self.assertAccessDependency(locations, items, True)
        print("This Prints if Crusher Beam can be reached with listed Item")

     #def test_dependency_bossreachable(self):
     #   locations = ["Plutonium Boss Defeated"]
      #  items = [["Hover Upgrade", "Hyper Beam", "Crusher Beam"]]

      #  self.assertAccessDependency(locations, items, True)
      #  print("This Prints if Boss Can Be Reached With listed Items")

