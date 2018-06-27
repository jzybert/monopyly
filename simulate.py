"""
Simulate a single character moving around a monopoly board to see the
percentage of landing on each square.
"""
import enum
import random

NUMBER_OF_SQUARES = 40


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

SQUARE_INDEX_GO = 0
SQUARE_INDEX_READING_RR = 5
SQUARE_INDEX_CHANGE_1 = 7
SQUARE_INDEX_JAIL = 10
SQUARE_INDEX_ST_CHARLES = 11
SQUARE_INDEX_ELECTRIC_CO = 12
SQUARE_INDEX_PENN_RR = 15
SQUARE_INDEX_CHANCE_2 = 22
SQUARE_INDEX_ILLINOIS = 24
SQUARE_INDEX_BO_RR = 25
SQUARE_INDEX_WATER_WORKS = 28
SQUARE_INDEX_SHORT_LINE_RR = 35
SQUARE_INDEX_CHANCE_3 = 36
SQUARE_INDEX_BOARDWALK = 39

cc_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
CC_CARD_NUMBER_ADVANCE_TO_GO = 1
CC_CARD_NUMBER_GET_OUT_OF_JAIL_FREE = 2
CC_CARD_NUMBER_GO_TO_JAIL = 3


chance_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
C_CARD_NUMBER_ADVANCE_TO_GO = 1
C_CARD_NUMBER_ADVANCE_TO_ILLINOIS = 2
C_CARD_NUMBER_ADVANCE_TO_ST_CHARLES = 3
C_CARD_NUMBER_ADVANCE_TO_NEAREST_UTILITY = 4
C_CARD_NUMBER_ADVANCE_TO_NEAREST_RAILROAD = 5
C_CARD_NUMBER_GET_OUT_OF_JAIL_FREE = 6
C_CARD_NUMBER_GO_BACK_3 = 7
C_CARD_NUMBER_GO_TO_JAIL = 8
C_CARD_NUMBER_GO_TO_READING = 9
C_CARD_NUMBER_GO_TO_BOARDWALK = 10


class Player:
    """
    Player class holding information about the Player's movements and dice 
    rolls.
    """
    def __init__(self):
        self.index_position = 0
        self.in_jail = False
        self.has_get_out_of_jail_free_card = False
        self.number_of_doubles_rolled = 0
        self.number_of_rounds = 0

    def simulate_round(self):
        dice_value, is_double = self.roll()
        self.move(dice_value, is_double)
        self.evaluate_position()

    @staticmethod
    def roll():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        is_double = dice_1 == dice_2
        return dice_1 + dice_2, is_double

    def move(self, number_of_spaces, is_double):
        # 3 consecutive doubles will put you in jail
        if is_double:
            self.number_of_doubles_rolled += 1
        else:
            self.number_of_doubles_rolled = 0
        # Move to appropriate spot on board
        if self.number_of_doubles_rolled == 3:
            self.move_to_jail()
        else:
            new_position = self.index_position + number_of_spaces
            self.index_position = new_position % NUMBER_OF_SQUARES

    def move_to_go(self):
        self.index_position = SQUARE_INDEX_GO

    def move_to_jail(self):
        self.index_position = SQUARE_INDEX_JAIL
        self.in_jail = True
        self.number_of_doubles_rolled = 0

    def move_to_illinois(self):
        self.index_position = SQUARE_INDEX_ILLINOIS

    def move_to_st_charles(self):
        self.index_position = SQUARE_INDEX_ST_CHARLES

    def move_to_nearest_utility(self):
        position = self.index_position
        if (position == SQUARE_INDEX_CHANGE_1
                or position == SQUARE_INDEX_CHANCE_2):
            self.index_position = SQUARE_INDEX_ELECTRIC_CO
        else:
            self.index_position = SQUARE_INDEX_WATER_WORKS

    def move_to_nearest_railroad(self):
        position = self.index_position
        if position == SQUARE_INDEX_CHANGE_1:
            self.index_position = SQUARE_INDEX_PENN_RR
        elif position == SQUARE_INDEX_CHANCE_2:
            self.index_position = SQUARE_INDEX_BO_RR
        else:
            self.index_position = SQUARE_INDEX_READING_RR

    def move_to_reading(self):
        self.index_position = SQUARE_INDEX_READING_RR

    def move_to_boardwalk(self):
        self.index_position = SQUARE_INDEX_BOARDWALK

    def evaluate_position(self):
        global cc_cards, chance_cards
        position_type = squares[self.index_position]["type"]
        if position_type == SquareType.GO_TO_JAIL:
            self.move_to_jail()
        elif position_type == SquareType.COMMUNITY_CHEST:
            if len(cc_cards) == 0:
                shuffle_community_chest_deck()
            card_index = random.randint(0, len(cc_cards))
            card = cc_cards.pop(card_index)
            if card == CC_CARD_NUMBER_ADVANCE_TO_GO:
                self.move_to_go()
            elif card == CC_CARD_NUMBER_GET_OUT_OF_JAIL_FREE:
                self.has_get_out_of_jail_free_card = True
            elif card == CC_CARD_NUMBER_GO_TO_JAIL:
                self.move_to_jail()
        elif position_type == SquareType.CHANCE:
            if len(chance_cards) == 0:
                shuffle_chance_deck()
            card_index = random.randint(0, len(chance_cards))
            card = chance_cards.pop(card_index)
            moved = False  # Flag to see if the Player moved
            if card == C_CARD_NUMBER_ADVANCE_TO_GO:
                moved = True
                self.move_to_go()
            elif card == C_CARD_NUMBER_ADVANCE_TO_ILLINOIS:
                moved = True
                self.move_to_illinois()
            elif card == C_CARD_NUMBER_ADVANCE_TO_ST_CHARLES:
                moved = True
                self.move_to_st_charles()
            elif card == C_CARD_NUMBER_ADVANCE_TO_NEAREST_UTILITY:
                moved = True
                self.move_to_nearest_utility()
            elif card == C_CARD_NUMBER_ADVANCE_TO_NEAREST_RAILROAD:
                moved = True
                self.move_to_nearest_railroad()
            elif card == C_CARD_NUMBER_GET_OUT_OF_JAIL_FREE:
                self.has_get_out_of_jail_free_card = True
            elif card == C_CARD_NUMBER_GO_BACK_3:
                moved = True
                new_position = self.index_position - 3
                self.index_position = new_position % NUMBER_OF_SQUARES
            elif card == C_CARD_NUMBER_GO_TO_JAIL:
                moved = True
                self.move_to_jail()
            elif card == C_CARD_NUMBER_GO_TO_READING:
                moved = True
                self.move_to_reading()
            elif card == C_CARD_NUMBER_GO_TO_BOARDWALK:
                moved = True
                self.move_to_boardwalk()
            # Reevaluate position if a card moved Player
            if moved:
                self.evaluate_position()


def simulate(number_of_turns):
    """
    Simulate a player moving around a Monopoly board.

    :param number_of_turns:
    :return: void
    """
    player = Player()
    for ii in range(number_of_turns):
        print("Current Position: {}".format(player.index_position))
        player.simulate_round()
        print("New Position: {}\n".format(player.index_position))


def shuffle_community_chest_deck():
    """
    Shuffles a new community chest deck.

    :return:
    """
    global cc_cards
    cc_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    random.shuffle(cc_cards)


def shuffle_chance_deck():
    """
    Shuffles a new chance deck.

    :return:
    """
    global chance_cards
    chance_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    random.shuffle(chance_cards)


def init():
    """
    Initializes a new game. Community Chest and Chance decks are shuffled.
    :return: void
    """
    shuffle_community_chest_deck()
    shuffle_chance_deck()


if __name__ == "__main__":
    init()
    simulate(10)
