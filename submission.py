# Tracy Hoang 
# CSCI 128 - Section F
# Create Performance Project: Choose Your Own Adventure Game
# References: tutorialspoint, pygame, jason semaan, geeksforgeeks, doug mcnally, reintech, stackoverflow

# genuinely one of the ugliest pieces of code ive ever written im sorry
# i feel like toby fox w/ all the if statements oh my god bruh

import pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()

# ----------------------- SET UP ----------------------------

# load music
pygame.mixer.music.load("save the princess.mp3") # shout out my friend rynn christner !!!
pygame.mixer.music.play(loops=-1)

# set up display 
width, height = 800, 800
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Save the Apricot!")
programicon = pygame.image.load('appricot icon.png')
pygame.display.set_icon(programicon)


# ---------------------- DEFINE EVERYTHING ------------------------

# colors
offwhite = (254, 238, 220)
orangeish = (218, 99, 65)
reddish = (136, 40, 19)

# fonts
font = pygame.font.Font("PixelOperator8-Bold.ttf", 30)

# assets
assets = {
    'textbox':pygame.transform.scale(pygame.image.load('textbox.png'), (width, height))
}

# images for dif locations
backgrounds = {
    'start': pygame.transform.scale(pygame.image.load('title_screen.png'), (width, height)),
    'shop': pygame.transform.scale(pygame.image.load('shop.png'), (width, height)),
    'forest': pygame.transform.scale(pygame.image.load('forest.png'), (width, height)),
    'path': pygame.transform.scale(pygame.image.load('path.png'), (width, height)),
    'castle': pygame.transform.scale(pygame.image.load('castle.png'), (width, height)),
    'room': pygame.transform.scale(pygame.image.load('room.png'), (width, height)),
    'bad': pygame.transform.scale(pygame.image.load('bad.png'), (width, height)),
    'good': pygame.transform.scale(pygame.image.load('good.png'), (width, height)),
    'neutral': pygame.transform.scale(pygame.image.load('neutral.png'), (width, height)),
    'letter': pygame.transform.scale(pygame.image.load('letter.png'), (width, height)),
    'quest_choices_paths': pygame.transform.scale(pygame.image.load('letter.png'), (width, height)),
}

# apricot sprites
apricot_sprites = {
    'apricot_neutral': pygame.transform.scale(pygame.image.load('apricot_neutral.png'), (width, height)),
    'apricot_happy': pygame.transform.scale(pygame.image.load('apricot_happy.png'), (width, height)),
    'apricot_mad': pygame.transform.scale(pygame.image.load('apricot_mad.png'), (width, height)),
    'apricot_neutral': pygame.transform.scale(pygame.image.load('apricot_neutral.png'), (width, height)),
    'apricot_oo': pygame.transform.scale(pygame.image.load('apricot_oo.png'), (width, height)),
    'apricot_sad': pygame.transform.scale(pygame.image.load('apricot_sad.png'), (width, height)),
    'apricot_apricot': pygame.transform.scale(pygame.image.load('apricot_apricot.png'), (width, height))
}

# some guy sprites
some_guy_sprites = {
    'some_guy_neutral': pygame.transform.scale(pygame.image.load('someguy_neutral.png'), (width, height)),
    'some_guy_dead':pygame.transform.scale(pygame.image.load('someguy_dead.png'), (width, height))
}

# starfruit sprites 
starfruit_sprites = {
    'starfruit_neutral': pygame.transform.scale(pygame.image.load('starfruit_neutral.png'), (width, height)),
    'starfruit_oo': pygame.transform.scale(pygame.image.load('starfruit_oo.png'), (width, height)),
    'starfruit_happy': pygame.transform.scale(pygame.image.load('starfruit_happy.png'), (width, height))
}

# dragon sprites
dragon_sprites = {
    'dragon_neutral': pygame.transform.scale(pygame.image.load('dragon_neutral.png'), (width, height)),
    'dragon_happy': pygame.transform.scale(pygame.image.load('dragon_happy.png'), (width, height)),
    'dragon_dead': pygame.transform.scale(pygame.image.load('dragon_dead.png'), (width, height))
}

# shop guy sprites
shopguy_sprites = {
    'shop_neutral': pygame.transform.scale(pygame.image.load('shop_neutral.png'), (width, height)),
    'shop_happy': pygame.transform.scale(pygame.image.load('shop_happy.png'), (width, height))
}

# ---------------------- BUTTONS -------------------------

button_rects = {
    'Start': pygame.Rect(300, 500, 200, 50),
    'Exit': pygame.Rect(300, 600, 200, 50),
    'Exit_2': pygame.Rect(300, 500, 200, 50),
    'Restart': pygame.Rect(300, 400, 200, 50),
    'Accept': pygame.Rect(100, 700, 200, 50),
    'Decline': pygame.Rect(500, 700, 200, 50),
    'Shop': pygame.Rect(300, 700, 150, 50),
    'Path': pygame.Rect(100, 700, 150, 50),
    'Talk': pygame.Rect(100, 700, 150, 50),
    'Forest': pygame.Rect(500, 700, 200, 50),
    'Fight': pygame.Rect(100, 700, 150, 50),
    'Go Back': pygame.Rect(100, 700, 150, 50),
    'Continue': pygame.Rect(500, 700, 250, 50),
    'Return': pygame.Rect(100, 700, 200, 50),
    'Shop_2': pygame.Rect(500, 700, 250, 50),

    # shop buttons 
    'Buy_Rough': pygame.Rect(650, 310, 100, 40),
    'Buy_Sleek': pygame.Rect(650, 390, 100, 30),
    'Buy_Apricots': pygame.Rect(650, 470, 100, 40),
    'Buy_Flowers': pygame.Rect(650, 550, 100, 40),
    'Shop_Exit': pygame.Rect(350, 700, 150, 50),
}

# ---------------------- DIALOGUE -------------------------

dialogue_sequences = {
    'letter_prompt': [
        {'char': None, 'text': 'You were sent a letter to save the princess!'},
        {'char': None, 'text': 'The castle is far and the journey may be dangerous.'},
        {'char': None, 'text': 'Do you accept this quest?'}
    ],
    'accept_quest': [
        {'char': None, 'text': 'You accepted the quest!'},
        {'char': None, 'text': 'You can visit the shop first or choose your journey:'},
        {'char': None, 'text': 'The long Path or the dangerous Forest.'}
    ],

    # SHOP ---------------------

    'shop_intro': [
        {'char': 'shop_neutral', 'text': '"Welcome to the best shop in the land!"'},
        {'char': 'shop_happy', 'text': '"I have everything you need, so please look around!"'},
    ],

    # PATH --------------------

    'path_intro':[
        {'char': None, 'text': 'You have decided to take the Path.'},
        {'char': None, 'text': 'As you walk along the path, you notice another princess.'},
        {'char': None, 'text': 'Will you speak to her?'}
    ],

    'starfruit_interaction': [
        {'char': 'starfruit_oo', 'text': '"Oh, Hello! You must be the chosen one."'},
        {'char': 'starfruit_neutral', 'text': '"I am glad someone is finally saving her..."'},
        {'char': 'starfruit_neutral', 'text': '"I miss her a lot..."'},
        {'char': 'starfruit_oo', 'text': '"Oh wait!"'},
        {'char': 'starfruit_oo', 'text': '"You should take these..."'},
        {'char': 'starfruit_happy', 'text': '"They will be useful for later!"'},
        {'char': 'starfruit_happy', 'text': 'You obtained apricots!'},
        {'char': 'starfruit_neutral', 'text': '"Thanks a lot!"'},
        {'char': None, 'text': 'After Princess Starfruit leaves,'},
        {'char': None, 'text': 'you decided to visit the shop on the way to the castle.'}
    ],

    # FOREST --------------------

    'forest_intro': [
        {'char': None, 'text': 'You have decided to venture through the Forest.'},
        {'char': None, 'text': 'While you were in the Forest, you noticed Some Guy...'},
        {'char': None, 'text': 'You deduced that Some Guy seems suspicous.'},
        {'char': None, 'text': 'Will you fight Some Guy?'}
    ],    

    'someguy_interaction_with_weapon': [
        {'char': 'some_guy_neutral', 'text': "You decide to fight Some Guy!"},
        {'char': 'some_guy_neutral', 'text': "You have a weapon... and he doesn't!"},
        {'char': 'some_guy_dead', 'text': "Some Guy is weak against you!"},
        {'char': 'some_guy_dead', 'text': "You have slain Some Guy!"},
        {'char': 'some_guy_dead', 'text': "Gained 100 gold!"},
        {'char': None, 'text': 'After defeating Some Guy,'},
        {'char': None, 'text': 'you decided to visit the shop on the way to the castle.'}
    ],

    'someguy_interaction_no_weapon': [
        {'char': 'some_guy_neutral', 'text': "You decide to fight Some Guy!"},
        {'char': 'some_guy_neutral', 'text': "But, you have no weapon..."},
        {'char': 'some_guy_neutral', 'text': "Oh no! Some Guy is way stronger than you!"},
        {'char': 'some_guy_neutral', 'text': "You have lost the battle with Some Guy..."},
    ],

    # BOTH PATH AND FOREST
    'continue_text': [
        {'char': None, 'text': "You decide to continue your journey."},
        {'char': None, 'text': "On the way to the castle, there lies another shop."},
        {'char': None, 'text': "You decide to head inside."}
    ],

    # CASTLE -----------------------
    'castle_prompt': [
        {'char': None, 'text': 'You have finally reached the castle.'},
        {'char': None, 'text': 'This is your final chance to go back.'},
        {'char': None, 'text': 'Ahead of you is a dangerous fight with the Dragon.'},
        {'char': None, 'text': 'Will you return back home or will you save the princess?'}
    ],

    # IF SOME GUY IS DEAD (CASTLE/APRICOT - TURN BACK)
    'some_guy_dead':[
        {'char': None, 'text': 'You decided to return home.'},
        {'char': None, 'text': 'However, blood stains your hands.'},
        {'char': None, 'text': "Turns out Some Guy wasn't suspicous at all!"},
        {'char': None, 'text': "You killed Some Guy, c'mon..."},
        {'char': None, 'text': "Sorry! But, you are now arrested for your crime."}
    ],

    # IF SOME GUY IS ALIVE (CASTLE/APRICOT - TURN BACK)
    'some_guy_alive': [
        {'char': None, 'text': 'You decided to return home.'},
        {'char': None, 'text': 'And got home safely!'},
    ],

    # DRAGON ----------------------------------
    'dragon_intro': [
        {'char': None, 'text': "You have decided to persue the princess and fight the Dragon."},
        {'char': 'dragon_neutral', 'text': "*dragon noises*"},
        {'char': 'dragon_happy', 'text': "*even more dragon noises*"},
    ],

    'dragon_weak_or_no_weapon': [
        {'char': 'dragon_happy', 'text': "As you fight the dragon..."},
        {'char': 'dragon_neutral', 'text': "You realize that he is much, much, stronger than you!"},
        {'char': 'dragon_neutral', 'text': 'He takes you down with one easy sweep!'},
        {'char': 'dragon_happy', 'text': 'You are now dead.'},
        {'char': 'dragon_happy', 'text': 'Hopefully somebody else can save the Princess now...'}
    ],

    'dragon_strong_weapon': [
        {'char': 'dragon_happy', 'text': "As you fight the dragon..."},
        {'char': 'dragon_happy', 'text': "You realize that you are stronger than him!"},
        {'char': 'dragon_neutral', 'text': 'You take him down with one easy sweep!'},
        {'char': 'dragon_dead', 'text': 'You defeated the dragon!'},
        {'char': 'dragon_dead', 'text': 'Now it is finally time to save the Princess!'},
    ],
    
    # APRICOT -----------------------

    'apricot_intro': [
        {'char': 'apricot_oo', 'text': '"Oh! Somebody is finally here to save me!"'},
        {'char': 'apricot_happy', 'text': '"Greetings!"'},
        {'char': 'apricot_neutral', 'text': '"I greatly appreciate that you took the journey to save me."'},
        {'char': 'apricot_neutral', 'text': '"I am Princess Apricot."'},
        {'char': 'apricot_neutral', 'text': '"It is a pleasure to finally meet my hero."'}
    ],

    'apricot_hasapricot': [
        {'char': 'apricot_oo', 'text': '"Oooo... I smell something on you..."'},
        {'char': 'apricot_neutral', 'text': '"Do you have apricots in your inventory..."'},
        {'char': 'apricot_happy', 'text': '"Or are you happy to see me?"'},
        {'char': 'apricot_happy', 'text': 'You take out the apricots from your inventory'},
        {'char': 'apricot_oo', 'text': '"Ah! You actually have apricots!"'},
        {'char': 'apricot_apricot', 'text': '"Thank you so much!"'},
        {'char': 'apricot_apricot', 'text': '"Now, let us get out of here!"'}
    ],

    'apricot_someguy_dead': [
        {'char': 'apricot_oo', 'text': '"Have you seen Some Guy?"'},
        {'char': 'apricot_neutral', 'text': '"I asked him to fetch me some apricots..."'},
        {'char': 'apricot_neutral', 'text': "You tell her that you fought and killed him."},
        {'char': 'apricot_neutral', 'text': '"..."'},
        {'char': 'apricot_sad', 'text': '"You... what?"'},
        {'char': 'apricot_mad', 'text': '"You... WHAT!?"'},
        {'char': 'apricot_mad', 'text': '"You... You... I cannot believe you!"'},
        {'char': 'apricot_mad', 'text': '"You are to be sent to jail IMMEDIATELY!"'},
        {'char': 'None', 'text': 'And... she was right! You were sent to jail immediately.'},
        {'char': 'None', 'text': "Maybe next time, don't kill Some Guy..."},
    ],

    'apricot_noapricot':[
        {'char': 'apricot_oo', 'text': '"Would you happen to have any apricots with you?"'},
        {'char': 'apricot_oo', 'text': 'You tell her you do not have any apricots'},
        {'char': 'apricot_mad', 'text': '"Ugh! Who do you think I am?"'},
        {'char': 'apricot_mad', 'text': '"The next time I see you, I want to smell some apricots!"'},
        {'char': 'apricot_mad', 'text': 'What a demanding princess!'},
        {'char': 'apricot_mad', 'text': 'You can either go back to the shop to buy her apricots,'},
        {'char': 'apricot_mad', 'text': 'Or... Just return home!'},
    ]
}

# ---------------------- FUNCTIONS ------------------------


# helps fit text in box --------------
def wrap_text(surface, text, font, rect, color, line_spacing = 10):
    
    # calc max width and starting x for center
    padding = 15
    max_text_width = rect.width - 2 * padding
    text_start_x = rect.x + padding
    line_height = font.get_height()

    # determine wrapped lines
    words = text.split(' ')
    wrapped_lines = []
    current_line = ''

    for word in words:
        test_line = current_line + ' ' + word if current_line else word
        test_surface = font.render(test_line, True, color)

        if test_surface.get_width() <= max_text_width:
            current_line = test_line
        else:
            if current_line:
                wrapped_lines.append(current_line)
            current_line = word
    wrapped_lines.append(current_line)

    # calc total height for center
    num_lines = len(wrapped_lines)
    total_text_height = (num_lines * line_height) + ((num_lines - 1) * line_spacing)

    # calc y position
    box_height = rect.height
    text_centered_y = rect.y + (box_height - total_text_height) // 2

    # draw the lines
    current_y = text_centered_y
    for line in wrapped_lines:
        line_surface = font.render(line, True, color)

        x_centered = text_start_x + (max_text_width - line_surface.get_width()) // 2

        surface.blit(line_surface, (x_centered, current_y))

        current_y += line_height + line_spacing

# dialogue --------------------------
def draw_dialogue(dialogue_key, line_index, current_bg_key):
    # makes sure bg is drawn
    screen.blit(backgrounds[current_bg_key], (0, 0))

    # get current line data
    line_data = dialogue_sequences[dialogue_key][line_index]
    char_sprite_key = line_data['char']
    text = line_data['text']

    # sprite lookup and drawing
    sprite_to_draw = None

    # checks character sprite
    if char_sprite_key in shopguy_sprites:
        sprite_to_draw = shopguy_sprites[char_sprite_key]
    elif char_sprite_key in apricot_sprites:
        sprite_to_draw = apricot_sprites[char_sprite_key]
    elif char_sprite_key in some_guy_sprites:
        sprite_to_draw = some_guy_sprites[char_sprite_key]
    elif char_sprite_key in dragon_sprites:
        sprite_to_draw = dragon_sprites[char_sprite_key]
    elif char_sprite_key in starfruit_sprites:
        sprite_to_draw = starfruit_sprites[char_sprite_key]

    if sprite_to_draw:
        screen.blit(sprite_to_draw, (0, 0))

    # draws the textbox
    screen.blit(assets['textbox'], (0, 0))

    # define area for the text
    text_rect = pygame.Rect(100,572,600,200)

    wrap_text(screen, text, font, text_rect, orangeish)


# draw the screen -----------
current_screen = 'start' # title screen
last_screen = 'start' # tracks the last screen just for shop LMAOO
current_bg = None

def draw_screen(screen_name):
    if screen_name in backgrounds:
        screen.blit(backgrounds[screen_name], (0, 0))

    # title screen -------------------------------------------------
    if screen_name == 'start':
        start_rect = button_rects['Start']
        exit_rect = button_rects['Exit']

        start_button_text = font.render('Start', True, offwhite)
        exit_button_text = font.render('Exit', True, offwhite)

        # start button
        pygame.draw.rect(screen, orangeish, start_rect)
        screen.blit(start_button_text, (start_rect.x + (start_rect.width - start_button_text.get_width()) // 2, start_rect.y + 15))
        
        # exit button
        pygame.draw.rect(screen, orangeish, exit_rect)
        screen.blit(exit_button_text, (exit_rect.x + (exit_rect.width - exit_button_text.get_width()) // 2, exit_rect.y + 15))

    # neutral ending --------------------------------
    elif screen_name == 'neutral':
        restart_rect = button_rects['Restart']
        exit_rect = button_rects['Exit_2']

        restart_button_text = font.render('Restart', True, offwhite)
        exit_button_text = font.render('Exit', True, offwhite)

        # restart button
        pygame.draw.rect(screen, orangeish, restart_rect)
        screen.blit(restart_button_text, (restart_rect.x + (restart_rect.width - restart_button_text.get_width()) // 2, restart_rect.y + 15))
        
        # exit button
        pygame.draw.rect(screen, orangeish, exit_rect)
        screen.blit(exit_button_text, (exit_rect.x + (exit_rect.width - exit_button_text.get_width()) // 2, exit_rect.y + 15)) 
        
    # bad ending ------------------------------------
    elif screen_name == 'bad':
        restart_rect = button_rects['Restart']
        exit_rect = button_rects['Exit_2']

        restart_button_text = font.render('Restart', True, offwhite)
        exit_button_text = font.render('Exit', True, offwhite)

        # restart button
        pygame.draw.rect(screen, orangeish, restart_rect)
        screen.blit(restart_button_text, (restart_rect.x + (restart_rect.width - restart_button_text.get_width()) // 2, restart_rect.y + 15))
        
        # exit button
        pygame.draw.rect(screen, orangeish, exit_rect)
        screen.blit(exit_button_text, (exit_rect.x + (exit_rect.width - exit_button_text.get_width()) // 2, exit_rect.y + 15))

    # good ending ------------------------------------
    elif screen_name == 'good':
        restart_rect = button_rects['Restart']
        exit_rect = button_rects['Exit_2']

        restart_button_text = font.render('Restart', True, offwhite)
        exit_button_text = font.render('Exit', True, offwhite)

        # restart button
        pygame.draw.rect(screen, orangeish, restart_rect)
        screen.blit(restart_button_text, (restart_rect.x + (restart_rect.width - restart_button_text.get_width()) // 2, restart_rect.y + 15))
        
        # exit button
        pygame.draw.rect(screen, orangeish, exit_rect)
        screen.blit(exit_button_text, (exit_rect.x + (exit_rect.width - exit_button_text.get_width()) // 2, exit_rect.y + 15))

    # letter ----------------------------------
    elif screen_name == 'letter':
        accept_rect = button_rects['Accept']
        decline_rect = button_rects['Decline']

        screen.blit(backgrounds['letter'], (0, 0))

        # accept/decline
        accept_button_text = font.render('Accept', True, offwhite)
        decline_button_text = font.render('Decline', True, offwhite)
        
        # accept button
        pygame.draw.rect(screen, orangeish, accept_rect)
        screen.blit(accept_button_text, (accept_rect.x + (accept_rect.width - accept_button_text.get_width()) // 2, accept_rect.y + 15))

        # decline button
        pygame.draw.rect(screen, orangeish, decline_rect)
        screen.blit(decline_button_text, (decline_rect.x + (decline_rect.width - decline_button_text.get_width()) // 2, decline_rect.y + 15))

    # choice screen AFTER LETTER  -------------------
    elif screen_name == 'quest_choices_paths':
        screen.blit(backgrounds['letter'], (0, 0))
        shop_rect = button_rects['Shop']
        path_rect = button_rects['Path']
        forest_rect = button_rects['Forest']
                
        shop_button_text = font.render('Shop', True, offwhite)
        path_button_text = font.render('Path', True, offwhite)
        forest_button_text = font.render('Forest', True, offwhite)

        # shop
        pygame.draw.rect(screen, orangeish, shop_rect)
        screen.blit(shop_button_text, (shop_rect.x + (shop_rect.width - shop_button_text.get_width()) // 2, shop_rect.y + 15))
        
        # path
        pygame.draw.rect(screen, orangeish, path_rect)
        screen.blit(path_button_text, (path_rect.x + (path_rect.width - path_button_text.get_width()) // 2, path_rect.y + 15))

        # forest
        pygame.draw.rect(screen, orangeish, forest_rect)
        screen.blit(forest_button_text, (forest_rect.x + (forest_rect.width - forest_button_text.get_width()) // 2, forest_rect.y + 15))

    # path -----------------------------------
    elif screen_name == 'path' or screen_name == 'starfuit_interaction':

        screen.blit(backgrounds['path'], (0, 0))

        talk_rect = button_rects['Talk']
        continue_rect = button_rects['Continue']

        # talk/continue
        talk_button_text = font.render('Talk', True, offwhite)
        continue_button_text = font.render('Continue', True, offwhite)
        
        # talk button
        pygame.draw.rect(screen, orangeish, talk_rect)
        screen.blit(talk_button_text, (talk_rect.x + (talk_rect.width - talk_button_text.get_width()) // 2, talk_rect.y + 15))

        # continue button
        pygame.draw.rect(screen, orangeish, continue_rect)
        screen.blit(continue_button_text, (continue_rect.x + (continue_rect.width - continue_button_text.get_width()) // 2, continue_rect.y + 15))

    # forest ------------------
    elif screen_name == 'forest' or screen_name == 'fight_someguy':

        screen.blit(backgrounds['forest'], (0, 0))

        fight_rect = button_rects['Fight']
        continue_rect = button_rects['Continue']

        # talk/continue
        fight_button_text = font.render('Fight', True, offwhite)
        continue_button_text = font.render('Continue', True, offwhite)
        
        # fight button
        pygame.draw.rect(screen, orangeish, fight_rect)
        screen.blit(fight_button_text, (fight_rect.x + (fight_rect.width - fight_button_text.get_width()) // 2, fight_rect.y + 15))

        # continue button
        pygame.draw.rect(screen, orangeish, continue_rect)
        screen.blit(continue_button_text, (continue_rect.x + (continue_rect.width - continue_button_text.get_width()) // 2, continue_rect.y + 15))

    # shop ----------------------------------------
    elif screen_name == 'shop' or screen_name == 'shop_menu':

        screen.blit(backgrounds['shop'], (0, 0))
        
        # player gold
        gold_text = font.render(f'Gold: {player_gold}', True, offwhite)

        padding = 10

        text_start_x = width // 2 - gold_text.get_width() // 2
        
        # rect for gold 
        gold_box_rect = pygame.Rect(
            text_start_x - padding, 
            50 - padding, # Y position is 50
            gold_text.get_width() + 2 * padding, 
            gold_text.get_height() + 2 * padding
        )

        # semi transparent 
        s_gold = pygame.Surface((gold_box_rect.width, gold_box_rect.height), pygame.SRCALPHA)
        s_gold.fill((218, 99, 65, 180)) 
        screen.blit(s_gold, (gold_box_rect.x, gold_box_rect.y))

        screen.blit(gold_text, (width // 2 - gold_text.get_width() // 2, 50))

        if screen_name == 'shop_menu':

            # textbox bg
            shop_box_rect = pygame.Rect(50, 250, width - 100, 420)
            s = pygame.Surface((shop_box_rect.width, shop_box_rect.height), pygame.SRCALPHA)
        
            s.fill((254, 238, 220, 225)) 
            screen.blit(s, (shop_box_rect.x, shop_box_rect.y))
            
            # list and buttons
            start_y = 280
            line_spacing = 100

            item_name_font = pygame.font.Font("PixelOperator8-Bold.ttf", 26)
            item_desc_font = pygame.font.Font("PixelOperator8-Bold.ttf", 18)
            buy_text = font.render('Buy', True, offwhite)
            
            # draw the items
            for i, item in enumerate(shop_inventory):
                y_pos = start_y + i * line_spacing
                item_name = item['item_name']
                price = item['price']
                description = item['description']
                rect = button_rects[item['rect_key']]

                rect.y = y_pos - 10
                
                # name and price
                name_price_text = item_name_font.render(f"{item_name} - {price} Gold", True, orangeish)
                screen.blit(name_price_text, (80, y_pos))
                
                # description -- accounts for \n
                desc_lines = description.split('\n')
            
                for line_index, line in enumerate(desc_lines):
                    desc_text = item_desc_font.render(line, True, reddish)
                
                # actually draws the line now
                    screen.blit(desc_text, (80, y_pos + 30 + (line_index * 20)))
                
                # buy button
                if item_name not in player_inventory:
                    pygame.draw.rect(screen, orangeish, rect)
                    buy_text_x = rect.x + (rect.width - buy_text.get_width()) // 2
                    buy_text_y = rect.y + (rect.height - buy_text.get_height()) // 2 
                    screen.blit(buy_text, (buy_text_x, buy_text_y))
                else:
                    # item already bought - SOLD
                    sold_text = font.render('SOLD', True, reddish)
                    sold_text_x = rect.x + (rect.width - sold_text.get_width()) // 2 - 8
                    sold_text_y = rect.y + (rect.height - sold_text.get_height()) // 2
                    screen.blit(sold_text, (sold_text_x, sold_text_y))

            # exit button 
            exit_rect = button_rects['Shop_Exit']
            exit_button_text = font.render('Exit', True, offwhite)
            pygame.draw.rect(screen, orangeish, exit_rect)
            screen.blit(exit_button_text, (exit_rect.x + (exit_rect.width - exit_button_text.get_width()) // 2, exit_rect.y + 15))

    # castle ---------------------------------
    elif screen_name == 'castle' or screen_name == 'dragon':

        screen.blit(backgrounds['castle'], (0, 0))
        
        return_rect = button_rects['Return']
        continue_rect = button_rects['Continue']

        # return/continue
        return_button_text = font.render('Return', True, offwhite)
        continue_button_text = font.render('Continue', True, offwhite)

        # return button
        pygame.draw.rect(screen, orangeish, return_rect)
        screen.blit(return_button_text, (return_rect.x + (return_rect.width - return_button_text.get_width()) // 2, return_rect.y + 15))

        # continue button
        pygame.draw.rect(screen, orangeish, continue_rect)
        screen.blit(continue_button_text, (continue_rect.x + (continue_rect.width - continue_button_text.get_width()) // 2, continue_rect.y + 15)) 

    # apricot decision room
    elif screen_name == 'room':
        screen.blit(backgrounds['room'], (0, 0))

        screen.blit(apricot_sprites['apricot_mad'], (0, 0))
        return_rect = button_rects['Return']
        shop_rect = button_rects['Shop_2']

        # return/continue
        return_button_text = font.render('Return', True, offwhite)
        shop_button_text = font.render('Shop', True, offwhite)

        # return button
        pygame.draw.rect(screen, orangeish, return_rect)
        screen.blit(return_button_text, (return_rect.x + (return_rect.width - return_button_text.get_width()) // 2, return_rect.y + 15))

        # shop button
        pygame.draw.rect(screen, orangeish, shop_rect)
        screen.blit(shop_button_text, (shop_rect.x + (shop_rect.width - shop_button_text.get_width()) // 2, shop_rect.y + 15)) 

#----------stats/dialogue prep--------

player_gold = 100
player_inventory = []
has_appricots = False
some_guy_alive = True

dialogue_in_progress = False
current_dialogue_key = None
current_line_index = 0

shop_inventory = [
    {"item_name": "Rough Sword", "price": 25, "description": "A weaker sword, will do you good!", "rect_key": 'Buy_Rough'},
    {"item_name": "Sleek Sword", "price": 50, "description": "The sword every knight dreams of!", "rect_key": 'Buy_Sleek'},
    {"item_name": "Apricots", "price": 5, "description": "Somebody will appreciate these\na lot more than most people!", "rect_key": 'Buy_Apricots'},
    {"item_name": "Flowers", "price": 10, "description": "Everybody loves flowers!", "rect_key": 'Buy_Flowers'}
]

#----------------- MAIN LOOP -----------------

def main():
    global current_screen, last_screen, current_bg, player_gold, player_inventory, has_appricots, some_guy_alive
    global dialogue_in_progress, current_dialogue_key, current_line_index

    running = True
    while running:

        screen.fill((0, 0, 0))

        if dialogue_in_progress and current_dialogue_key:
            draw_dialogue(current_dialogue_key, current_line_index, current_screen)
        else:
            draw_screen(current_screen)

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # escape key
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button

                    # handles dialogue sequences
                    if dialogue_in_progress:

                        current_line_index += 1
                        total_lines = len(dialogue_sequences[current_dialogue_key])

                        if current_line_index >= total_lines:

                            completed_dialogue = current_dialogue_key    

                            # end dialogue, reset state
                            dialogue_in_progress = False
                            current_dialogue_key = None
                            current_line_index = 0

                            # this ensures the next scene happens
                            if completed_dialogue == 'shop_intro':
                                current_screen = 'shop_menu'
                            
                            elif completed_dialogue == 'path_intro':
                                pass

                            elif completed_dialogue == 'forest_intro':
                                pass

                            elif completed_dialogue == 'starfruit_interaction':
                                current_screen = 'shop'
                                dialogue_in_progress = True
                                current_dialogue_key = 'shop_intro'
                                current_line_index = 0

                            elif completed_dialogue == 'someguy_interaction_no_weapon':
                                current_screen = 'bad'

                            elif completed_dialogue == 'someguy_interaction_with_weapon':
                                current_screen = 'shop'
                                dialogue_in_progress = True
                                current_dialogue_key = 'shop_intro'
                                current_line_index = 0

                            elif completed_dialogue == 'continue_text':
                                current_screen = 'shop'
                                dialogue_in_progress = True
                                current_dialogue_key = 'shop_intro'
                                current_line_index = 0

                            elif completed_dialogue == 'castle_prompt':
                                current_screen = 'castle'

                            elif completed_dialogue == 'dragon_intro':
                                dialogue_in_progress = True
                                if "Sleek Sword" in player_inventory:
                                    current_dialogue_key = 'dragon_strong_weapon' 
                                else:
                                    current_dialogue_key = 'dragon_weak_or_no_weapon'
                                current_line_index = 0

                            elif completed_dialogue == 'dragon_weak_or_no_weapon':
                                current_screen = 'bad'

                            elif completed_dialogue == 'some_guy_dead':
                                current_screen = 'bad'
                            
                            elif completed_dialogue == 'some_guy_alive':
                                current_screen = 'neutral'

                            elif completed_dialogue == 'dragon_strong_weapon':
                                current_screen = 'room'
                                dialogue_in_progress = True
                                current_dialogue_key = 'apricot_intro'
                                current_line_index = 0

                            elif completed_dialogue == 'apricot_intro':
                                current_screen = 'room'
                                dialogue_in_progress = True
                                if "Apricots" in player_inventory:
                                    dialogue_in_progress = True
                                    current_dialogue_key = 'apricot_hasapricot'
                                    current_line_index = 0
                                
                                elif "Apricots" not in player_inventory and some_guy_alive == False:
                                    dialogue_in_progress = True
                                    current_dialogue_key = 'apricot_someguy_dead'
                                    current_line_index = 0

                                elif "Apricots" not in player_inventory:
                                    dialogue_in_progress = True
                                    current_dialogue_key = 'apricot_noapricot'
                                    current_line_index = 0

                            elif completed_dialogue == 'apricot_hasapricot':
                                current_screen = 'good'
                            
                            elif completed_dialogue == 'apricot_someguy_dead':
                                current_screen = 'bad'
                            
                            elif completed_dialogue == 'apricot_noapricot':
                                current_screen = 'room'

                            else:
                                dialogue_in_progress = False
                                current_dialogue_key = None
                                current_line_index = 0


                        continue
                    

                    if current_screen == 'start':
                        if button_rects['Start'].collidepoint(event.pos): # starts the game
                            current_screen = 'letter'

                            player_gold = 100 # for a reset of the game
                            player_inventory = []
                            has_appricots = False

                            dialogue_in_progress = True
                            current_dialogue_key = 'letter_prompt'
                            current_line_index = 0

                        elif button_rects['Exit'].collidepoint(event.pos): # exit button
                            running = False

                    # endings ------------------------------------

                    # neutral
                    elif current_screen == 'neutral':
                        if button_rects['Restart'].collidepoint(event.pos): # start game
                            current_screen = 'start'
                        elif button_rects['Exit_2'].collidepoint(event.pos): # exit button
                            running = False

                    # bad
                    elif current_screen == 'bad':
                        if button_rects['Restart'].collidepoint(event.pos): # start game
                            current_screen = 'start'
                        elif button_rects['Exit_2'].collidepoint(event.pos): # exit button
                            running = False

                    # good
                    elif current_screen == 'good':
                        if button_rects['Restart'].collidepoint(event.pos): # start game
                            current_screen = 'start'
                        elif button_rects['Exit_2'].collidepoint(event.pos): # exit button
                            running = False

                    # game play now ---------------------------------------

                    # letter page 
                    elif current_screen == 'letter':
                        if not dialogue_in_progress:
                            if button_rects["Accept"].collidepoint(event.pos):
                                current_screen = 'quest_choices_paths'

                                dialogue_in_progress = True
                                current_dialogue_key = 'accept_quest'
                                current_line_index = 0

                            if button_rects['Decline'].collidepoint(event.pos):
                                current_screen = 'neutral'

                    # quest choices AFTER letter 
                    elif current_screen == 'quest_choices_paths':
                        last_screen = current_screen

                        if button_rects['Shop'].collidepoint(event.pos):
                            current_screen = 'shop' 
                            dialogue_in_progress = True
                            current_dialogue_key = 'shop_intro'
                            current_line_index = 0

                        elif button_rects['Path'].collidepoint(event.pos):
                            current_screen = 'path' 
                            dialogue_in_progress = True
                            current_dialogue_key = 'path_intro'
                            current_line_index = 0

                        elif button_rects['Forest'].collidepoint(event.pos):
                            current_screen = 'forest'     
                            dialogue_in_progress = True
                            current_dialogue_key = 'forest_intro'
                            current_line_index = 0 

                    # ---------- SHOP ------------
                    elif current_screen == 'shop_menu':
                        for item in shop_inventory:
                            item_name = item['item_name']
                            item_price = item['price']
                            item_rect = button_rects[item['rect_key']]

                            if item_name not in player_inventory and item_rect.collidepoint(event.pos):
                                if player_gold >= item_price:
                                    player_gold -= item_price
                                    player_inventory.append(item_name)
                                    
                                    # apricot flag yay
                                    if item_name == 'Apricots':
                                        has_appricots = True
                                    
                        
                        # exit
                        if button_rects['Shop_Exit'].collidepoint(event.pos):            

                            # choices screen
                            if last_screen == 'quest_choices_paths':
                                current_screen = 'quest_choices_paths'

                            # castle
                            elif last_screen == 'path' or last_screen == 'forest':
                                current_screen = 'castle'
                                dialogue_in_progress = True
                                current_dialogue_key = 'castle_prompt'
                                current_line_index = 0
                            
                            # apricot
                            elif last_screen == 'room':
                                current_screen = 'room'
                                dialogue_in_progress = True
                                if "Apritocts" in player_inventory:
                                    current_dialogue_key = 'apricot_hasapricot'
                                    current_line_index = 0
                                else:
                                    current_dialogue_key = 'apricot_noapricot'
                                    current_line_index = 0

                    # ----- PATH -------
                    elif current_screen == 'path':
                        last_screen = current_screen
                        some_guy_alive = True
                        if button_rects['Talk'].collidepoint(event.pos):
                            current_screen = 'path'
                            dialogue_in_progress = True
                            current_dialogue_key = 'starfruit_interaction'
                            current_line_index = 0
                            player_inventory.append('Apricots')
                            has_appricots = True
                                
                            
                        elif button_rects['Continue'].collidepoint(event.pos):
                            dialogue_in_progress = True
                            current_dialogue_key = 'continue_text'
                            current_line_index = 0
                    
                    # ----- FOREST -------
                    elif current_screen == 'forest':
                        last_screen = current_screen
                        if button_rects['Fight'].collidepoint(event.pos):
                            
                            dialogue_in_progress = True
                            current_screen = 'forest'

                            if "Rough Sword" in player_inventory or "Sleek Sword" in player_inventory:
                                current_dialogue_key = 'someguy_interaction_with_weapon'
                                player_gold += 100
                                some_guy_alive = False
                            
                            elif "Rough Sword" not in player_inventory or "Sleek Sword" not in player_inventory:
                                current_dialogue_key = 'someguy_interaction_no_weapon'

                        elif button_rects['Continue'].collidepoint(event.pos):
                            dialogue_in_progress = True
                            current_dialogue_key = 'continue_text'
                            current_line_index = 0

                    # ----- CASTLE -------
                    elif current_screen == 'castle':
                        last_screen = current_screen
                            
                        if button_rects['Continue'].collidepoint(event.pos):

                            dialogue_in_progress = True
                            current_dialogue_key = 'dragon_intro'
                            current_line_index = 0

                        elif button_rects['Return'].collidepoint(event.pos):
                            dialogue_in_progress = True

                            if some_guy_alive == False:
                                current_dialogue_key = 'some_guy_dead'
                                current_screen = 'path'
                            
                            elif some_guy_alive == True:
                                current_dialogue_key = 'some_guy_alive'
                                current_screen = 'path'

                    # ------- ROOM --------
                    elif current_screen == 'room':
                        last_screen = current_screen

                        if button_rects['Return'].collidepoint(event.pos):
                            dialogue_in_progress = True

                            if some_guy_alive == True:
                                current_dialogue_key = 'some_guy_alive'
                                current_screen = 'path'

                        elif button_rects['Shop_2'].collidepoint(event.pos):
                            current_screen = 'shop' 
                            dialogue_in_progress = True
                            current_dialogue_key = 'shop_intro'
                            current_line_index = 0

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()