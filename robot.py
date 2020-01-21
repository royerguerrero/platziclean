class SlackOfPlates:

    def __init__(self):
        self.slack_of_plates = []

    def add_dish(self):
        self.slack_of_plates.append('plato')

    def remove_dish(self):
        self.slack_of_plates.pop()

    def list_slack_of_plates(self):
        for idx in enumerate(self.slack_of_plates):
            print(idx)

bot = SlackOfPlates()

bot.add_dish()
bot.add_dish()
bot.add_dish()
bot.add_dish()

bot.list_slack_of_plates()

bot.remove_dish()

bot.list_slack_of_plates()
