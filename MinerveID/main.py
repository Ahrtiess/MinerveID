from colorama import Fore
import time
import requests
from datetime import datetime
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_user_info(id_address):
    url = f"https://dashboard.botghost.com/api/public/tools/user_lookup/{id_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        avatar_id = data.get('avatar', "Non disponible")
        avatar_url = f"https://cdn.discordapp.com/avatars/{id_address}/{avatar_id}.png"
        
        creation_date = datetime.utcfromtimestamp(((int(id_address) >> 22) + 1420070400000) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        
        return {
            "Identifiant de l'utilisateur": id_address,
            "Nom d'utilisateur": data.get('username', "Non disponible"),
            "Nom d'affichage": data.get('global_name', "Non disponible"),
            "Photo de profil": avatar_url,
            "Nitro": "Non" if data.get('premium_type') == 0 else data.get('premium_type', "Non disponible"), 
            "Date de création du compte": creation_date
        }
    else:
        return {'Échec de la récupération des données'}

def display_user_info(user_info):
    """Affiche les informations de l'utilisateur."""
    clear_screen()
    print(logo)
    print()
    for key, value in user_info.items():
        print(f"{Fore.LIGHTBLUE_EX}{key}:{Fore.BLUE} {value}")
    print()
    time.sleep(10)

logo = f'''{Fore.LIGHTBLUE_EX}   
    __  ____                            ________     
   /  |/  (_)___  ___  ______   _____  /  _/ __ \    
  / /|_/ / / __ \/ _ \/ ___/ | / / _ \ / // / / /    
 / /  / / / / / /  __/ /   | |/ /  __// // /_/ /     
/_/  /_/_/_/ /_/\___/_/    |___/\___/___/_____/      
                                                     
         
{Fore.LIGHTBLUE_EX}made by ahrtiess
{Fore.LIGHTBLUE_EX}github.com/ahrtiess
'''

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print()
    ID = input(f"{Fore.LIGHTBLUE_EX}ID:{Fore.BLUE} ")
    user_info = get_user_info(ID)
    display_user_info(user_info)