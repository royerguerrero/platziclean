from dishes import SlackOfPlates

def bot():
    while True:
        command = input('''
        d[o_0]b >> Hola soy tu pallet washer 3000, que puedo hacer por ti?
        d[o_0]b >> Seleciona una opcion:
                   [A]ñadir un plato
                   [L]avar un plato
                   [C]ontar el numero de platos a lavar
                   [S]alir
        
        ''').lower()

        if command == 'a':
            dishes.add_dish()
        elif command == 'l':
            dishes.remove_dish()
        elif command == 'c':
            dishes.list_slack_of_plates()
        elif command == 's':
            break
        else:
            print('d[o_0]b >> Comando invalido intentalo nuevamente')


if __name__ == "__main__":
    dishes = SlackOfPlates()
    print("""
    __________.__                .__  _________ .__                        
    \______   \  | _____  _______|__| \_   ___ \|  |   ____ _____    ____  
     |     ___/  | \__  \ \___   /  | /    \  \/|  | _/ __ \\__  \  /    \ 
     |    |   |  |__/ __ \_/    /|  | \     \___|  |_\  ___/ / __ \|   |  |
     |____|   |____(____  /_____ \__|  \______  /____/\___  >____  /___| _/
    """)
    bot()
