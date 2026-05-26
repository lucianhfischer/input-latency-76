class LatencyError(Exception):
    """
    Exception raised for latency-related errors.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class InputError(Exception):
    """
    Exception raised for errors with user input.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class GameOverError(Exception):
    """
    Exception raised when a game session ends unexpectedly.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

if __name__ == '__main__':
    try:
        raise LatencyError("Input latency is too high!")
    except LatencyError as e:
        print(f'LatencyError: {e.message}')
    
    try:
        raise InputError("Invalid input received!")
    except InputError as e:
        print(f'InputError: {e.message}')
    
    try:
        raise GameOverError("The game has ended unexpectedly!")
    except GameOverError as e:
        print(f'GameOverError: {e.message}')