import pygame

from menu.button import Button, print_text
import main


def show_menu():
    start_button = Button(300, 70)
    records_button = Button(300, 70)
    about_button = Button(300, 70)
    exit_button = Button(300, 70)

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        main.RenderProperties.WINDOW.blit(main.RenderProperties.SPACE_MENU_IMAGE, (0, 0))
        start_button.draw(100, 200, 'START GAME', start_action, 40)
        records_button.draw(100, 280, 'RECORDS', None, 40)
        about_button.draw(100, 360, 'ABOUT', about_action, 40)
        exit_button.draw(100, 440, 'EXIT', exit_action, 40)
        pygame.display.update()


def start_action():
    return main.start_game()


def exit_action():
    exit()


def about_action():
    back_button = Button(150, 60)
    about = True
    while about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        main.RenderProperties.WINDOW.fill('gray')
        back_button.draw(170, 700, 'BACK', show_menu, font_size=40)
        print_text('The player controls the cannon ', 25, 190, font_size=25)
        print_text('at the bottom of the screen, ', 25, 225, font_size=25)
        print_text('which can move only horizontally. ', 25, 260, font_size=25)
        print_text('The aliens moves both horizontally ', 25, 295, font_size=25)
        print_text('and vertically. The cannon can be', 25, 330, font_size=25)
        print_text('controlled to shoot laser to destroy', 25, 365, font_size=25)
        print_text('the aliens while the aliens, will', 25, 400, font_size=25)
        print_text('randomly shoot towards the cannon.', 25, 435, font_size=25)
        pygame.display.update()


def game_over():
    main.RenderProperties.WINDOW.fill('black')
    back_to_menu_button = Button(320, 60)
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        main.RenderProperties.WINDOW.fill((200, 98, 90))
        back_to_menu_button.draw(100, 700, 'BACK TO MENU', show_menu, 40)
        print_text('GAME', 110, 100, font_size=80)
        print_text('OVER', 110, 200, font_size=80)
        pygame.display.update()
