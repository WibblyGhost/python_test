import sys
from isort import file
from utils.csv_tools import csv_reader


class Intersection:
    """
    Defines an intersection which can be made up from four roads and each set their own CPM/weight
    """

    def __init__(
        self, north: int = 5, east: int = 5, south: int = 5, west: int = 5
    ) -> None:
        """
        Initialization of the class
        """
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.units = "CPM"

    def sum_all_roads(self) -> int:
        """
        Adds the CPM value of all intersecting roads
        """
        return self.north + self.east + self.south + self.west

    def __str__(self) -> None:
        """
        String representation of the class
        """
        return f"north: {self.north}, east: {self.east}, south: {self.south}, west: {self.west}"

    # TODO: 2
    def set_road(self, *args):
        """
        Sets CPM value of a given road in interactive python
        """
        if len(args) > 1:
            if args[0] == "north":
                self.north = args[1]
            elif args[0] == "east":
                self.east = args[1]
            elif args[0] == "south":
                self.south = args[1]
            elif args[0] == "west":
                self.east = args[1]
            else:
                print(
                    "Input a road direction [north, east, south, west] followed by a CPM [0..20] etc"
                )
        else:
            print(
                "Input a road direction [north, east, south, west] followed by a CPM [0..20] etc"
            )
        print(self.__str__())


class ControlCircuit:
    """
    Decides on what intersection type to use with given CPM values of each road
    """

    def __init__(
        self,
        intersection: Intersection,
        roundabout_cost=100000,
        stop_signs_cost=40000,
        traffic_light_cost=200000,
    ) -> None:
        """
        Initialization
        """
        self.roundabout = None
        self.stop_signs = None
        self.traffic_lights = None
        self.weights = {}
        self.intersection = intersection
        self.total_cpm = intersection.sum_all_roads()

        # DONE 6.
        # Convert these to a tuple instead
        self.roundabout_cost = roundabout_cost
        self.stop_signs_cost = stop_signs_cost
        self.traffic_lights_cost = traffic_light_cost

    def set_cpm_per_dollar(self, *args):
        """
        Sets cost value for control signals through interactive python
        """
        if len(args) > 1:
            if args[0] == "roundabout":
                self.roundabout_cost = args[1]
            elif args[0] == "stop_sign":
                self.stop_signs_cost = args[1]
            elif args[0] == "traffic_lights":
                self.traffic_lights_cost = args[1]
            else:
                print("Bad args for set_cpm_per_dollar")
        else:
            print("Bad args for set_cpm_per_dollar")
        print(self.__str__())

    def get_cpm_per_dollar(self):
        """
        Returns the set dollar amounts for the control signals
        """
        return {
            "roundabout": self.roundabout / self.roundabout_cost,
            "stop_signs": self.stop_signs / self.stop_signs_cost,
            "traffic_lights": self.traffic_lights / self.traffic_lights_cost,
        }

    def __str__(self) -> str:
        """
        Returns string representation of the class
        """
        return f"roundabout: {self.roundabout}, stop_signs: {self.stop_signs}, traffic_lights: {self.traffic_lights}"

    def _get_weights(self) -> dict:
        """
        Gets weights of given control types
        """
        self.weights = {
            "roundabout": self.roundabout,
            "stop_sign": self.stop_signs,
            "traffic_light": self.traffic_lights,
        }
        return self.weights

    def decide_weights(self) -> None:
        """
        Returns the correct type of control circuit for intersection
        """
        # TODO: 5.
        high_cpm = 20
        low_cpm = 10

        intersection = self.intersection
        road_north_south = intersection.north + intersection.south
        road_east_west = intersection.west + intersection.east

        roundabout_modifier = 0

        if road_north_south >= (high_cpm / 2) and road_east_west <= (low_cpm / 2):
            print("roundabout modifier")
            roundabout_modifier += 0.1

        # TODO: Split into different function if possible
        # Refer to given table
        if self.total_cpm >= high_cpm:
            self.roundabout = 0.5 + roundabout_modifier
            self.stop_signs = 0.2
            self.traffic_lights = 0.9
        elif high_cpm > self.total_cpm >= low_cpm:
            self.roundabout = 0.75 + roundabout_modifier
            self.stop_signs = 0.3
            self.traffic_lights = 0.75
        elif self.total_cpm < low_cpm:
            self.roundabouts = 0.9 + roundabout_modifier
            self.stop_signs = 0.4
            self.traffic_lights = 0.3
        else:
            print("FAIL")
            sys.exit()
        print(self.__str__())

        weights_dict = self._get_weights()
        print(
            f"You should use a {max(weights_dict, key=weights_dict.get)} it has a weight value of, {max(weights_dict.values())}"
        )

    @property
    def print_decision(weights: dict) -> None:
        print(max(weights.values()))


# TODO: 3.
# def model_csv_data(table: list) -> None:
#     for item in table:
#         new_intersection = Intersection()

#         count = 1
#         print(item[count])
#         count += 2
#     # intersections_dict = Convert(table)
#     # print(intersections_dict)
#     # for item in table:
#         # print(item)


def main():
    """
    Main runtime of our council intersections program
    """
    print("hello")
    # Get road weights
    new_intersection = Intersection(5, 1, 5, 1)
    print(new_intersection)

    # Calculate control circuit
    control = ControlCircuit(new_intersection)
    control.decide_weights()

    # TODO: 3.
    # table = csv_reader(file_path="./intersections.csv")
    # model_csv_data(table=table)


def main_interactive():
    """
    Definitely not well fleshed out but it does work, given more time I would implement *args into all the functions
    to allow for a more interactive experience rather than a coding experience.
    """
    print(
        "Run command, new_intersection = Intersection()\nnew_intersection.set_road(direction, CPM)"
    )
    print("then run ControlCircuit(new_intersection).decide_weights()")
    print("set costs with ControlCircuit().set_cpm_per_dollar(controle_type, value)")


if __name__ == "__main__":
    """
    More docstrings
    """
    # TODO: 2 If you want to run interactively comment out main() and uncomment main_interactive()
    main()
    # main_interactive()


# EXTENSIONS
"""
1. DONE -> Look at 2
2. DONE - Kinda, needs more fleshing, can be done through "py -i" running Intersection().set_road(*args)
3. FIXME - Got the CSV reader working, need to flesh out converting list into dictionary then running the functions
4. TODO - Requires making a table or dictionaries within dictionaries
5. DONE
6. DONE - Easy, just add new variables to the defined roads in the class, -> Basic version
7.
8.
9.
10.

Not enough time to do rest, otherwise I would
"""
