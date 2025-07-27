import os

CONFIG_PATH = os.path.expanduser("~/.malehterminalrc")

VALID_COLORS = {
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
}

DEFAULT_SETTINGS = {
    "PROMPT_STYLE": "$USER@$OS $DIR$ ",
    "USER_COLOR": "red",
    "OS_COLOR": "red",
    "DIR_COLOR": "cyan",
    "SHOW_UPDATE_NOTIFICATION": "true",
}

def validate_color(value, default):
    if value.lower() in VALID_COLORS:
        return value.lower()
    return default

def load_settings(config_path=CONFIG_PATH):
    settings = {}
    if not os.path.exists(config_path):
        return settings

    with open(config_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                settings[key.strip()] = value.strip().strip('"').strip("'")
    return settings


def create_settings(config_path=CONFIG_PATH):
    if os.path.exists(config_path):
        return False

    with open(config_path, "w") as file:
        for key, value in DEFAULT_SETTINGS.items():
            file.write(f"{key}=\"{value}\"\n")
    return True


def get_settings():
    user_settings = load_settings()
    settings = DEFAULT_SETTINGS.copy()
    settings.update(user_settings)

    settings["USER_COLOR"] = validate_color(
        user_settings.get("USER_COLOR", settings["USER_COLOR"]),
        DEFAULT_SETTINGS["USER_COLOR"]
    )
    settings["OS_COLOR"] = validate_color(
        user_settings.get("OS_COLOR", settings["OS_COLOR"]),
        DEFAULT_SETTINGS["OS_COLOR"]
    )
    settings["DIR_COLOR"] = validate_color(
        user_settings.get("DIR_COLOR", settings["DIR_COLOR"]),
        DEFAULT_SETTINGS["DIR_COLOR"]
    )

    return settings
