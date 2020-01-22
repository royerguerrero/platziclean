class SlackOfPlates:

    def __init__(self):
        self.slack_of_plates = []
        self.clean_dishes = 0


    def add_dish(self):
        self.slack_of_plates.append('\______/')
        print('d[o_0]b >> Añadiendo plato')

    def remove_dish(self):
        if len(self.slack_of_plates) <= 0:
            print('d[o_0]b >> No quedan platos para lavar')
        else:
            self.slack_of_plates.pop()
            self.clean_dishes += 1
            print('d[o_0]b >> Plato Lavado')


    def list_slack_of_plates(self):
        print(f'd[o_0]b >> La totalidad de los paltos para lavar son: {len(self.slack_of_plates)}')
        print(f'd[o_0]b >> Los platos lavados en esta session son: {self.clean_dishes} \n')
        for plate in self.slack_of_plates:
            print('\t \t \t', plate)