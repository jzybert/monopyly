"""
Simulate a single character moving around a monopoly board to see the
percentage of landing on each square.
"""
import enum


class SquareType(enum.Enum):
    """
    Enumeration class representing what type a square can be.
    """
    GO = 1
    DARK_BLUE = 2
    TAX = 3
    RAILROAD = 4
    LIGHT_BLUE = 5
    CHANCE = 6
    JAIL = 7
    PURPLE = 8
    UTILITY = 9
    ORANGE = 10
    COMMUNITY_CHEST = 11
    FREE_PARKING = 12
    RED = 13
    YELLOW = 14
    GO_TO_JAIL = 15
    GREEN = 16
    BLUE = 17


squares = [
    {"name": "Go", "type": SquareType.GO},
    {"name": "Mediterranean Avenue", "type": SquareType.DARK_BLUE},
    {"name": "Community Chest", "type": SquareType.COMMUNITY_CHEST},
    {"name": "Baltic Avenue", "type": SquareType.DARK_BLUE},
    {"name": "Income Tax", "type": SquareType.TAX},
    {"name": "Reading Railroad", "type": SquareType.RAILROAD},
    {"name": "Central Avenue", "type": SquareType.LIGHT_BLUE},
    {"name": "Chance", "type": SquareType.CHANCE},
    {"name": "Vermont Avenue", "type": SquareType.LIGHT_BLUE},
    {"name": "Connecticut Avenue", "type": SquareType.LIGHT_BLUE},
    {"name": "Jail", "type": SquareType.JAIL},
    {"name": "St. Charles Place", "type": SquareType.PURPLE},
    {"name": "Electric Company", "type": SquareType.UTILITY},
    {"name": "States Avenue", "type": SquareType.PURPLE},
    {"name": "Virginia Avenue", "type": SquareType.PURPLE},
    {"name": "Pennsylvania Railroad", "type": SquareType.RAILROAD},
    {"name": "St. James Place", "type": SquareType.ORANGE},
    {"name": "Community Chest", "type": SquareType.COMMUNITY_CHEST},
    {"name": "Tennessee Avenue", "type": SquareType.ORANGE},
    {"name": "New York Avenue", "type": SquareType.ORANGE},
    {"name": "Free Parking", "type": SquareType.FREE_PARKING},
    {"name": "Kentucky Avenue", "type": SquareType.RED},
    {"name": "Chance", "type": SquareType.CHANCE},
    {"name": "Indiana Avenue", "type": SquareType.RED},
    {"name": "Illinois Avenue", "type": SquareType.RED},
    {"name": "B. & O. Railroad", "type": SquareType.RAILROAD},
    {"name": "Atlantic Avenue", "type": SquareType.YELLOW},
    {"name": "Ventnor Avenue", "type": SquareType.YELLOW},
    {"name": "Water Works", "type": SquareType.UTILITY},
    {"name": "Marvin Gardens", "type": SquareType.YELLOW},
    {"name": "Go To Jail", "type": SquareType.GO_TO_JAIL},
    {"name": "Pacific Avenue", "type": SquareType.GREEN},
    {"name": "North Carolina Avenue", "type": SquareType.GREEN},
    {"name": "Community Chest", "type": SquareType.COMMUNITY_CHEST},
    {"name": "Pennsylvania Avenue", "type": SquareType.GREEN},
    {"name": "Short Line", "type": SquareType.RAILROAD},
    {"name": "Chance", "type": SquareType.CHANCE},
    {"name": "Park Place", "type": SquareType.BLUE},
    {"name": "Luxury Tax", "type": SquareType.BLUE},
    {"name": "Board Walk", "type": SquareType.BLUE}
]