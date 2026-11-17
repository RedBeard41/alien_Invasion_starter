from enum import Enum, auto
import json
from pathlib import Path
import warnings


class GameState(Enum):
    WAITING = auto()
    PLAYING = auto()
    GAME_OVER = auto()


class GameStats:
    # Track the current game's lives, score, level, and active status.

    def __init__(self, ship_limit, high_score_file=None):
        self.ship_limit = ship_limit
        self.high_score_file = (Path(high_score_file) if high_score_file is not None
                                else Path(__file__).resolve().parent / 'high_score.json')
        self.high_score = self.read_high_score()
        self.reset_stats()
        self.state = GameState.WAITING

    def read_high_score(self):
        """Load a valid record, or start at zero if no usable save exists."""
        try:
            data = json.loads(self.high_score_file.read_text(encoding='utf-8'))
            value = data.get('high_score') if isinstance(data, dict) else None
            return value if type(value) is int and value >= 0 else 0
        except (OSError, ValueError):
            return 0

    def save_high_score(self):
        """Replace the save atomically to avoid leaving a partial JSON file."""
        temporary_file = self.high_score_file.with_suffix('.tmp')
        try:
            temporary_file.write_text(
                json.dumps({'high_score': self.high_score}), encoding='utf-8')
            temporary_file.replace(self.high_score_file)
        except OSError as error:
            warnings.warn(f'Could not save high score: {error}', RuntimeWarning)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    @property
    def game_active(self):
        return self.state == GameState.PLAYING

    @property
    def waiting_to_start(self):
        return self.state == GameState.WAITING

    def reset_stats(self):
        self.lives_remaining = self.ship_limit
        self.score = 0
        self.level = 1
        self.state = GameState.PLAYING

    def add_score(self, points):
        if self.game_active:
            self.score += points
            self.update_high_score()

    def advance_level(self):
        if self.game_active:
            self.level += 1

    def lose_life(self):
        if not self.game_active:
            return
        if self.lives_remaining > 0:
            self.lives_remaining -= 1
        if self.lives_remaining == 0:
            self.state = GameState.GAME_OVER
