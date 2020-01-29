import commands
from controllers.participante_controller import route as participante_route

run = True

while run:
    command = input('$>> ')
    if command in commands.EXIT:
        run = False
    elif command.split(' ')[0] in commands.PARTICIPANTS:
       participante_route(command.split(' ')[1])

