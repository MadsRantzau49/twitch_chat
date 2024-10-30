# In find_open_game.py
import psutil


def find_open_game():

    game_processes = {
        "RocketLeague": "RocketLeague.exe",
        "Counter-Strike 2": "cs2.exe",
        "Trackmania": "Trackmania.exe"
    }
    for proc in psutil.process_iter(['name']):
        try:
            process_name = proc.info['name']
            for game_name, exe in game_processes.items():
                if process_name == exe:
                    print(f"{exe} is launched")
                    if game_name == "RocketLeague":
                        from games.rocket_league.RocketLeague import RocketLeague
                        return RocketLeague()  # Instantiate RocketLeague
                    # Add other games as needed
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(e)
    return None
