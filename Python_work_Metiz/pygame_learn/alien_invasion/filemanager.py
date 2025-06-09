import os
import json

class FileManager():

    def __init__(self):
        """Initial resourses for File manager."""
        if not os.path.exists('data/data.json'):
            with open('data/data.json', 'w') as f:
                json.dump({'record': 0}, f)


    def load_high_score(self):
        """Load files."""
        with open('data/data.json', 'r') as f:
            data = json.load(f)
            self.current_high_score = data.get('record', 0)

    def save_new_high_score(self, new_high_score):
        """Save new high score in data.json."""
        with open('data/data.json', 'r') as f:
            data = json.load(f)
        data['record'] = new_high_score
        with open('data/data.json', 'w') as f:
            json.dump(data, f)