import time
import logging

class GameEvent:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data
        self.timestamp = time.time()

    def __repr__(self):
        return f'<GameEvent(type={self.event_type}, data={self.data})>'

class EventHandler:
    def __init__(self):
        self.events = []
        self.logger = logging.getLogger(__name__)

    def add_event(self, event_type, data):
        event = GameEvent(event_type, data)
        self.events.append(event)
        self.logger.info(f'Event added: {event}')

    def process_events(self):
        while self.events:
            event = self.events.pop(0)
            self.handle_event(event)

    def handle_event(self, event):
        # Placeholder for event handling logic
        self.logger.debug(f'Handling event: {event}')
        # Handle specific event types here

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    handler = EventHandler()
    handler.add_event('player_joined', {'username': 'player1'})
    handler.process_events()