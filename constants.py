GAME_SESSION_TIMEOUT = 300  # in seconds

LEVELS = {
    1: 'Starting Point',
    2: 'The Plains',
    3: 'The Volcano',
    4: 'The Fortress',
    5: 'The Final Dungeon',
}

ITEMS = {
    'sword': {'damage': 10, 'type': 'weapon'},
    'shield': {'defense': 5, 'type': 'armor'},
    'health_potion': {'heal': 20, 'type': 'consumable'},
}

PLAYER_STATES = [
    'idle',
    'running',
    'attacking',
    'defending',
    'dead',
]

ENEMY_TYPES = {
    'goblin': {'health': 30, 'damage': 5},
    'troll': {'health': 50, 'damage': 10},
}

MAX_PLAYERS = 4

FPS = 60  # frames per second

def get_level_name(level_number):
    return LEVELS.get(level_number, 'Unknown Level')

# Function to get item details by name

def get_item_details(item_name):
    return ITEMS.get(item_name, None)

# Function to check if a player state is valid

def is_valid_player_state(state):
    return state in PLAYER_STATES

