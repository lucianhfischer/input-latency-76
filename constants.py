from typing import Final

# Game settings constants
FPS: Final[int] = 60  # Frames per second
SCREEN_WIDTH: Final[int] = 1920  # Screen width in pixels
SCREEN_HEIGHT: Final[int] = 1080  # Screen height in pixels
PLAYER_SPEED: Final[float] = 5.0  # Player speed in units per second
GRAVITY: Final[float] = 9.81  # Gravity constant in m/s^2

# Color constants
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game state constants
STATE_MENU: Final[str] = 'menu'
STATE_PLAYING: Final[str] = 'playing'
STATE_PAUSED: Final[str] = 'paused'
STATE_GAME_OVER: Final[str] = 'game_over'

# Control key bindings
KEY_UP: Final[str] = 'w'
KEY_DOWN: Final[str] = 's'
KEY_LEFT: Final[str] = 'a'
KEY_RIGHT: Final[str] = 'd'

# Maximum values
MAX_PLAYERS: Final[int] = 4  # Max number of players in a game
MAX_LEVELS: Final[int] = 10  # Max number of game levels
