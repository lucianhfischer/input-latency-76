import time

class Game:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_game(self):
        self.start_time = time.time()
        print("Game started!")

    def end_game(self):
        self.end_time = time.time()
        elapsed_time = self.calculate_elapsed_time()
        print(f"Game ended! Duration: {elapsed_time} seconds")

    def calculate_elapsed_time(self):
        if self.start_time is None:
            return 0
        return self.end_time - self.start_time if self.end_time else time.time() - self.start_time

# Usage example:
if __name__ == '__main__':
    game = Game()
    game.start_game()
    time.sleep(2)  # Simulate game play time
    game.end_game()