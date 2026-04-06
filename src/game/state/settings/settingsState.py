from game.state.settings.display import Display
from game.state.settings.keymapsSettings import KeymapsSettings

class SettingsState:
    def __init__(self, display: Display, keymapsSettings: KeymapsSettings):
        self.display: Display = display 
        self.keymapsSettings: KeymapsSettings = keymapsSettings
        pass

