import pygame
import sys, json, pickle, os, time
from os import path
from data.scripts.settings import *
from data.scripts.sprites import *
from data.scripts.tilemap import *
from data.scripts.pathfinder import *
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

pygame.joystick.init()


fullscreen = 0


if fullscreen == 1: flags = FULLSCREEN | DOUBLEBUF | HWSURFACE
else: flags = DOUBLEBUF | HWSURFACE

screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, 16)





hud_on = True
mouse_hide = False

pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])


#season change
current_season = 8

prems = 3434340


have_skins = [0]
have_gliders = [0]
have_trails = [0]
have_musics = [0]
have_backpacks = [0]
have_emoticons = [0]
have_sprays = [0]
have_ls = [0]

skin_num = 0

logged_in_any = False
username = "Player"
password = "43refijo"

friend_list = []

item_shops = []

#season change
battle_passes = [False, False, False, False, False, False, False]
season_tiers = [1, 1, 1, 1, 1, 1, 1]

season_xp = 0

def real_dump(data, filename, b=1):
    with open(filename, 'w') as f:
        datax = {}
        datax[0] = data
        json.dump(datax, f)

    if b==1:
        j = filename.split('/')
        j[1] = "unpack"
        lg = "/".join(j)
        j = lg.split('.')
        j[-1] = "txt"
        lg = ".".join(j)
        dbfile = open(lg, 'wb')
        pickle.dump(data, dbfile)                    
        dbfile.close()



   

    

def real_load(filename):
    try:
        f = open(filename)
        datax = json.load(f)
        return datax["0"]
    except:
            j = filename.split('/')
            j[1] = "unpack"
            lg = "/".join(j)
            j = lg.split('.')
            j[-1] = "txt"
            lg = ".".join(j)

            dbfile = open(lg, 'rb')    
            db = pickle.load(dbfile)
            dbfile.close()


            real_dump(db, filename)
            return db


# list_of_users = []
# real_dump(list_of_users, orn(f"data/users/@list_of_users.json"))
list_of_users = real_load(f"data/users/@list_of_users.json")

max_rp = 0


# for name in list_of_users:
#         real_dump(True, (f"data/users/{name}/{name}_pins.json"))
#         real_dump(have_trails, (f"data/users/{name}/{name}_trails.json"))


# real_dump(0, (f"data/users/nytro._rp.json"))

# real_dump(1912, (f"data/users/Mega_prems.json"))

# real_dump(99999999, (f"data/users/t1_prems.json"))

def create_account(name, pw):
    list_of_users.append(name)
    try:
        os.mkdir(f"data/users/{name}")
        os.mkdir(f"data/unpack/{name}")
    except: pass
    real_dump(list_of_users, (f"data/users/{name}/@list_of_users.json"))
    real_dump(name, (f"data/users/{name}/{name}_name.json"))
    real_dump(pw, (f"data/users/{name}/{name}_pw.json"))
    global username, password
    username = name
    password = pw

def auto_save(name):
    if logged_in_any:
        real_dump(friend_list, (f"data/users/{name}/{name}_friends.json"))
        real_dump(prems, (f"data/users/{name}/{name}_prems.json"))

        real_dump(have_skins, (f"data/users/{name}/{name}_skins.json"))

        real_dump(season_tiers, (f"data/users/{name}/{name}_tiers.json"))
        real_dump(battle_passes, (f"data/users/{name}/{name}_bp.json"))
        real_dump(season_xp, (f"data/users/{name}/{name}_xp.json"))

        real_dump(pin_screen, (f"data/users/{name}/{name}_pins.json"))

        real_dump(have_backpacks, (f"data/users/{name}/{name}_backpacks.json"))
        real_dump(have_ls, (f"data/users/{name}/{name}_ls.json"))
        real_dump(have_gliders, (f"data/users/{name}/{name}_gliders.json"))
        real_dump(have_musics, (f"data/users/{name}/{name}_musics.json"))
        real_dump(have_trails, (f"data/users/{name}/{name}_trails.json"))
        real_dump(have_emoticons, (f"data/users/{name}/{name}_emoticons.json"))
        real_dump(have_sprays, (f"data/users/{name}/{name}_sprays.json"))

        real_dump(rlr, (f"data/users/{name}/{name}_rlr.json"))

        real_dump(discovered, (f"data/users/{name}/{name}_discovered.json"))

        real_dump(w_move, (f"data/users/{name}/{name}_s$move.json"))

        real_dump(rp, (f"data/users/{name}/{name}_rp.json"))
        real_dump(mrp, (f"data/users/{name}/{name}_mrp.json"))

        real_dump(max_rp, (f"data/users/{name}/{name}_max_rp.json"))

        lst = [skin_num, backpack_num, glider_num, emoticon_num, spray_num, ls_num, trail_num, music_num]
        real_dump(lst, (f"data/users/{name}/{name}_locker.json"))


# for i in list_of_users:
# if 1:
#     i = "t1"
#     if not os.path.exists(f"data/unpack/{i}"): os.mkdir(f"data/unpack/{i}") 
#     for j in os.listdir(f"data/users/{i}"):
#         # try:
#             p = f"data/users/{i}/{j}"
#             j = real_load(p)
#             yj = p.replace(".json", ".txt")
#             yj = yj.replace("users", "unpack")
#             t = yj
#             f = open(t, 'x')
#             f.close()
#             vd = open(t, 'wb')
#             pickle.dump(j, vd)      
#             vd.close()
            # db = pickle.load(open(p, 'rb'))
            # real_dump(db, p, b=0)
        # except:pass

def login(name):
    global season_xp, friend_list, username, password, prems, have_skins, rlr, discovered, have_backpacks, pin_screen, have_gliders, rp, mrp, max_rp, have_emoticons, have_sprays, have_ls, season_tiers, battle_passes, season_xp, have_trails, have_musics
    friend_list = real_load((f"data/users/{name}/{name}_friends.json"))
    username = real_load((f"data/users/{name}/{name}_name.json"))
    password = real_load((f"data/users/{name}/{name}_pw.json"))

    prems = real_load((f"data/users/{name}/{name}_prems.json"))
    have_skins = real_load((f"data/users/{name}/{name}_skins.json"))

    pin_screen = real_load((f"data/users/{name}/{name}_pins.json"))
    global pin_b
    if pin_screen: pin_b = Tick(50, 410, 'Emoji / Spray Screen: On', font30)
    else: pin_b = Tick(50, 410, 'Emoji / Spray Screen: Off', font30)

    season_tiers = real_load((f"data/users/{name}/{name}_tiers.json"))
    battle_passes = real_load((f"data/users/{name}/{name}_bp.json"))
    season_xp = real_load((f"data/users/{name}/{name}_xp.json"))

    have_backpacks = real_load((f"data/users/{name}/{name}_backpacks.json"))
    have_ls = real_load((f"data/users/{name}/{name}_ls.json"))
    have_emoticons = real_load((f"data/users/{name}/{name}_emoticons.json"))
    have_sprays = real_load((f"data/users/{name}/{name}_sprays.json"))
    have_gliders = real_load((f"data/users/{name}/{name}_gliders.json"))
    have_musics = real_load((f"data/users/{name}/{name}_musics.json"))
    have_trails = real_load((f"data/users/{name}/{name}_trails.json"))

    
    discovered = real_load((f"data/users/{name}/{name}_discovered.json"))

    mrp = real_load((f"data/users/{name}/{name}_mrp.json"))
    rp = real_load((f"data/users/{name}/{name}_rp.json"))
    max_rp = real_load((f"data/users/{name}/{name}_max_rp.json"))
    
    global menu_state, nsx
    while len(season_tiers) < current_season-1:
        season_tiers.append(1)
        battle_passes.append(False)
        season_xp = 0
        rp = 0
        menu_state = "new season"
        nsx = -800
    
    global estce
    estce = False



    

    global w_move
    w_move = real_load((f"data/users/{name}/{name}_s$move.json"))

    lst = real_load((f"data/users/{name}/{name}_locker.json"))
    global skin_num, backpack_num, glider_num, emoticon_num, spray_num, ls_num, trail_num, music_num
    skin_num = lst[0]; backpack_num = lst[1]; glider_num = lst[2]; emoticon_num = lst[3]; spray_num = lst[4]; ls_num = lst[5]; trail_num = lst[6]; music_num = lst[7]

    rlr = real_load((f"data/users/{name}/{name}_rlr.json"))

    global prev_ls; prevls = 0
    global rl_b
    if rlr:
            ls_num = random.choice(have_ls)
            rl_b = Tick(WIDTH - 475, 150, 'Set Custom', font30)
    else:
            rl_b = Tick(WIDTH - 475, 150, 'Set Random', font30)

    global old_level; old_level = season_tiers[current_season-2]

    global old_rank; old_rank = get_rank(rp)

    global dskin; dskin = Scale(Image(f'customize/skins/{skin_num}.svg'), 2)
    global dbling; dbling = Scale(Image(f'customize/backpacks/{backpack_num}.svg'), 2)

    pygame.mixer.music.stop()

    # reroll_is()

estce = False

discovered = []
for i in range(9):
    discovered.append("u")

got_bp_rewards = False

KILLER_CACHE = {}
def draw_text(text, font, e, x, y, center=False, color=(255,255,255), r=0):

    if r==0:
        if (text, font, color) in KILLER_CACHE:
            img = KILLER_CACHE[(text, font, color)]
        else:
            img = font.render(text, True, color).convert_alpha()

                
            KILLER_CACHE[(text, font, color)] = img.copy()
        if e == g: s = e.screen
        else: s = screen
        if center:
            text_rect = img.get_rect(center=(640/2, 480/2))
            s.blit(img, (text_rect[0], text_rect[1] + y))
        else:
            s.blit(img, (x, y))
    else:
        if e == g: s = e.screen
        else: s = screen
        s.blit((render(text, font, color, BLACK)), (x,y))
        
    
def get_text(text, font):
    img = font.render(text, True, (0,0,0))
    return img

def grant_item(lvl):
    lm = lvl_grants[lvl]
    global have_backpacks, have_emoticons, have_emoticons, have_ls, have_skins, have_sprays, prems
    global got_new_level

    if lm[1] == "skin":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_skins: have_skins.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_skins: have_skins.append(lm[0]); got_new_level = True

    if lm[1] == "glider":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_gliders: have_gliders.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_gliders: 
                have_gliders.append(lm[0]); got_new_level = True

    if lm[1] == "music":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_musics: have_musics.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_musics: 
                have_musics.append(lm[0]); got_new_level = True

    if lm[1] == "trail":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_trails: have_trails.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_trails: 
                have_trails.append(lm[0]); got_new_level = True

    if lm[1] == "backpack":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_backpacks: 
                    have_backpacks.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_backpacks: 
                have_backpacks.append(lm[0]); got_new_level = True

    if lm[1] == "emoticon":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_emoticons: 
                    have_emoticons.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_emoticons: 
                have_emoticons.append(lm[0]); got_new_level = True

    if lm[1] == "spray":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_sprays: 
                    have_sprays.append(lm[0]); got_new_level = True
        else:
            if lm[0] not in have_sprays: 
                have_sprays.append(lm[0]); got_new_level = True

    if lm[1] == "ls":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                if lm[0] not in have_ls: have_ls.append(lm[0]); got_new_level = True
        else:
           if lm[0] not in have_ls:  have_ls.append(lm[0]); got_new_level = True

    if lm[1] == "prems":
        if lm[2] == True:
            k = battle_passes[current_season-2]
            if k:
                prems += 40
        else:
           prems += 40

def challenges_grant(c):
    global season_xp
    #for challenge in challenges
    ind = 0
    for i in c:
        if cc_tracker[i] >= cc_goal[i]:
                cc_tracker[i] = 0
                season_xp += 4000
                cc_complete[ind] = True
        ind += 1
     


cc_tracker = []
challenges = [0,0,0,0]
cc_goal = [4000, 1000, 250, 250, 100, 150, 200, 2, 2]
cc_complete = []
challenge_acts = [
    "Deal Damage",
    "Deal Damage in a single match",
    "Heal for 250 Health",
    "Heal for 250 Gulp Shield",
    "Heal for 100 health in a single match",
    "Heal for 150 Gulp Shield in a single match",
    "Collect Ammo",
    "Eliminate Opponents",
    "Eliminate Opponents in a single match",
]

for i in range(season_tiers[current_season-2]):
    try: grant_item(i+1)
    except: pass

def reroll_challenges():
    global challenges; challenges = []
    global cc_complete; cc_complete = []
    gg = []
    for i in range(4):
        f = random.randint(0, len(challenge_acts)-1)
        while f in gg:
            f = random.randint(0, len(challenge_acts)-1)
        gg.append(f)
        challenges.append(f)
        cc_complete.append(False)
    
    global cc_tracker
    cc_tracker = []
    for i in range(len(challenge_acts)):
        cc_tracker.append(0)

reroll_challenges()

def check_xp():
    challenges_grant(challenges)
    global season_xp, season_tiers
    if season_xp >= 10000:
        season_xp -= 10000
        season_tiers[current_season-2] += 1
        Audio('other/lvl.wav')
        if season_tiers[current_season-2] <= len(lvl_grants): 
            grant_item(season_tiers[current_season-2])
        else:
            global prems
            prems += 25
bptx=0


class Button():
    def __init__(self, x, y, image, scale, glide=0, glide2=0):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.width, self.height = self.image.get_width(), self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.o = image
        self.glide = glide
        self.glide2 = glide2
        self.ogx = self.rect.x
        self.ogy = self.rect.y

    def draw(self):
        if self.glide2 == 69420:
            self.rect.y = self.ogy + customy
        if self.glide2 == 332:
            self.rect.y = self.ogy + boux

        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if self.clicked and pygame.mouse.get_pressed()[0] == 0:
            action = True
            self.clicked = False

#draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

class BP():
    def __init__(self, x, y, image, scale, glide=0, glide2=0, glide3=0):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.width, self.height = self.image.get_width(), self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.o = image
        self.glide = glide
        self.glide2 = glide2
        self.glide3 = glide3

        self.ogx = self.rect.x
        self.ogy = self.rect.y
        self.na = False

    def draw(self):
        if self.glide2 == 234:
            self.rect.x = self.ogx + bptx
        if self.glide2 == 332:
            self.rect.y = self.ogy + boux
        
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if self.clicked and pygame.mouse.get_pressed()[0] == 0:
            action = True
            self.clicked = False

#draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Tick():
    def __init__(self, x, y, text, font, glide=0, glide2=0):
        self.rect = pygame.Rect(x, y, get_text(text, font).get_width() + 15, get_text(text, font).get_height() + 10)
        self.rect.topleft = (x, y)
        self.clicked = False
        self.glide = glide
        self.txt, self.fnt = text, font
        self.hovering = False
        self.glide2 = glide2
        self.ogy = self.rect.y



    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.glide2 == 2424:
            self.rect.y = self.ogy + friendy
        
        col = (0, 71, 171)
        if self.rect.collidepoint(pos):
            if not self.hovering: Audio(f'interact/hover{random.randint(1, 3)}.wav')
            self.hovering = True
            col = (111, 143, 175)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        else: self.hovering = False

        if self.clicked and pygame.mouse.get_pressed()[0] == 0:
            Audio(f'interact/select1.wav')
            action = True
            self.clicked = False

        pygame.draw.rect(screen, col, self.rect)
        pygame.draw.rect(screen, (100, 149, 237), self.rect, 4)

        draw_text(self.txt, self.fnt, 0, self.rect.x + 5, self.rect.y + 5, color=(0,0,0))

        return action


not_in_shop_list = [
    #season change
    [5,6,7,8,9,10,11,12,13,14,15,16, 24,25,26,27,28,29,30,31,32,33,34,35, 40,41,42,43,44,45,46,47,48,49,50,51, 57,58,59,60,61,62,63,64,65,66,67,68, 
     73,74,75,76,77,78,79,80,81,82,83,84, 93,94,95,96,97,98,99,100,101,102,103,104, 105,106,107,108,109,110,111,112,113,114,115,116, 124,129], #skins
    [5,6,7,8,9,10, 13,14,15,16,17,18, 20,21,22,23,24,25, 27,28,29,30,31,32, 34,35,36,37,38,39, 42,43,44,45,46,47, 48,49,50,51,52,53,55], #gliders
    [3,4,5,6,7,8, 15,16,17,18,19,20, 22,23,24,25,26,27, 29,30,31,32,33,34, 36,37,38,39,40,41, 44,45,46,47,48,49, 50,51,52,53,54,55, 57,58,59,60,61,62], #backpacks
    [7,8,9,10,11,12,13,14, 17,18,19,20,21,22,23,24, 26,27,28,29,30,31,32,33, 35,36,37,38,39,40,41,42, 44,45,46,47,48,49,50,51, 54,55,56,57,58,59,60,61, 62,63,64,65,66,67,68,69, 70], #emojis
    [7,8,9,10,11,12,13, 16,17,18,19,20,21,22, 24,25,26,27,28,29,30, 32,33,34,35,36,37,38, 40,41,42,43,44,45,46, 49,50,51,52,53,54,55, 56,57,58,59,60,61,62, 63], #sprays
]

def get_skin_info(type, num):
    #format:    return NAME, RARITY (rarity: 0=common, 1=uncommon, 2=rare, 3=epic, 4=legendary)

    if type == "skin":
        if num == 0:
            return "Mark", 0
        if num == 1:
            return "Undead", 3
        if num == 2:
            return "Amina", 1
        if num == 3:
            return "Maddie", 2
        if num == 4:
            return "Jonas", 2
        
        if num == 17:
            return "Adeline", 2
        if num == 18:
            return "Red V Blue", 3
        if num == 19:
            return "Green V Purple", 3
        if num == 20:
            return "Oran. V Aqua", 3
        if num == 21:
            return "Gulpo", 4
        if num == 22:
            return "Veronica", 3
        if num == 23:
            return "Destroylonely", 3
        
        if num == 36:
            return "Shadow Guard", 3
        if num == 37:
            return "DJ Crystal", 3
        if num == 38:
            return "Plasma", 4
        if num == 39:
            return "Goopy Guy", 2
        
        if num == 52:
            return "Red Leader", 2 
        if num == 53:
            return "Green Leader", 2
        if num == 54:
            return "Blue Leader", 2
        if num == 55:
            return "Yellow Leader", 2
        if num == 56:
            return "Holosam", 3
        
        if num == 69:
            return "Frostbiter", 3
        if num == 70:
            return "TV Enforcer", 4
        if num == 71:
            return "Lyla", 3
        if num == 72:
            return "Valeria", 3
        
        if num == 85:
            return "Goldman", 2
        if num == 86:
            return "Chani", 3
        if num == 87:
            return "Astrid", 1
        if num == 88:
            return "Grandfather", 2
        
        if num == 89:
            return "Houseman", 2
        if num == 90:
            return "The Baron", 4
        if num == 91:
            return "GTV-020 X", 4
        if num == 92:
            return "Apple Muncher", 4
        
        if num == 117:
            return "Deadpool", 4
        if num == 118:
            return "Dr. Strange", 3
        if num == 119:
            return "Glaz", 4
        if num == 120:
            return "Luno", 3
        if num == 121:
            return "Wyldryder", 1
        if num == 122:
            return "Wolverine", 4
        if num == 123:
            return "Lyte", 3
        if num == 124:
            return "Lyte (Maxima)", 3
        if num == 125:
            return "Zombs Default", 1
        
        if num == 126:
            return "Jock Mark", 2
        if num == 127:
            return "Miles Morales", 3
        if num == 128:
            return "Quack", 2
        if num == 129:
            return "Quack (Blanc)", 2
        if num == 130:
            return "Bomby", 3
     
        
    elif type == "glider":
        if num == 0:
            return "Default", 0
        if num == 1:
            return "Red Default", 1
        if num == 2:
            return "Blue Default", 1
        if num == 3:
            return "Yellow Default", 1
        if num == 4:
            return "Skull Lander", 3
        
        if num == 11:
            return "Gulp Glider", 3
        if num == 12:
            return "Destroydecker", 3
        
        if num == 19:
            return "Dark Gradient", 3
        
        if num == 26:
            return "Holo-Hopper", 3
        
        if num == 33:
            return "Play Popper", 2
        
        if num == 40:
            return "Liquid Loft", 2
        
        if num == 41:
            return "Baron Board", 2
        
        if num == 54:
            return "Dead Dropper", 3
        
        if num == 55:
            return "RHO Rider", 2
        
        
    elif type == "backpack":
        if num == 0:
            return "None", 0
        if num == 1:
            return "Skull Wings", 3
        if num == 2:
            return "Hiker's Bag", 1
        
        if num == 9:
            return "Trippy Red", 2
        if num == 10:
            return "R.VS.B. Bag", 3
        if num == 11:
            return "G.VS.P. Bag", 3
        if num == 12:
            return "O.VS.A. Bag", 3
        if num == 13:
            return "Empty Gulp", 4
        if num == 14:
            return "Thief's Stuff", 3
        
        if num == 21:
            return "Plasma Helm", 4
        
        if num == 28:
            return "Holo-Bag", 3
        
        if num == 35:
            return "Lil' TV", 3
        
        if num == 42:
            return "Liquid Bag", 2
        
        if num == 43:
            return "Suspensors", 4
        
        if num == 56:
            return "Deadpool's Katanas", 4
        if num == 57:
            return "Katana-Klaws", 4
        if num == 58:
            return "Lytepack", 2
        
        if num == 59:
            return "RHO Ball", 2
        if num == 60:
            return "Spider Signal", 3
        if num == 61:
            return "Quack Feathers", 2
        if num == 62:
            return "Lil' Bomb", 3
        
        
    elif type == "emoticon":
        if num == 0:
            return "Happy", 0
        if num == 1:
            return "Sad", 1
        if num == 2:
            return "Elated", 1
        if num == 3:
            return "Dead", 2
        if num == 4:
            return "Angry", 1
        if num == 5:
            return "Winner", 3
        if num == 6:
            return "Loser", 3
        
        if num == 15:
            return "Need Shields", 3
        if num == 16:
            return "Cartoony GGs", 4
        
        if num == 25:
            return "Skull", 4
        
        if num == 34:
            return "Star-Struck", 2
        
        if num == 43:
            return "Angelic", 3
        
        if num == 52:
            return "Ghost Sad", 2
        if num == 53:
            return "Ghost Mad", 2
        
        if num == 70:
            return "Zombs Royale!", 3
        
    elif type == "spray":
        if num == 0:
            return "None", 0
        if num == 1:
            return "Slippy", 1
        if num == 2:
            return "Targeted", 2
        if num == 3:
            return "Heal Up", 3
        if num == 4:
            return "Fake Wall", 4
        if num == 5:
            return "This Way!", 3
        if num == 6:
            return "That Way!", 3
        
        if num == 14:
            return "Lil' Gulpy", 3
        if num == 15:
            return "Apple GGs", 2
        
        if num == 23:
            return "Go Bananas", 2
        
        if num == 31:
            return "Green Flag", 2
        
        if num == 39:
            return "Ring-a-ling!", 2
        
        if num == 47:
            return "100 Percent", 4
        
        if num == 48:
            return "Frog GGs", 3
        if num == 63:
            return "Spidey Spray", 3


def get_rar1(o):
    return coke("skin", o)
def get_rar2(o):
    return coke("glider", o)
def get_rar3(o):
    return coke("backpack", o)
def get_rar4(o):
    return coke("emoticon", o)
def get_rar5(o):
    return coke("spray", o)

def coke(i, o):
    f = get_skin_info(i, o)
    if f == None:
        return 4
    if f[1] == 4:
        return 5
    return f[1]


def reroll_is():
    gg=[]
    num = 0
    global item_shops; item_shops=[]
    for i in range(2):
        if len(have_skins) >= (len(os.listdir('data/images/customize/skins'))-1):
            num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
            while (num in not_in_shop_list[0]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
        else:
            o=0
            num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
            while (num in not_in_shop_list[0]) or (num in gg) or (num in have_skins):
                o+=1
                if o >= 200:
                    break
                num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
            while (num in not_in_shop_list[0]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
        # num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
        # while (num in not_in_shop_list[0]) or (num in gg):
        #     num = random.randint(1, len(os.listdir('data/images/customize/skins'))-2)
        gg.append(num)
        item_shops.append(ItemShop(50 + i*200, 200, "skin", num))
    
    gg = []
    num = 0
    for i in range(2):
        if len(have_gliders) >= (len(os.listdir('data/images/customize/gliders'))):
            num = random.randint(1, len(os.listdir('data/images/customize/gliders'))-1)
            while (num in not_in_shop_list[1]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/gliders'))-1)
        else:
            o=0
            num = random.randint(1, len(os.listdir('data/images/customize/gliders'))-1)
            while (num in not_in_shop_list[1]) or (num in gg) or (num in have_gliders):
                o+=1
                if o >= 200:
                    break
                num = random.randint(1, len(os.listdir('data/images/customize/gliders'))-1)
            while (num in not_in_shop_list[1]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/gliders'))-1)
        gg.append(num)
        item_shops.append(ItemShop(50 + (i+2)*200, 200, "glider", num))

    gg = []
    num = 0
    for i in range(2):
        if len(have_backpacks) >= (len(os.listdir('data/images/customize/backpacks'))):
            num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)
            while (num in not_in_shop_list[2]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)
        else:
            o=0
            num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)
            while (num in not_in_shop_list[2]) or (num in gg) or (num in have_backpacks):
                o+=1
                if o >= 200:
                    break
                num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)
            while (num in not_in_shop_list[2]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)

        # num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)
        # while (num in not_in_shop_list[2]) or (num in gg):
        #     num = random.randint(1, len(os.listdir('data/images/customize/backpacks'))-1)
        gg.append(num)
        item_shops.append(ItemShop(50 + (i)*200, 450, "backpack", num))

    gg = []
    num = 0
    for i in range(1):
        if len(have_emoticons) >= (len(os.listdir('data/images/customize/emoticons'))):
            num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
            while (num in not_in_shop_list[3]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
        else:
            o=0
            num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
            while (num in not_in_shop_list[3]) or (num in gg) or (num in have_emoticons):
                o+=1
                if o >= 200:
                    break
                num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
            while (num in not_in_shop_list[3]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
        # num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
        # while (num in not_in_shop_list[3]) or (num in gg):
        #     num = random.randint(1, len(os.listdir('data/images/customize/emoticons'))-1)
        gg.append(num)
        item_shops.append(ItemShop(50 + (i+2)*200, 450, "emoticon", num))

    gg = []
    num = 0
    for i in range(1):
        if len(have_sprays) >= (len(os.listdir('data/images/customize/sprays'))):
            num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
            while (num in not_in_shop_list[4]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
        else:
            o=0
            num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
            while (num in not_in_shop_list[4]) or (num in gg) or (num in have_sprays):
                o+=1
                if o >= 200:
                    break
                num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
            while (num in not_in_shop_list[4]) or (num in gg):
                num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
        # num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
        # while (num in not_in_shop_list[4]) or (num in gg):
        #     num = random.randint(1, len(os.listdir('data/images/customize/sprays'))-1)
        gg.append(num)
        item_shops.append(ItemShop(50 + (i+3)*200, 450, "spray", num))



rsm = Tick(650, 150, f'Reroll Shop (15 Prems)', font25)

bfgfg = Image("HUD/bp/bpbg2.svg")


class ItemShop():
    def __init__(self, x, y, type_of_offer, num, glide=0):
        self.rect = pygame.Rect(x, y, 180, 200)
        self.rect.topleft = (x, y)
        self.clicked = False
        self.glide = glide
        
        self.num = num
        
        self.name, self.rarity = get_skin_info(type_of_offer, self.num)

        self.image_of_skin = Image(f'customize/{type_of_offer}s/{self.num}.svg')

        if type_of_offer == "skin":
            self.fnt_size = int(26-math.log(len(self.name)+1))-1
            if (self.fnt_size > 26) or (len(self.name) < 13): self.fnt_size = 26
            if self.rarity==0:
                self.price = 0; self.col = (168, 168, 168)
            elif self.rarity == 1:
                self.price = 70; self.col = (120, 209, 105)
            elif self.rarity == 2:
                self.price = 140; self.col = (51, 107, 181)
            elif self.rarity == 3:
                self.price = 210; self.col = (127, 26, 171)
            elif self.rarity == 4:
                self.price = 300; self.col = (224, 117, 9)

        elif type_of_offer == "glider":
            self.fnt_size = int(26-math.log(len(self.name)+1))-1
            if (self.fnt_size > 26) or (len(self.name) < 13): self.fnt_size = 26
            self.image_of_skin = Scale(self.image_of_skin, 0.3)
            if self.rarity==0:
                self.price = 0; self.col = (168, 168, 168)
            elif self.rarity == 1:
                self.price = 15; self.col = (120, 209, 105)
            elif self.rarity == 2:
                self.price = 30; self.col = (51, 107, 181)
            elif self.rarity == 3:
                self.price = 45; self.col = (127, 26, 171)
            elif self.rarity == 4:
                self.price = 65; self.col = (224, 117, 9)

        elif type_of_offer == "backpack":
            self.fnt_size = int(((26-math.log(len(self.name)+1))-1) / 1.2)
            if (self.fnt_size > 26) or (len(self.name) < 13): self.fnt_size = 26
            # self.image_of_skin = Scale(self.image_of_skin, 1)
            if self.rarity==0:
                self.price = 0; self.col = (168, 168, 168)
            elif self.rarity == 1:
                self.price = 25; self.col = (120, 209, 105)
            elif self.rarity == 2:
                self.price = 50; self.col = (51, 107, 181)
            elif self.rarity == 3:
                self.price = 75; self.col = (127, 26, 171)
            elif self.rarity == 4:
                self.price = 100; self.col = (224, 117, 9)

        elif type_of_offer == "emoticon":
            self.fnt_size = int(26-math.log(len(self.name)+1))-1
            if (self.fnt_size > 26) or (len(self.name) < 13): self.fnt_size = 26
            # self.image_of_skin = Scale(self.image_of_skin, 1)
            if self.rarity==0:
                self.price = 0; self.col = (168, 168, 168)
            elif self.rarity == 1:
                self.price = 15; self.col = (120, 209, 105)
            elif self.rarity == 2:
                self.price = 30; self.col = (51, 107, 181)
            elif self.rarity == 3:
                self.price = 45; self.col = (127, 26, 171)
            elif self.rarity == 4:
                self.price = 60; self.col = (224, 117, 9)

        elif type_of_offer == "spray":
            self.fnt_size = int(26-math.log(len(self.name)+1))-1
            if (self.fnt_size > 26) or (len(self.name) < 13): self.fnt_size = 26
            self.image_of_skin = Scale(self.image_of_skin, 0.5)
            if self.rarity==0:
                self.price = 0; self.col = (168, 168, 168)
            elif self.rarity == 1:
                self.price = 20; self.col = (120, 209, 105)
            elif self.rarity == 2:
                self.price = 40; self.col = (51, 107, 181)
            elif self.rarity == 3:
                self.price = 60; self.col = (127, 26, 171)
            elif self.rarity == 4:
                self.price = 80; self.col = (224, 117, 9)

        self.type_of_offer = type_of_offer


        if (self.type_of_offer, self.num) in bundle_prices:
            self.price = bundle_prices[(self.type_of_offer, self.num)]
        self.txt, self.fnt = self.name, font

        
        
        # except: self.image_of_skin = Image(f'{type_of_offer}s/{self.num}.png')


        

    def draw(self):
        if self.type_of_offer == "skin": global have_skins; self.corresponding_list = have_skins
        elif self.type_of_offer == "glider": global have_gliders; self.corresponding_list = have_gliders
        elif self.type_of_offer == "backpack": global have_backpacks; self.corresponding_list = have_backpacks
        elif self.type_of_offer == "emoticon": global have_emoticons; self.corresponding_list = have_emoticons
        elif self.type_of_offer == "spray": global have_sprays; self.corresponding_list = have_sprays

        action = False
        pos = pygame.mouse.get_pos()
        
        col = self.col
        if self.rect.collidepoint(pos):
            col = (233, 233, 233)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                # if ismm: 
                    self.clicked = True

        global menu_state
        # if logged_in_any:
        if 1:
          if self.clicked and pygame.mouse.get_pressed()[0] == 0:
            # if ismm:
                action = True
                global prems
                global cork
                cork = []
                global cork_index
                cork_index = 0

                if (self.type_of_offer, self.num) in bundles:
                    for bundle in bundles[(self.type_of_offer, self.num)]:
                        scsc = Body()
                        scsc.num = bundle[1]
                        if bundle[0] == "skin": cor = have_skins
                        elif bundle[0] == "glider": cor = have_gliders
                        elif bundle[0] == "backpack": cor = have_backpacks
                        elif bundle[0] == "emoticon": cor = have_emoticons
                        elif bundle[0] == "spray": cor = have_sprays
                        scsc.corresponding_list = cor
                        scsc.price = self.price #DONT CHANGE
                        scsc.type_of_offer = bundle[0]
                        scsc.image_of_skin = Image(f'customize/{bundle[0]}s/{bundle[1]}.svg')
                        if bundle[0] == "spray":
                            scsc.image_of_skin = Scale(scsc.image_of_skin, 0.5)
                        if bundle[0] == "glider":
                            scsc.image_of_skin = Scale(scsc.image_of_skin, 0.3)
                        if bundle[0] == "backpack":
                            scsc.image_of_skin = Scale(scsc.image_of_skin, 1.3)

                        cork.append(scsc)
                else:
                    scsc = Body()
                    scsc.num = self.num
                    scsc.corresponding_list = self.corresponding_list
                    scsc.price = self.price
                    scsc.type_of_offer = self.type_of_offer
                    scsc.image_of_skin = Image(f'customize/{self.type_of_offer}s/{self.num}.svg')
                    if self.type_of_offer == "spray":
                        scsc.image_of_skin = Scale(scsc.image_of_skin, 0.5)
                    if self.type_of_offer == "glider":
                        scsc.image_of_skin = Scale(scsc.image_of_skin, 0.3)
                    if self.type_of_offer == "backpack":
                            scsc.image_of_skin = Scale(scsc.image_of_skin, 1.3)
                    cork.append(scsc)
                global menu_state
                menu_state = "is"
                self.clicked = False

             


        pygame.draw.rect(screen, col, self.rect)
        pygame.draw.rect(screen, (100, 149, 237), self.rect, 4)

        screen.blit(self.image_of_skin, (self.rect.x + 65, self.rect.y + 90))
        if self.fnt_size in FONT_CACHE:
            f = FONT_CACHE[self.fnt_size]
        else:
            f = pygame.font.SysFont("bahnschrift", self.fnt_size)
            FONT_CACHE[self.fnt_size] = f
        draw_text(self.txt, f, 0, self.rect.x + 5, self.rect.y + 5, color=(0,0,0))
        draw_text((f"{self.price} Prems"), font27, 0, self.rect.x + 5, self.rect.y + 42, color=(0,0,0))

        draw_text((f"{self.type_of_offer.capitalize()}"), font20, 0, self.rect.x + 2, self.rect.y + self.rect.height + 4, color=(0,0,0))

        if (self.num in self.corresponding_list):
            draw_text(("Owned!"), font27, 0, self.rect.x + 5, self.rect.y + self.rect.width - 15, color=(0,0,0))

        return action

FONT_CACHE = {}

cork_index = 0
bundles = {

    ("skin", 122): [("skin", 122), ("backpack", 57)], 
    ("skin", 123): [("skin", 123), ("skin", 124), ("backpack", 58)], 
    ("skin", 125): [("skin", 125), ("emoticon", 70),], 
    ("skin", 126): [("skin", 126), ("backpack", 59), ("glider", 55),], 
    ("skin", 127): [("skin", 127), ("backpack", 60), ("spray", 63),], 
    ("skin", 128): [("skin", 128), ("skin", 129), ("backpack", 61),], 
    ("skin", 130): [("skin", 130), ("backpack", 62)], 

}

bundle_prices = {
    ("skin", 126): 180,
    ("skin", 127): 230,
    ("skin", 128): 170,


}
checklist = []

fint = {
    "ls": "customize/ls",
    "skin": "customize/skins",
    "backpack": "customize/backpacks",
    "glider": "customize/gliders",
    "trail": "customize/trails",
    "emoticon": "customize/emoticons",
    "spray": "customize/sprays",
    "music": "customize/musics",
    "prems": "ess",
}

wmove_b = Tick(50, 210, 'W/UP Key Movement & Mouse Rotation', font30)
cuser_b = Tick(50, 260, 'Change Username', font30)
cpass_b = Tick(50, 310, 'Change Password', font30)
contr_b = Tick(50, 360, 'Controller in-Game: Off', font30)
pin_b = Tick(50, 410, 'Emoji / Spray Screen: On', font30)
instr_b = Tick(50, 460, 'How to Play (Controls / Instructions)', font30)

pin_screen = True


def mbp(start, stop, gang, minced=False):
    if gang:
        global bpv, bpi, bpr, thyr, bpo
        diqt = lvl_grants
        thyr = {}
        bpv = []
        bpr = []
        bpi = []
        bpo = []
        for a, i in enumerate(diqt):
            kin = lvl_grants[i][0]
            formt = "svg"
            if lvl_grants[i][1] == "prems":
                kin = "prem"
            if lvl_grants[i][1] == "ls":
                formt = "png"
                img= Smoothscale(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'), 0.15)
            elif lvl_grants[i][1] == "glider":
                img= Scale(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'), 0.3)
            elif lvl_grants[i][1] == "skin":
                img= Scale(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'), 1.5)
                
            else:
                img=Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}')

            if lvl_grants[i][1] == "skin":
                bpo.append(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'))
            else:
                bpo.append(0)

            jpp = img.copy()

            if lvl_grants[i][1] in thyr:
                thyr[lvl_grants[i][1]] += 1
            else:
                thyr[lvl_grants[i][1]] = 0

            b = BP(100 + a * 110, 500, img, 1, glide=(i), glide2=234, glide3=thyr[lvl_grants[i][1]])
            

            j=pygame.Rect(b.rect.x-5, b.rect.y-5, 100, 100)
            bpr.append(j)
            if b.na == False:
                        b.rect.x = j.center[0] - (b.image.get_width() / 2)
                        b.rect.y = j.center[1] - (b.image.get_height() / 2)
                        b.ogx = b.rect.x
                        b.na = True
            while b.image.get_width() > 90:
                b.image = Smoothscale(b.image, 0.9)
                b.rect = b.image.get_rect()
                b.rect.x = j.center[0] - (b.image.get_width() / 2)
                b.rect.y = j.center[1] - (b.image.get_height() / 2)
                b.ogx = b.rect.x
            if lvl_grants[i][1] == "emoticon":
                b.rect.x -= 15
                b.ogx = b.rect.x
                b.rect.y += 13

            jpp = pygame.transform.scale2x(jpp)
            while jpp.get_width() > 200:
                jpp = Smoothscale(jpp, 0.8).convert_alpha()
            bpi.append(jpp)

            bpv.append(b)
    else:
        global nbpv, nbpi, nbpr, nthyr
        diqt = {}
        for i in range(start, stop):
            if i >= 70:
                break
            if battle_passes[current_season-2]:
                if minced:
                    if lvl_grants[i+1][2] == True:
                        diqt[i+1] = lvl_grants[i+1]
                else:
                    diqt[i+1] = lvl_grants[i+1]
            else:
                if lvl_grants[i+1][2] == False:
                    diqt[i+1] = lvl_grants[i+1]

        nthyr = {}
        nbpv = []
        nbpr = []
        nbpi = []
        for a, i in enumerate(diqt):
            kin = lvl_grants[i][0]
            formt = "svg"
            if lvl_grants[i][1] == "prems":
                kin = "prem"
            if lvl_grants[i][1] == "ls":
                formt = "png"
                img= Smoothscale(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'), 0.15)
            elif lvl_grants[i][1] == "glider":
                img= Scale(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'), 0.3)
            elif lvl_grants[i][1] == "skin":
                img= Scale(Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}'), 1.5)
            else:
                img=Image(f'{fint[lvl_grants[i][1]]}/{kin}.{formt}')

            jpp = img.copy()

            if lvl_grants[i][1] in thyr:
                thyr[lvl_grants[i][1]] += 1
            else:
                thyr[lvl_grants[i][1]] = 0

            b = BP(100 + a * 110, 500, img, 1, glide=(i), glide2=234, glide3=thyr[lvl_grants[i][1]])
            

            j=pygame.Rect(b.rect.x-5, b.rect.y-5, 100, 100)
            nbpr.append(j)
            if b.na == False:
                        b.rect.x = j.center[0] - (b.image.get_width() / 2)
                        b.rect.y = j.center[1] - (b.image.get_height() / 2)
                        b.ogx = b.rect.x
                        b.na = True
            while b.image.get_width() > 90:
                b.image = Smoothscale(b.image, 0.9)
                b.rect = b.image.get_rect()
                b.rect.x = j.center[0] - (b.image.get_width() / 2)
                b.rect.y = j.center[1] - (b.image.get_height() / 2)
                b.ogx = b.rect.x
            if lvl_grants[i][1] == "emoticon":
                b.rect.x -= 15
                b.ogx = b.rect.x
                b.rect.y += 13

            jpp = pygame.transform.scale2x(jpp)
            while jpp.get_width() > 200:
                jpp = Smoothscale(jpp, 0.8).convert_alpha()
            nbpi.append(jpp)

            nbpv.append(b)


mbp(1, 70, True)
mainbp = bpv[0]

bsco = 0

tinps = []

class TrashInput():
    def __init__(self, string, font, color, x, y, limit):
        self.str = string
        self.font = font
        self.x = x
        self.color = color
        self.y = y
        self.limit = limit
        self.updating = False
        tinps.append(self)
        self.returned = False

    def fk(self):
        self.updating = False

    def update(self, x, y, font, color):
        self.updating = True
        # TABNINE PRO DID THIS:
        # if len(self.str) < self.limit:
        #     draw_text(self.str, font, color, x, y)
        # else:
        #     draw_text(self.str[:self.limit], font, color, x, y)
        if self.str == '':
            draw_text('Start typing...', font, (0), x, y)
        else:
            draw_text(self.str, font, color, x, y)

        if self.returned:
              return self.str
        
joysticks = []

def ca(s):
    u = {"X": "^", "Z": "v", "SPACE": "A", "SPACE2": "B", "C": ">", "V": "<", "T": "B", "U": "▯", "P": "Right Joystick"}
    if contr:
        return u[s]
    if s == "SPACE2": return "SPACE"
    return s


# HUD functions
def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_bar(surf, x, y, pct, col, size=1, w=100, h=20):
    if pct < 0:
        pct = 0
    BAR_LENGTH = w * size
    BAR_HEIGHT = h * size
    fill = pct * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

if not replit: pygame.mixer.pre_init(44100, 16, 2, 4096)

reticle_img = Image("ess/rect.svg")

ranked = False

def grab_foff(n):
    return friendoff[n]

default_map_img = Image("HUD/maps/none.png")
nbdefault_map_img = Image("HUD/maps/nonenb.png")

dmih = default_map_img.get_height()
dmiw = default_map_img.get_width()

rlr = False

nsx = -800
boux = 0
checklister = []
checktick = []

rp = 0

menu_state = "main"
class Game:
    def __init__(self):
        pygame.init()
        self.screen = screen
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(Image("customize/skins/0.svg"))

        self.clock = pygame.time.Clock()
        self.bullet_img = Image('ess/bullets/bullet.svg')
        self.trade_img = Image('ess/trade.svg')



        self.mode = "Solos"
        self.ranked = ranked

        self.s = pygame.Surface((WIDTH, HEIGHT))   # per-pixel alpha

        

        self.load_images()

    def load_images(self):
        self.non = Image('ess/blank.svg')

        self.img_rarities = []
        for i in range(len(os.listdir('data/images/HUD/display_rarity'))):
            self.img_rarities.append(Image(f'HUD/display_rarity/{i}.svg'))

        self.img_weapons = []
        for i in range(len(os.listdir('data/images/weapons/cards'))):
            img = Image(f'weapons/cards/{i}.svg')
            self.img_weapons.append(img)

        self.img_p_rarity = []
        for i in range(len(os.listdir('data/images/HUD/pickup_rarity'))):
            self.img_p_rarity.append(Image(f'HUD/pickup_rarity/{i}.svg'))

        self.nature_imgs = []
        for i in range(len(os.listdir('data/images/tiles/nature'))):
            self.nature_imgs.append(Image(f'tiles/nature/{i}.svg'))

        self.tp_wp_imgs = []
        for i in range(len(BULLET_DAMAGE)):
            self.tp_wp_imgs.append(Image(f'weapons/tp/{i}.svg'))     

        self.tree_images = []
        for i in range(len(os.listdir('data/images/ess/trees'))):
            self.tree_images.append(Image(f'ess/trees/{i}.svg'))

        self.contrail_imgs = []
        for i in range(len(os.listdir('data/images/customize/trails'))):
            self.contrail_imgs.append(Image(f'customize/trails/{i}.svg'))

        self.EXPLOSION_IMGS = [] 
        for i in range(6):
            im = Image(f"random/explosion/{i}.png")
            self.EXPLOSION_IMGS.append(Scale(im, 0.4))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.in_range = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.ultimas = pygame.sprite.Group()

        self.layers = [[],[],[],[],[]]

        self.gunhelds = pygame.sprite.Group()
        self.friends = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()  
        self.props = pygame.sprite.Group()  
        self.team = pygame.sprite.Group()          

        self.bullets = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()
        self.storm = pygame.sprite.Group()
        self.shadow_tiles = pygame.sprite.Group()
        self.gang = pygame.sprite.Group()
        self.nature = pygame.sprite.Group()
        self.trees = pygame.sprite.Group()
        self.construction = pygame.sprite.Group()
        self.water = pygame.sprite.Group()

        self.friend_kb = []

        self.vehicles = pygame.sprite.Group()

        self.airdrops = pygame.sprite.Group()
        self.airdrops.empty()
        
        self.chests = pygame.sprite.Group()

        self.water = pygame.sprite.Group()

        self.contr = contr

        self.first_layer = pygame.sprite.Group()
        self.second_layer = pygame.sprite.Group()
        self.third_layer = pygame.sprite.Group()

        self.front_layer = pygame.sprite.Group()

        self.offgrid = pygame.sprite.Group()

        self.discoveries = pygame.sprite.Group()
        self.discoveries.empty()

        self.pressing_e = False
        self.map_should_on = False

        self.pressing_u = False
        self.fry_should_on = True

        self.ldep = False

        self.joysticks = joysticks

        self.hud_on = hud_on

        self.storm_poses = []

        self.hopoff = [False, False, False, False, False, False, False, False, False, False, False]

        self.nearby_tiles = []

        self.iter1 = 0
        self.iter2 = 0

        self.squads = []
        for i in range(100):
            self.squads.append([])

        self.grid = {}

        a1, b1 = 100, 100
        if self.mode == "Marvel Mayhem":
            a1, b1 = 100, 200
        self.standard_hp = a1
        self.standard_sp = b1

        self.phase_timer = 0

        self.rumble = 0

        self.phase_cooldown = 0

        self.on_bus = True

        self.bosses = []

        self.hashed = True

        if contr:
            df = " (X)"
        else: df = ""
        self.swispe = Tick(WIDTH-200, HEIGHT-50, f'Cycle Player{df}', font20)
        

        self.wall_poses = []

        self.maxdeathcd = 40
        self.deathcd = self.maxdeathcd

        self.elimtim = 0

        self.splashed = False
        self.lem = None


        self.map = json.load(open(f'data/maps/map.json'))
        posesx, posesy = [], []
        uposesx, uposesy = [], []
        self.mob_count  = 0

        self.tiles = list(self.map['tilemap'].values())

        self.access_index = 0
        self.len_tiles = len(self.tiles)

        self.elims = 0
        self.felims = 0

        self.fps_tac = [10000.0, 0.0]

        self.pauses = 3



        for tile in (self.map['tilemap']).values():
            posesx.append(tile['pos'][0] * TILESIZE); posesy.append(tile['pos'][1] * TILESIZE)
            uposesx.append(tile['pos'][0]); uposesy.append(tile['pos'][1])

        self.uposes = uposesx, uposesy
        self.poses = posesx, posesy

        self.uposesx, self.uposesy = self.uposes
        self.posesx, self.posesy = self.poses

        self.backpack_num = backpack_num
        self.emoticon_num = emoticon_num
        self.spray_num = spray_num

        self.nonat = False
        
        self.wvec = []

        #left, up, right, down
        # log(min(uposesx), min(uposesy), max(uposesx), max(uposesy))

        h=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        if self.access_index <= self.len_tiles-1:
            for i in range(self.len_tiles):
                if self.access_index <= self.len_tiles-1: tile = self.tiles[self.access_index]
                path = f"tiles/{tile['type']}/{tile['variant']}.svg"
                if tile['type'] == 'walls':
                    self.grid[int(tile['pos'][0]), int(tile['pos'][1])] = Wall(self, tile['pos'][0], tile['pos'][1], Image(path))
                    self.wvec.append((int(tile['pos'][0]), int(tile['pos'][1])))

                if tile['type'] == 'nocol':
                    self.grid[int(tile['pos'][0]), int(tile['pos'][1])] = Noncol(self, tile['pos'][0], tile['pos'][1], Image(path), tile['variant'])

                if tile['type'] == 'nature' and (not (tile['variant'] in [8, 12])):
                    h[tile['variant']] += 1
                    self.grid[int(tile['pos'][0]), int(tile['pos'][1])] = Nature(self, tile['pos'][0], tile['pos'][1], tile['variant'])


                if tile['type'] == 'props':
                    Prop(self, tile['pos'][0], tile['pos'][1], Image(path), tile['constant'])

                if tile['type'] == 'vehicles':
                    Vehicle(self, tile['pos'][0], tile['pos'][1], Image(path), tile['constant'])

                # if tile['type'] == 'temp':
                #     if tile['variant'] == 0:
                #         self.player = Player(self, tile['pos'][0], tile['pos'][1])
                #     else:
                #         Mob(self, tile['pos'][0], tile['pos'][1])

                if hud_on:
                  if not ranked:
                    if self.mode in ["Solos", "Duos", "Squads"]:
                        if tile['type'] == 'temp':
                            if tile['variant'] == 0:
                                ss = 49 #random.choice(UNVAULTED)
                                # while (ss in STACKABLES) or (ss in [53, 51, ]):
                                #     ss =  random.choice(UNVAULTED)

                                # if tile['pos'][1] > 140:
                                #     ss =  random.randint(15, 16)
                                Henchman(self, tile['pos'][0], tile['pos'][1], Image('random/henchman1.svg'), ss)
                                
                            if tile['variant'] == 1:
                                self.bosses.append(Boss(self, tile['pos'][0], tile['pos'][1], Image('customize/skins/116.svg'), 55, name="Iron Man"))
                            
                            if tile['variant'] == 2:
                                self.bosses.append(Boss(self, tile['pos'][0], tile['pos'][1], Image('customize/skins/107.svg'), 54, name="Black Widow"))

                            if tile['variant'] == 3:
                                self.bosses.append(Boss(self, tile['pos'][0], tile['pos'][1], Image('customize/skins/109.svg'), 61, name="Dr. Doom"))
               

                if tile['type'] == 'valuables':
                    if tile['variant'] == 0:
                        Chest(self, tile['pos'][0], tile['pos'][1])
                    elif (not ranked):
                        if self.mode in ["Solos", "Duos", "Squads", "Trios"]:
                            if random.randint(1, 4) == 1:
                                Chest(self, tile['pos'][0], tile['pos'][1], tp=4)

                self.access_index += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.JOYDEVICEADDED:
                        joy = pygame.joystick.Joystick(event.device_index)
                        joysticks.append(joy)



        self.new_run()


        
        self.pressing_m = False
        
       


    def new_run(self):
        self.skin_num = skin_num

        self.fill0 = fill0
        self.lobby = lobby

        uposesx, uposesy = self.uposes
        posesx, posesy = self.poses

        self.pathgrid = WeightedGrid(max(uposesx), max(uposesy))
        for wall in self.wvec:
            self.pathgrid.walls.append(vec(wall))

        self.player = Player(self, 1, 1)
        self.ogplayer = self.player
        self.player.active = False

        



        #top = miny , bottom = maxy, left = minx, right = maxx
        pipk = [
            (min(uposesx)+14, min(uposesy)+14,  45, (1, 1)),
            (max(uposesx)-14, min(uposesy)+14, 135, (-1, 1)),
            (max(uposesx)-14, max(uposesy)-14, 225, (-1, -1)),
            (min(uposesx)+14, max(uposesy)-14, 315, (1, -1)),

            (((max(uposesx) +14) // 2), min(uposesy)+14, 90 + 90, (0, 1)),
            (((max(uposesx) +14) // 2), max(uposesy)-14, 270 + 90, (0, -1)),
            (max(uposesx)-14, ((max(uposesy) - 14) // 2), 180 + 90, (-1, 0)),
            (min(uposesx)+14, ((max(uposesy) - 14) // 2), 0 + 90, (1, 0)),

        ]

        self.discovered = discovered

        self.uposesx = uposesx; self.uposesy = uposesy

        # Discovery(self, 38, 13, 0)
        # Discovery(self, 55, 98, 1)
        # Discovery(self, 69, 149, 2)
        # Discovery(self, 143, 125, 3)
        # Discovery(self, 144, 64, 4)
        # Discovery(self, 98, -60, 5)
        # Discovery(self, 189, -42, 6)
        # Discovery(self, 218, 40, 7)
        # Discovery(self, 230, 132, 8)

        cho = random.choice(pipk)
        
        self.discovered = discovered
        self.map_img = default_map_img
        if ranked:
            self.map_img = nbdefault_map_img
        if not (self.mode in ["Solos", "Duos", "Squads", "Trios"]):
            self.map_img = nbdefault_map_img

        self.map_imgs = []
        for i in range(9):
            self.map_imgs.append(Image(f"HUD/s5map/{i}{self.discovered[i]}.png"))
        self.bus_rt_img = Image(f'HUD/maps/{pipk.index(cho)}.png')
        
        self.mptim = 0

        self.bus_time_over = False

        self.w_move = w_move

        self.center = vec(72*64, 69*64)

        
        self.mx_players = 50

        self.ldtim = 0

        self.bus = Bus(self, vec(cho[0], cho[1]) * TILESIZE, cho)

        self.player.pos = self.bus.pos

        self.nature_index = 0

        self.nat_list = list(self.nature)

        self.camera = Camera(max(posesx), max(posesy))

        self.fake_player_count = self.mx_players - self.bus.mobs_on_board 

        self.bus_time = 0

        self.tree_index = 0

        self.player_died = 0
        self.player_at_count = 0

        if self.mode == "Marvel Mayhem":
            self.lootpool = UNVAULTED_MM
        elif self.mode == "Shotgun Special":
            self.lootpool = UNVAULTED_CE
        else:
            self.lootpool = UNVAULTED
        self.lootpoolm = self.lootpool.copy()

        banned = [53, 43, 9, 10, 11, 12, 60]
        for v in banned:
            if v in self.lootpoolm: self.lootpoolm.remove(v)
        

        self.friend_ranks = []
        self.friend_mranks = []

        for i in range(self.bus.friends_on_board):
            if ranked:
                r = abs((get_rank(rp)) + random.randint(-2, 2))
                if r > 17:
                    r = 17
                r2 = abs(r + random.randint(0, 5))
                if r2 > 17:
                    r2 = random.randint(16, 17)
            else:
                r = 0
                r2 = 0
            
            self.friend_ranks.append(r)
            self.friend_mranks.append(r2)


        self.ror = 0

        self.ww = 0

        self.cremoved = False

        self.unis = 0

        self.airdrop_text_timer = 0

        self.backpack_num = backpack_num
        self.emoticon_num = emoticon_num
        self.spray_num = spray_num

        self.paused = False


        StormTile(self, min(uposesx), min(uposesy), 'right', posesx, posesy)

        StormTile(self, min(uposesx), min(uposesy), 'up', posesx, posesy)

        StormTile(self, max(uposesx), min(uposesy), 'left', posesx, posesy)

        StormTile(self, min(uposesx), max(uposesy), 'down', posesx, posesy)

        self.players = self.mx_players

        self.maxuposesx = max(uposesx)
        self.maxuposesy = max(uposesy)
        self.minuposesx = min(uposesx)
        self.minuposesy = min(uposesy)

        

        self.friend_names = []

        self.player.health = self.player.max_health

        self.pressing_q = False
        self.chl_should_on = False

        global challenges
        cc_tracker[1] = 0
        cc_tracker[4] = 0
        cc_tracker[5] = 0
        cc_tracker[8] = 0

        self.mob_index = 0

        self.at_match_lvl = season_tiers[current_season-2]
        


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x

            if self.clock.get_fps() > 1: self.jdt = FPS / self.clock.get_fps()
            else: self.jdt = 0.7
            self.events()
            if not self.paused:
                self.update()
            self.draw()
    
    def quit(self):
        pygame.quit()
        sys.exit()

    def path(self, start, goal):
        return a_star_search(self.pathgrid, start, goal, s=1)

    def update(self):
        self.picking_up = False
        self.player.reviving_someone = None
        self.nonat = False
        self.hashed = True
        # update portion of the game loop

        check_xp()
        global season_xp
        self.season_xp = season_xp


        self.in_range.update()

        # ms = list(self.mobs)
        # if len(ms) > 0:
        #     for i in range(30):
        #         if self.mob_index < len(ms):
        #             ms[self.mob_index].update()
        #         self.mob_index += 1
        #         if self.mob_index >= len(ms):
        #             self.mob_index = 0
        #             break


        self.mobs.update()
        self.gunhelds.update()

        # lst = list(self.mobs)
        # for i in range(20):
        #     try:
        #         mob = lst[self.iter1]
        #     except:
        #         break
        #     mob.update()

        #     self.iter1 += 1
        #     if self.iter1 >= len(lst):
        #         self.iter1 = 0

        
        self.bullets.update()

        # lst = list(self.friends)
        # for i in range(1):
        #     try:
        #         mob = lst[self.iter2]
        #     except:
        #         break
        #     mob.update()

        #     self.iter2 += 1
        #     if self.iter2 >= len(lst):
        #         self.iter2 = 0

        self.friends.update()
        self.storm.update()
        self.airdrops.update()

        # self.discoveries.update()

        

        

        self.friend_list = friend_list
        self.lobby = lobby
        self.skin_num = skin_num
        self.glider_num = glider_num
        self.backpack_num = backpack_num
        self.emoticon_num = emoticon_num
        self.spray_num = spray_num
        self.trail_num = trail_num
        self.cc_tracker = cc_tracker
        self.challenges = challenges
        self.cc_complete = cc_complete
        self.ranked = ranked
        global discovered
        self.discovered = discovered
        global rp
        self.rp = rp


        check_xp()
        
        
        pygame.sprite.groupcollide(self.trees, self.bullets, True, True)
        
        
        

        if self.ror == 0:
            if len(self.friends) > 0:
                self.ror = 1
                self.friend_kb = []
                self.swispe = Tick(WIDTH-200, HEIGHT-50, f'Cycle Player', font20)
                for i, m in enumerate(self.friends):
                        if not (m.name in friend_list):
                           self.friend_kb.append(Tick(65, 400 + i*60, f'Would you like to friend {m.name}?', font30, glide=m.name, glide2=m.skin_num))
                        else:
                            self.friend_kb.append(Tick(65, 400 + i*60, f'Already friended {m.name}!', font30, glide=m.name, glide2=m.skin_num))

            if self.mode == 'Solos': self.friend_kb = []
                           
        if self.tree_index < 50:
            self.tree_index += 1
            for some in range(3): Prop(self, random.randrange(min(self.uposesx)+7, max(self.uposesx)-7), random.randrange(min(self.uposesy)+7, max(self.uposesy)-7), self.tree_images[random.randint(0, 3)], random.randint(0, 359), onnatural=True)
            
        if not self.bus_time_over: self.fake_player_count = self.mx_players - self.bus.mobs_on_board - 1; self.bus_time += 1
        
        if self.bus_time >= 1200:
            if not self.bus.dropped_player: self.bus.drop_player()
            self.bus_time_over = True
            self.bus_time = 0
            
            self.fake_player_count = self.bus.mobs_on_board - 1
            self.bus.kill()

        if self.on_bus: self.camera_focus_on = self.bus
        else: self.camera_focus_on = self.player
        self.camera.update(self.camera_focus_on)

        
        tings = [self.first_layer, self.second_layer, self.third_layer, self.front_layer]
        # L = list(self.offgrid)
        for sprite in self.offgrid:
            # if self.iter1 < len(L): 
            #     sprite = L[self.iter1]
            # else: break
            if not (isinstance(sprite, Bus)):
                  inrad = self.camera_focus_on.isinrad(sprite)
                  if inrad and (not (sprite in self.in_range)):
                      
                    self.in_range.add(sprite)

                    plu = 0
                    for i in range(4):
                          if not (sprite in self.layers[i]):
                            if sprite in tings[i]:
                              plu = 1
                              self.layers[i].append(sprite)

                    if plu == 0:
                        self.layers[4].append(sprite)

                  elif not inrad and ((sprite in self.in_range)):
                      self.in_range.remove(sprite)
                      for i in range(5):
                          if sprite in self.layers[i]:
                              self.layers[i].remove(sprite)
            else:
                if not (sprite in self.in_range): 
                    self.in_range.add(sprite)
                    plu = 0
                    for i in range(4):
                          if not (sprite in self.layers[i]):
                            if sprite in tings[i]:
                              plu = 1
                              self.layers[i].append(sprite)

                    if plu == 0:
                        self.layers[4].append(sprite)

            # self.iter1 += 1
            # if self.iter1 >= len(L):
            #     self.iter1 = 0
  

        self.nearby_tiles = []
        for x in range(-9, 9):
            for y in range(-7, 7):
                try:
                    self.nearby_tiles.append((self.camera_focus_on.tilex + x, self.camera_focus_on.tiley + y))
                    t = self.grid[self.camera_focus_on.tilex + x, self.camera_focus_on.tiley + y]
                    if not (t in self.in_range): 
                        self.in_range.add(t)
                        plu = 0
                        for i in range(4):
                            if not (t in self.layers[i]):
                                if t in tings[i]:
                                    plu = 1
                                    self.layers[i].append(t)

                        if plu == 0:
                            self.layers[4].append(t)
                except: pass 

        if self.nonat == False:
            self.type_foot = "foot"

        # if self.rumble > 0:
        #     self.rumble -= 1
        #     for joystick in self.game.joysticks:
        #             joystick.stop_rumble()
        # if self.rumble <= 0: self.rumble = 0

        if self.on_bus:
            self.player.pos = self.bus.pos.copy()

        global menu_state

        if self.player_died: 
            sysd = 1
        else: 
            sysd = 0
        if self.players > 1:
            if len(self.mobs) == (sysd + 1) and self.bus_time_over and (not self.ldep):
                r = list(self.mobs)
                utr = [r[-1].skin_num, r[-1].backpack_num]
                r[-1].health = 0; r[-1].knocked_health = 0
                r[-1].yof = True
                # for i in self.mobs:
                #     i.health = 0; i.knocked_health = 0
                self.fake_player_count = 0
                if random.randint(1, 2) == 1: c = 1
                else: c = -1
                if random.randint(1, 2) == 1: d = 1
                else: d = -1
                Audio(f"weapons/{random.choice([53,53,60])}.wav")
                self.ldtim = 100
                Mob(self, self.player.tilex + (random.randint(3, 9) * c), self.player.tiley + (random.randint(3, 7) * d), stacked=True, tn=0, sk=utr)
                self.ldep = True

            if self.bus_time_over:
                if self.bus.dropped_player:
                    if self.player.gliding == False:
                        if random.randint(1, 1000) == 1:
                            if len(self.mobs) > 0:
                                h = list(self.mobs)
                                r = random.choice(h) 
                                u=0
                                while r in self.in_range:
                                    r = random.choice(h) 
                                    u+=1
                                    if u >= 500:
                                        break
                                utr = [r.skin_num, r.backpack_num]
                                r.health = 0; r.knocked_health = 0
                                r.yof = True
                                # for i in self.mobs:
                                #     i.health = 0; i.knocked_health = 0
                                if random.randint(1, 2) == 1: c = 1
                                else: c = -1
                                if random.randint(1, 2) == 1: d = 1
                                else: d = -1
                                Audio("weapons/53.wav")
                                Mob(self, self.player.tilex + (random.randint(3, 9) * c), self.player.tiley + (random.randint(4, 7) * d), stacked=True, tn=0, sk=utr)

        if self.player.health <= 0:
          if self.mode != "Solos":
            #if it is not solos
            if self.player.knocked_health <= 0:
                self.deathcd -= 1
                if len(self.mobs) != 0: 
                    self.player.kill()
                    if self.deathcd <= 0:
                        if len(self.friends) != 0:
                            m = random.choice(list(self.friends))
                        else:
                            m = random.choice(list(self.mobs))
                        self.camera_focus_on = m
                        self.player = m
                        self.deathcd = self.maxdeathcd
                    if self.player_died == False:
                            if self.bus_time_over: self.player_at_count = len(self.mobs)+self.fake_player_count+len(self.friends)+1
                            else: self.player_at_count = random.randint(80, 100)
                    self.player_died = True
                else: 
                    if self.player_died:
                        global af; af = True
                    self.quit_match()
          else:
            self.deathcd -= 1
            if len(self.mobs) != 0: 
                self.player.kill()
                if self.deathcd <= 0:
                    m = random.choice(list(self.mobs))
                    self.camera_focus_on = m
                    self.player = m
                    self.deathcd = self.maxdeathcd
                if self.player_died == False:
                        if self.bus_time_over: self.player_at_count = len(self.mobs)+self.fake_player_count+len(self.friends)+1
                        else: self.player_at_count = random.randint(80, 100)

                self.player_died = True
            else:
                if self.player_died:
                    af = True
                self.quit_match()
        
        sqa = 1
        if self.player_died:
            sqa = 0
        self.players = len(self.mobs)+self.fake_player_count+sqa+len(self.friends)

        
        if self.phase_timer <= 0:
            if self.mode in ["Team Rumble", "Shotgun Special"]:
                self.phase_cooldown -= 0 #self.jdt * 1
            else:
                self.phase_cooldown -= self.jdt * 3

            if self.phase_cooldown <= 0:
                self.phase_timer = 3000
                if self.players < 40:
                 if self.bus_time_over:
                  if random.randint(0, 0) == 0:
                    self.airdrop_text_timer = 700
                    Airdrop(self, random.randint(0, max(self.uposesx)), random.randint(0, max(self.uposesy)))
        else:
            if self.mode in ["Team Rumble", "Shotgun Special"]:
                self.phase_timer -= self.jdt * 1000
            else:
                self.phase_timer -= self.jdt * 3
            if self.phase_timer <= 0: self.phase_cooldown = 6000

        if self.fake_player_count > 0:
            if random.randint(0,75) == 0:
                self.fake_player_count -= 1

        season_xp = self.season_xp
        discovered = self.discovered

     


    

        

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def wall_exists(self, p):
        if (int(p.x), int(p.y)) in self.wall_poses:
                return True
        return False

    def draw(self):
        self.screen.fill("#3B7732")

        # your code here    

        # self.draw_grid()

        # for sprite in self.in_range:
        #     self.screen.blit(sprite.image, self.camera.apply(sprite))
        qin = set(self.offgrid)
        for sprite in self.in_range.copy():
          if not (sprite in qin):
            if not ((sprite.x, sprite.y) in self.nearby_tiles):
                self.in_range.remove(sprite)  
        del qin




        # for sprite in self.layers[4]:
        #     try: sprite.draw()
        #     except: pass
        #     self.screen.blit(sprite.image, self.camera.apply(sprite))
        #     if sprite.alive() == False: self.layers[4].remove(sprite)
        
        
        for sprite in self.layers[0]:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if sprite.alive() == False: self.layers[0].remove(sprite)

        for sprite in self.storm:
            pygame.draw.rect(self.screen, (203, 195, 227), pygame.Rect(self.camera.apply(sprite)[0], self.camera.apply(sprite)[1], sprite.rect.width, sprite.rect.height))

        

        for sprite in self.layers[1]:
            try: sprite.draw()
            except: pass
            if isinstance(sprite, (Vehicle)): sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if sprite.alive() == False: self.layers[1].remove(sprite)

        for sprite in self.layers[2]:
                if isinstance(sprite, (Boss, Henchman)): sprite.draw()
                if isinstance(sprite, (Mob, Vehicle, Player, Friend, Boss, Henchman)): sprite.draw_health()
                self.screen.blit(sprite.image, self.camera.apply(sprite))
                if sprite.alive() == False: self.layers[2].remove(sprite)
                
                

        for sprite in self.layers[3]:
            try: sprite.draw()
            except: pass
            if isinstance(sprite, (Mob, Vehicle, Player, Friend, Boss, Henchman)): sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if sprite.alive() == False: self.layers[3].remove(sprite)

        for i in self.gunhelds:
            self.screen.blit(i.image, self.camera.apply(i))
        
        # self.draw_grid()

            
        # pygame.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        
        global season_xp
        global season_tiers
        global rp
        if not logged_in_any:
            season_xp = 0
            season_tiers[current_season-2] = 1

        
            # HUD functions
        if hud_on:
            if ((self.deathcd == self.maxdeathcd)):
                if self.player_died == False:
                    draw_text(f'{username}', font, 0, 10, 5, color=(0,0,0))
                    if (ranked) and (rp > 0):
                        col = rank_colors[get_rank(max_rp)]
                        draw_text(f'{username}', font, 0, 8, 5, color=col)
                
                if self.player.health <= 0:
                    draw_bar(self.screen, 10, 80, self.player.knocked_health / 100, (255, 0, 0), size=2)
                    draw_bar(self.screen, 10, 40, self.player.revive_process / 100, (0, 255, 0), size = 2)

                    draw_text(f'{int(self.player.revive_process)}%', font, 0, 215, 45, color=(0,0,0))
                    draw_text(f'{int(self.player.knocked_health)} / 100', font, 0, 215, 85, color=(0,0,0))
                else:
                    draw_bar(self.screen, 10, 40, self.player.shield / self.player.max_shield, (0, 255, 255), size = 2)
                    draw_bar(self.screen, 10, 80, self.player.health / self.player.max_health, (0, 255, 0), size=2)

                    draw_text(f'{int(self.player.shield)} / {self.player.max_shield}', font, 0, 215, 45, color=(0,0,0))
                    draw_text(f'{math.ceil(self.player.health)} / {self.player.max_health}', font, 0, 215, 85, color=(0,0,0))


            if self.player.on_vehicle:
                draw_bar(self.screen, 10, 410, self.player.vehicle.fuel / self.player.vehicle.mfuel, (255, 140, 0), size = 1)
                draw_text(f'{math.ceil(self.player.vehicle.fuel / self.player.vehicle.mfuel * 100)}% Fuel', font, 0, 125, 415, color=(0,0,0))

                draw_bar(self.screen, 10, 450, self.player.vehicle.health / self.player.vehicle.mhealth, (0, 255, 0), size = 1)
                draw_text(f'{math.ceil(self.player.vehicle.health / self.player.vehicle.mhealth * 100)}% Hull Integrity', font25, 0, 125, 455, color=(0,0,0))
            
            if not self.map_should_on:
                draw_bar(self.screen, 10, HEIGHT - 150, season_xp / 10000, (0, 0, 255), size = 1.5)
                draw_text(f'{int(season_xp)} / 10000  (Season Level {season_tiers[current_season-2]})', font20, self, 10, HEIGHT - 100, color=(0,0,0))

                if self.at_match_lvl+1 == season_tiers[current_season-2]:
                    draw_text(f'NEW LEVEL!', font27, self, 10, HEIGHT - 70, color=GOLD)
                elif season_tiers[current_season-2] > self.at_match_lvl:
                    draw_text(f'NEW LEVELS!', font28, self, 10, HEIGHT - 70, color=GOLD)
            
            if not self.player_died:
              
              for i, friend in enumerate(self.friends):
                if ranked: s = 55
                else: s = 0
                draw_text(friend.name, font17, self, 11 + s, 150 + i*75-20, color = (0,0,0))
                if (ranked) and (rp > 0):
                        col = rank_colors[friend.mrank]
                        draw_text(friend.name, font17, self, 9 + s, 150 + i*75-20, color = col)

                screen.blit(friend.original_image, (190 + s, 150 + i*75))
                if ranked: 
                    screen.blit(rank_imgs_scaled[friend.rank], (10, 150 + i*75))
                    draw_text(str(rank_names[friend.rank]), font10, self, 10, 150 + i*75 - 20, color = (0,0,0))
                
                if friend.health <= 0:
                    draw_text(str(int(friend.knocked_health)), font, self, 135 + s, 150 + i*75+30, color=(0,0,0))
                    draw_text(str(int(friend.revive_process)), font, self, 135 + s, 150 + i*75+0, color=(0,0,0))
                    draw_bar(self.screen, 10 + s, 150 + i*75+30, friend.knocked_health / 100, (255, 0, 0), size=1)
                    draw_bar(self.screen, 10 + s, 150 + i*75, friend.revive_process / 100, (0, 255, 0), size=1)
                else:
                    draw_text(str(int(friend.health)), font, self, 135 + s, 150 + i*75+30, color=(0,0,0))
                    draw_text(str(int(friend.shield)), font, self, 135 + s, 150 + i*75+0, color=(0,0,0))
                    draw_bar(self.screen, 10 + s, 150 + i*75+30, friend.health / friend.max_health, (0, 255, 0), size=1)
                    draw_bar(self.screen, 10 + s, 150 + i*75, friend.shield / friend.max_shield, (0, 255, 255), size=1)
                if self.mode == "Team Rumble":
                    if i >= 2:
                        break
              if ranked and (rp > 0):
                if self.player.on_vehicle == False:
                  draw_text(f'Your Rank: (RP: {rp})', font30, self, 10, 150 + (len(self.friends))*75 - 20, color = (0,0,0))
                  screen.blit(rank_imgs_scaled[get_rank(rp)], (10, 180 + (len(self.friends))*75))
                  draw_text(str(rank_names[get_rank(rp)]), font20, self, 10, 180 + (len(self.friends))*75 - 20, color = (0,0,0))


        
            
            if self.elimtim > 0:
                        self.elimtim -= 1
            if self.cremoved:
                global contr, contr_b
                contr = False
                self.contr = contr
                contr_b = Tick(50, 360, 'Controller in-Game: Off', font30)
                fgr = render(f"Controller Disconnected!", font, RED, BLACK)
                coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 + 70)
                screen.blit(fgr, coord)
                fgr = render(f"Please restart the game and re-connect.", font20, RED, BLACK)
                coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 + 100)
                screen.blit(fgr, coord)
                fgr = render(f"Since this is a bot royale, you shouldn't lose any significant progress.", font15, WHITE, BLACK, opx=1)
                coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 + 120)
                screen.blit(fgr, coord)

            else:
                if not self.player_died:
                    if self.player.ammo[BULLET_AMMO[self.player.weapon]] <= 0 and self.player.weapon > 0 and (self.player.weapon not in STACKABLES):
                        screen.blit(render(f"NO AMMO!", font, WHITE, BLACK), (WIDTH // 2 - 70, HEIGHT // 2 + 100,))
                        self.player.clips[self.player.inven_slot] = 0
                    
                    if self.elimtim > 0:
                            fgr = render(f"Eliminated {self.lem.name}", font, RED, BLACK)
                            coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 + 70)
                            screen.blit(fgr, coord)

                            fgr = render(f"Eliminated", font, WHITE, BLACK)
                            screen.blit(fgr, coord)

            # if self.ldtim > 0:
            #     self.ldtim -= 1
            #     fgr = render(f"2 Players Left!", font, GOLD, BLACK)
            #     coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 - 70)
            #     screen.blit(fgr, coord)

            if self.player.on_vehicle:
                        if self.player_died == False:
                            fgr = render(f"[{ca('T')}] to exit vehicle", font20, WHITE, BLACK)
                            coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 - 70)
                            screen.blit(fgr, coord)

            if self.player.gliding and (not self.on_bus):
                draw_bar(self.screen, WIDTH // 2 - 70, HEIGHT // 2 - 80, (self.player.glide_cd) / 500, (0, 155, 255), size=1.4)

            elif self.on_bus:
                if self.bus.cd == 0:
                    fgr = render(f"[{ca('SPACE')}] to Jump!", font, WHITE, BLACK)
                    coord = (WIDTH // 2 - fgr.get_width() / 2, HEIGHT // 2 - 80)
                    screen.blit(fgr, coord)

                    # draw_text(F"", font, self, WIDTH // 2 - 110, HEIGHT // 2 - 80, color=(0,0,0))

            if not self.splashed:
                if self.mptim > 0:
                    self.mptim -= 12
                    draw_text("New Location Discovered!", font, self, WIDTH // 2 - 210, HEIGHT // 2 - 240, color=(0,0,0))
                    if not contr: 
                        draw_text("Press [M] to see the Map.", font, self, WIDTH // 2 - 210, HEIGHT // 2 - 210, color=(0,0,0))

                if self.airdrop_text_timer > 0:
                    self.airdrop_text_timer -= 4
                    if self.player_died == False:
                        draw_text("The Storm is approaching!", font, self, WIDTH // 2 - 140, HEIGHT // 2 - 180, color=(0,0,0))
                        draw_text("An Airdrop has arrived!", font25, self, WIDTH // 2 - 140, HEIGHT // 2 - 150, color=(0,0,0))
                        draw_text("  (Shown with pink on the map)", font20, self, WIDTH // 2 - 140, HEIGHT // 2 - 120, color=(0,0,0))

            for i in self.friends:
                # if (i.health > 0):
                    ttv = render(f"{i.name}", font17, gfcolor=GREEN, ocolor=BLACK)
                    screen.blit(ttv, (self.camera.apply(i)[0] + 25 - (ttv.get_width() / 2), self.camera.apply(i)[1]-30))

            
            if len(self.mobs)+self.fake_player_count > 0:
                if self.phase_timer <= 0:
                    if not (self.mode in ["Team Rumble", "Shotgun Special"]):
                        ss = str(int(self.phase_cooldown/100))
                        if len(ss) == 1:
                            ss = "0" + ss
                        draw_text(f"Phase ends in 00:{ss}", fontseg, self, WIDTH - 675, 10, r=1)
                else:
                    ss = str(int(self.phase_timer/100))
                    if len(ss) == 1:
                        ss = "0" + ss
                    draw_text(f"Phase begins in 00:{ss}", fontseg, self, WIDTH - 675, 10, r=1)

                hn = len(self.friends)
                if self.mode == "Team Rumble":
                    if self.player_died == False: hn += 1
                    if not self.bus_time_over: 
                        screen.blit(render(f"Dropping Players...", fontseg, WHITE, BLACK), (WIDTH - 675, 10))
                        screen.blit(render(f"Eliminate the enemy team to win!", fontseg20, WHITE, BLACK), (WIDTH - 675, 40))
                    else:
                        draw_text(f"Your Team: 👤{hn}", fontseg, self, WIDTH - 675, 10, color=AQUA, r=1)
                        draw_text(f"Enemy Team: 👤{len(self.mobs)}", fontseg, self, WIDTH - 675, 40, color=RED, r=1)

                else:
                    # Players On Island: {self.players}
                    # if not self.bus_time_over: draw_text(f"Dropping Players...", font, self, WIDTH - 675, 40, color=(0,0,0))
                    # else: draw_text(f"Players: {self.players}", font, self, WIDTH - 675, 40, color=(0,0,0))
                    #👤
                    if not self.bus_time_over: screen.blit(render(f"Dropping Players...", fontseg, WHITE, BLACK), (WIDTH - 675, 40))
                    else: screen.blit(render(f"👤 {self.players} Left", fontseg, WHITE, BLACK), (WIDTH - 675, 40))


            if len(self.mobs)+self.fake_player_count > 0:
                if not self.player_died:
                    # draw_text(f"Eliminations: {self.elims}", font, self, WIDTH - 675, 70, r=1)
                    # if self.mode != "Solos": 
                    #     if self.mode != "Team Rumble":
                    #         draw_text(f"Squad Elims: {self.felims + self.elims}", font, self, WIDTH - 675, 100, r=1)
                    # draw_text(f"👤⚔️{self.elims} | 👥⚔️{self.felims + self.elims}", fontseg, self, WIDTH - 675, 70, r=1)
                    if self.mode in ["Solos", "Team Rumble"]:
                            qqq = "s"
                            if self.elims == 1:
                                qqq = ""
                            draw_text(f"⚔️ {self.elims} Elimination{qqq}", fontseg, self, WIDTH - 675, 70, r=1)
                    else:
                            draw_text(f"⚔️ {self.elims} | 👥⚔️ {self.felims + self.elims}", fontseg, self, WIDTH - 675, 70, r=1)


                            # draw_text(f"Squad Elims: {self.felims + self.elims}", font, self, WIDTH - 675, 100, r=1)


            # pygame.draw.rect(self.screen, WHITE, pygame.Rect(WIDTH-300 - 30, 20 - 10, 269, 290), 6)
            # pygame.draw.circle(self.screen, GREEN, (WIDTH-300 + self.player.pos.x // 128, 100 + self.player.pos.y // 128), 5)
            # for f in (self.friends): 
            #     pygame.draw.circle(self.screen, (0,0,255), (WIDTH-280 + f.pos.x // 128, 100 + f.pos.y // 128), 4)
            # for a in (self.airdrops): 
            #     pygame.draw.circle(self.screen, (255,0,255), (WIDTH-280 + a.pos.x // 128, 100 + a.pos.y // 128), 4)

            # ix, iy = WIDTH-300, 10
            # pygame.draw.rect(self.screen, WHITE, pygame.Rect(ix, iy, 148, 158), 6)
            # pygame.draw.circle(self.screen, GREEN, (ix + self.player.pos.x // 128 + 10, iy + 50 + self.player.pos.y // 128 + 10), 5)
            # for f in (self.friends): 
            #     gr = (0,0,255)
            #     if f.health <= 0:
            #         gr = (255,0,0)
            #     pygame.draw.circle(self.screen, gr, (ix + f.pos.x // 128 + 10, iy + 50 + f.pos.y // 128 + 10), 4)

            # for f in (self.mobs): 
            #     gr = (255,0,255)
            #     if f.health <= 0:
            #         gr = (255,255,0)
            #     pygame.draw.circle(self.screen, gr, (ix + f.pos.x // 128 + 10, iy + 50 + f.pos.y // 128 + 10), 4)

            # for a in (self.airdrops): 
            #     pygame.draw.circle(self.screen, (255,0,255), (ix + a.pos.x // 128 + 10, iy + 50 + a.pos.y // 128 + 10), 4)

            if self.chl_should_on:
                for j, i in enumerate(challenges):
                    if cc_complete[j]:
                        draw_text(f"COMPLETE! {challenge_acts[i]}", font, self, 10, 445 + (j*35), r=1)
                    else:
                        draw_text(f"{challenge_acts[i]} ({cc_tracker[i]}/{cc_goal[i]})", font, self, 10, 445 + (j*35), r=1)

            if pin_screen:
                if not self.player_died:
                    draw_text(f'[{ca("Z")}]', font20, self, WIDTH-220-30, 22, color=BLACK)
                    draw_text(f'[{ca("V")}]', font20, self, WIDTH-220-30, 90, color=BLACK)

                    for a, i in enumerate(emoticon_num):
                        ddf = Image(f"customize/emoticons/{i}.svg")
                        if a != self.player.emoji_index:
                            ddf.set_alpha(60)
                        else:
                            draw_text(f'[{ca("X")}]', font20, self, WIDTH-250 + a*65 + 57,56, color=BLACK)
                        screen.blit(ddf, (WIDTH-250 + a*65,10))
                    
                    for a, i in enumerate(spray_num):
                            ddf = Scale(Image(f"customize/sprays/{i}.svg"), 0.5)

                            
                            if a != self.player.spray_index:
                                if i == 0:
                                    ddf.set_alpha(30)
                                else:
                                    ddf.set_alpha(60)
                            else:
                                if i != 0: draw_text(f'[{ca("C")}]', font20, self, WIDTH-250 + a*65 + 32,120, color=BLACK)

                            screen.blit(ddf, (WIDTH-220 + a*65,80))

            # else:
                
            #     if float("{:.2f}".format(self.clock.get_fps())) > self.fps_tac[1]:
            #         self.fps_tac[1] = round(float("{:.2f}".format(self.clock.get_fps())), 2)
                
            #     if float("{:.2f}".format(self.clock.get_fps())) < self.fps_tac[0]:
            #       if float("{:.2f}".format(self.clock.get_fps())) != 0:
            #         self.fps_tac[0] = round(float("{:.2f}".format(self.clock.get_fps())), 2)

            #     draw_text("FPS: " + "{:.2f}".format(self.clock.get_fps()), font, self, 10, 500, color=(0,255,0))
            #     draw_text(f"v {self.fps_tac[0]} ^ {self.fps_tac[1]}", font25, self, 10, 535, color=(0,255,0))

        # draw_text(f"{self.bus.perfdrop} // {self.bus_time}", font, self, 10, 550, color=(0,255,0))
        # draw_text(f"lenmobs: {len(self.mobs)}, fakemob: {self.fake_player_count}, friends: {len(self.friends)}", font, self, 10, 600, color=(0,255,0))

        if self.players > 100:
            self.fake_player_count /= 2

        if len(self.mobs) == 0:
            self.fake_player_count = 0
        if len(self.mobs)+self.fake_player_count <= 0:
            if self.bus_time_over:
                if ranked: 
                    if rp >= 0: 
                      if rp_formula(self.elims, self.player_at_count) >= 0:
                        draw_text(f'Earned {rp_formula(self.elims, self.player_at_count)} RP!', font35, self, WIDTH // 2 - 170, HEIGHT // 2 - 260, color=RED)
                      else:
                          draw_text(f'Lost {abs(rp_formula(self.elims, self.player_at_count))} RP!', font35, self, WIDTH // 2 - 170, HEIGHT // 2 - 260, color=RED)
                    else: draw_text(f'Your NEW Rank: {rank_names[get_rank(rp)]}!')
                
                bdd = 0
                if (self.player_died):
                    if len(self.friends) <= 0:
                        bdd = 1

                if bdd == 0:
                    draw_text('VICTORY!', font60, self, WIDTH // 2 - 70, HEIGHT // 2 - 180, color=GOLD, r=1)

                    self.splashed = True

                    draw_text('Congratulations!', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 120, color=GOLD, r=1)
                    draw_text(F'[{ca("SPACE2")}] to leave', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 220, color=GOLD, r=1)

                # global menu_state
                # if self.player_died:
                #     self.quit_match()
                
                if not self.player_died:
                    if len(self.mobs) > 0:
                            self.mobs.empty()

                global friend_list
                i=0
                if self.fry_should_on:
                    if len(friend_list) < 100:
                        for k in self.friend_kb:
                            self.screen.blit(Image(f"customize/skins/{k.glide2}.svg"), (10, 400 + i*60))
                            if k.draw():
                                if k.glide != 0:
                                    if k.glide not in friend_list: friend_list.append(k.glide)
                                    self.friend_kb[i] = Tick(65, 400 + i*60, f'Already friended {k.glide}!', font30, glide2=k.glide2)
                            i+=1
                        if len(self.friend_kb) > 0:
                            draw_text(f'Press [{ca("U")}] to hide/show this.', font15, self, 10, 400 + i*60, color=(0,0,0))
                    else:
                        draw_text('You have too many friends! (The cap is 100.)', font, self, 10, 400, color=(0,0,0))
                        draw_text(f'Press [{ca("U")}] to hide/show this.', font15, self, 10, 435, color=(0,0,0))

        else:
            if self.player_died:
                if len(self.mobs) <= 1 and len(self.friends) == 0:
                    if ranked: 
                        if rp >= 0: 
                            if rp_formula(self.elims, self.player_at_count) >= 0:
                                draw_text(f'Earned {rp_formula(self.elims, self.player_at_count)} RP!', font35, self, WIDTH // 2 - 170, HEIGHT // 2 - 260, color=RED)
                            else:
                                draw_text(f'Lost {abs(rp_formula(self.elims, self.player_at_count))} RP!', font35, self, WIDTH // 2 - 170, HEIGHT // 2 - 260, color=RED)
                        else: draw_text(f'Your NEW Rank: {rank_names[get_rank(rp)]}! Progress to next rank: {(rp_formula(self.elims, self.player_at_count) / rank_targs[get_rank(rp)]) * 100}%')
                    # draw_text('VICTORY!', font60, self, WIDTH // 2 - 70, HEIGHT // 2 - 180, color=GOLD, r=1)
                    self.splashed = True
                    # draw_text('Congratulations!', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 120, color=GOLD, r=1)
                    # draw_text(F'[{ca("SPACE2")}] to leave', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 220, color=GOLD, r=1)

                    draw_text(F'[{ca("SPACE2")}] to leave', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 220, color=RED, r=1)
                    if self.mode != "Team Rumble":
                        draw_text(f'You placed #{self.player_at_count}.', font60, self, WIDTH // 2 - 170, HEIGHT // 2 - 160, color=RED, r=1)
                        draw_text(f'The player you are spectating has won.', font20, self, WIDTH // 2 - 170, HEIGHT // 2 - 100, color=RED, r=1)
                    else:
                        draw_text(f'You have died.', font60, self, WIDTH // 2 - 170, HEIGHT // 2 - 160, color=RED, r=1)
                        draw_text(f'The other team has won.', font30, self, WIDTH // 2 - 170, HEIGHT // 2 - 100, color=RED, r=1)

                    
                    # if self.player_died:
                    #     self.quit_match()
                    if not self.player_died:
                        if len(self.mobs) > 0:
                            self.mobs.empty()

                    i=0
                    if self.fry_should_on:
                        if len(friend_list) < 100:
                            for k in self.friend_kb:
                                self.screen.blit(Image(f"customize/skins/{k.glide2}.svg"), (10, 400 + i*60))
                                if k.draw():
                                    if k.glide != 0:
                                        if k.glide not in friend_list: friend_list.append(k.glide)
                                        self.friend_kb[i] = Tick(65, 400 + i*60, f'Already friended {k.glide}!', font30, glide2=k.glide2)
                                i+=1
                            draw_text(f'Press [{ca("U")}] to hide/show this.', font15, self, 10, 400 + i*60, color=(0,0,0))
                        else:
                            draw_text(f'Press [{ca("U")}] to hide/show this.', font15, self, 10, 435, color=(0,0,0))
                            draw_text('You have too many friends! (The cap is 100.)', font, self, 10, 400)
                            

                else:
                    if ranked: 
                        if rp >= 0: 
                            if rp_formula(self.elims, self.player_at_count) >= 0:
                                draw_text(f'Earned {rp_formula(self.elims, self.player_at_count)} RP!', font35, self, WIDTH // 2 - 170, HEIGHT // 2 - 260, color=RED, r=1)
                            else:
                                draw_text(f'Lost {abs(rp_formula(self.elims, self.player_at_count))} RP!', font35, self, WIDTH // 2 - 170, HEIGHT // 2 - 260, color=RED, r=1)
                        # else: draw_text(f'Your NEW Rank: {rank_names[get_rank(rp)]}! Progress to next rank: {(rp_formula(self.elims, self.player_at_count) / rank_targs[get_rank(rp)]) * 100}%')

                    if self.mode != "Team Rumble":
                        draw_text(f'You placed #{self.player_at_count}.', font60, self, WIDTH // 2 - 170, HEIGHT // 2 - 160, color=RED, r=1)
                    else:
                        draw_text(f'You have died.', font60, self, WIDTH // 2 - 170, HEIGHT // 2 - 160, color=RED, r=1)
                        if len(self.friends) == 0:
                            self.quit_match()
                            global af
                            if self.player_died:
                                af = True

                    if ranked:
                        if rp <= 0:
                            rp = get_init_rp(self.elims, self.player_at_count)
                            self.rp = get_init_rp(self.elims, self.player_at_count)

                    if self.deathcd == self.maxdeathcd:
                        draw_text('Spectating', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 100, color=RED, r=1)
                        draw_text(F'[{ca("SPACE2")}] to leave', font, self, WIDTH // 2 - 70, HEIGHT // 2 - 200, color=RED, r=1)
                        self.splashed = True
                        ulti = False

                        if self.swispe.draw():
                            ulti = True

                        for joystick in self.joysticks:
                            if thrust(joystick, 2):
                                ulti = True

                        if ulti:
                            if len(self.friends) >= 2:
                                q = random.choice(list(self.friends))
                                while q==self.player:
                                    q = random.choice(list(self.friends))
                                self.camera_focus_on = q
                                self.player = q
                            elif (len(self.friends) == 0) and (len(self.mobs) >= 2):
                                q = random.choice(list(self.mobs))
                                while q==self.player:
                                    q = random.choice(list(self.mobs))
                                self.camera_focus_on = q
                                self.player = q

                        i=0

                        if self.fry_should_on:
                            if len(friend_list) < 100:
                                for k in self.friend_kb:
                                    self.screen.blit(Image(f"customize/skins/{k.glide2}.svg"), (10, 400 + i*60))
                                    if k.draw():
                                        if k.glide != 0:
                                            if k.glide not in friend_list: 
                                                friend_list.append(k.glide)
                                            self.friend_kb[i] = Tick(65, 400 + i*60, f'Already friended {k.glide}!', font30, glide2=k.glide2)
                                    i+=1
                                draw_text(f'Press [{ca("U")}] to hide/show this.', font15, self, 10, 400 + i*60, color=(0,0,0))
                            else:
                                draw_text(f'Press [{ca("U")}] to hide/show this.', font15, self, 10, 435, color=(0,0,0))
                                draw_text('You have too many friends! (The cap is 100.)', font, self, 10, 400, color=(0,0,0))

            else:
                for boss in self.bosses:
                  if boss.alive():
                    if 0 < (self.player.pos - boss.pos).length() < 700:
                        r = render(f'BOSS', font30, RED, BLACK)
                        screen.blit(r, (WIDTH / 2 - r.get_width() / 2, 100))
                        r = render(f'{boss.name} HP', font20, RED, BLACK)
                        screen.blit(r, (WIDTH / 2 - r.get_width() / 2, 170))
                        draw_bar(self.screen, WIDTH / 2 - 100, 150, boss.health / boss.max_health, (255, 0, 0), w=200, h=16)


                    
                    




        if not self.player_died:
            if self.player.weapon > 0:
                if (self.player.weapon not in STACKABLES):
                    if self.player.reload_time == 0 and GUN_CLIP[self.player.weapon] != math.inf:
                        screen.blit(render(f"{GUN_CLIP[self.player.weapon] - self.player.clips[self.player.inven_slot]}|{GUN_CLIP[self.player.weapon]}", font50, WHITE, BLACK), (WIDTH - 535, HEIGHT - 150))
                    elif GUN_CLIP[self.player.weapon] != math.inf:
                        screen.blit(render(f"{int(int(self.player.reload_time) * 100 / self.player.reload_rate)}%", font50, WHITE, BLACK), (WIDTH - 535, HEIGHT - 150))
                else:
                    screen.blit(render(f"   {self.player.stack_count[self.player.inven_slot]}", font50, WHITE, BLACK), (WIDTH - 537, HEIGHT - 150,))

                lrewl = len(WEAPON_NAMES[self.player.weapon]) 
                if lrewl > 14:
                    ll = len(WEAPON_NAMES[self.player.weapon]) - 14
                    ff = pygame.font.SysFont("bahnschrift", 27 - ll)
                else:
                    ff = font27
                screen.blit(render(f"{WEAPON_NAMES[self.player.weapon]}", ff, WHITE, BLACK), (WIDTH - 400, HEIGHT - 70,))
            

            k = 0
            for i in self.player.rarity:
                self.screen.blit(self.img_rarities[i], (WIDTH - 400 + k * 75, HEIGHT - 150))

                

                self.screen.blit(self.img_weapons[self.player.inventory[k]], (WIDTH - 400 + k * 75, HEIGHT - 150))
                if self.player.inventory[k] > 0:
                    if self.player.inventory[k] in STACKABLES:
                        screen.blit(render(f"{self.player.stack_count[k]}", font, WHITE, BLACK), (WIDTH - 400 -4 + k * 75 + 5, HEIGHT - 150))
                    elif BULLET_AMMO[self.player.inventory[k]] == 4:
                        if pygame.time.get_ticks() - self.player.last_shot > BULLET_RATE[self.player.inventory[k]]: word = "Ready!"
                        else: 
                            s = pygame.Surface((69-(69 * (pygame.time.get_ticks() - self.player.last_shot) / BULLET_RATE[self.player.inventory[k]]), 69), pygame.SRCALPHA)   # per-pixel alpha
                            s.fill((0,0,0,150))                         # notice the alpha value in the color
                            screen.blit(s, (int(WIDTH - 400 + k * 75), int(HEIGHT - 150)))
                            word = "Charging"  
                        screen.blit(render(f"{word}", font15, WHITE, BLACK), (WIDTH - 400 -4 + k * 75 + 5, HEIGHT - 150))
                    else:
                        screen.blit(render(f"{self.player.ammo[BULLET_AMMO[self.player.inventory[k]]]}", font, WHITE, BLACK), (WIDTH - 400 -4 + k * 75 + 5, HEIGHT - 150))
                
                if self.player.inven_slot == k:
                    pygame.draw.rect(self.screen, WHITE, pygame.Rect(WIDTH - 400 + k * 75 - 4, HEIGHT - 150 - 4, 69 + 4, 69+4), 4)
                    
                k += 1

        if not self.player_died:
            if self.player.consuming:
                draw_bar(self.screen, WIDTH // 2 - 70, HEIGHT // 2 - 80, (BULLET_RATE[self.player.weapon] - self.player.cons_cool) / BULLET_RATE[self.player.weapon], (0, 0, 255), size=1.4)
        elif self.player.reviving_someone != None:
            draw_bar(self.screen, WIDTH // 2 - 70, HEIGHT // 2 - 80, self.player.reviving_someone.revive_process / 100, (0, 255, 0), size=1.4)

        if self.map_should_on:
            screen.blit(self.map_img, (190, 98))
            # for i in self.map_imgs:
            #     screen.blit(i, (190, 98))

            # if self.on_bus: screen.blit(self.bus_rt_img, (190, 98))

            if self.player.weapon != 0:
                w = self.map_img.get_width()
                s = pygame.Surface((WIDTH-(190+w), self.map_img.get_height()), pygame.SRCALPHA)   # per-pixel alpha
                s.fill((0,0,0,180))                         # notice the alpha value in the color
                screen.blit(s, (190+w, 98)) 

                lrewl = len(WEAPON_NAMES[self.player.weapon]) 
                if lrewl > 14:
                    ll = len(WEAPON_NAMES[self.player.weapon]) - 14
                    ff = pygame.font.SysFont("bahnschrift", 23 - ll)
                else:
                    ff = font27

                draw_text(WEAPON_NAMES[self.player.weapon], ff, self, 190+w+10, 102)
                draw_text(MRARITY_NAMES[self.player.rarity[self.player.inven_slot]], font18, self, 190+w+10, 130)

                rarity_for_code = self.player.rarity[self.player.inven_slot]

                if not (self.player.weapon in STACKABLES):
                    ef = 1
                    if BULLET_AMMO[self.player.weapon] == 3:
                        ef = 5


                    asfs = ef * round(BULLET_DAMAGE[self.player.weapon] * RARITY_MULTIPLIERS[rarity_for_code], 1)
                                      

                    draw_text(f"Damage: {asfs}", font18, self, 190+w+10, 175)
                    draw_text(f"Rate: {BULLET_RATE[self.player.weapon] // 10}", font18, self, 190+w+10, 200)

                    if math.isinf(BULLET_LIFETIME[self.player.weapon]):
                        draw_text(f"Lifetime: Infinite", font18, self, 190+w+10, 225)
                    else:
                        draw_text(f"Lifetime: {BULLET_LIFETIME[self.player.weapon] // 5}", font18, self, 190+w+10, 225)
                    
                    if math.isinf(GUN_CLIP[self.player.weapon]):
                        draw_text(f"Infinite Magazine Size!", font18, self, 190+w+10, 250)
                    else:
                        draw_text(f"Magazine Size: {GUN_CLIP[self.player.weapon]}", font18, self, 190+w+10, 250)
                    draw_text(f"Ammo: {AMMO_NAMES[BULLET_AMMO[self.player.weapon]]}", font18, self, 190+w+10, 275)
                    draw_text(f"Spread: {GUN_SPREAD[self.player.weapon] // 2}°", font18, self, 190+w+10, 300)
                    draw_text(f"Reload: {RELOAD_NAMES[WEAPON_RELOADS[self.player.weapon] // 50]}", font18, self, 190+w+10, 325)

            w=[]    
            dv = {}
            for i in self.storm:
                dv[i.dir] = i
            
            for i in self.storm:
                if i.dir == "left": 
                    r = pygame.Rect(dmiw+190-(i.rect.width / 64 * (dmiw/269)), 98, i.rect.width / 64 * (dmiw/269), dmih)
                    r.normalize()
                    pygame.draw.rect(screen, (203, 195, 227), r)
                if i.dir == "right":
                    r = pygame.Rect(190, 98, i.rect.width / 64 * (dmiw/269), dmih)
                    r.normalize()
                    pygame.draw.rect(screen, (203, 195, 227), r)
                if i.dir == "up":
                    r = pygame.Rect(190, 98+dmih-i.rect.height / 64 * (dmih/290), dmiw, i.rect.height / 64 * (dmih/290))
                    r.normalize()
                    pygame.draw.rect(screen, (203, 195, 227), r)
                if i.dir == "down":
                    r = pygame.Rect(190, 98, dmiw, i.rect.height / 64 * (dmih/290))
                    r.normalize()
                    pygame.draw.rect(screen, (203, 195, 227), r)

            pygame.draw.circle(screen, (0,255,0), (self.player.pos.x / 64 * (dmiw/269) + 190, (self.player.pos.y / 64 + 110) * (dmih/290) + 98 - 20), 6)
            coord = f'YOU: ({self.player.pos.x // 64}m, {self.player.pos.y // 64}m) '
            for i in (self.friends):
                gr = (0,0,255)
                if i.health <= 0:
                    gr = (255,0,0)
                pygame.draw.circle(screen, gr, (i.pos.x / 64 * (dmiw/269) + 190, (i.pos.y / 64 + 110) * (dmih/290) + 98 - 20), 4)
                coord += f'{i.name}: ({i.pos.x // 64}m, {i.pos.y // 64}m) '

            # for i in (self.mobs):
            #     if not (i in self.in_range):
            #         gr = (255,150,255)
            #     else:
            #         gr = (255,0,255)
            #     if i.health <= 0:
            #         gr = (255,255,0)
            #     pygame.draw.circle(screen, gr, (i.pos.x / 64 * (dmiw/269) + 190, (i.pos.y / 64 + 110) * (dmih/290) + 98 - 20), 4)

            for i in (self.airdrops):
                pygame.draw.circle(screen, (255,0,255), (i.pos.x / 64 * (dmiw/269) + 190, (i.pos.y / 64 + 110) * (dmih/290) + 98 - 20), 4)
            draw_text(coord, font18, self, 10, HEIGHT - 80, color=(0,0,0))
            draw_text(coord, font18, self, 8, HEIGHT - 78)
    
            draw_text(f"AMMO: {self.player.ammo[0]} Light, {self.player.ammo[1]} Medium, {self.player.ammo[2]} Heavy, {self.player.ammo[3]} Shells.", font18, self, 10, HEIGHT - 50, color=(0,0,0))
            draw_text(f"AMMO: {self.player.ammo[0]} Light, {self.player.ammo[1]} Medium, {self.player.ammo[2]} Heavy, {self.player.ammo[3]} Shells.", font18, self, 8,  HEIGHT - 48)

        else:
            if not self.player_died:
                if not (self.player.weapon in [*STACKABLES, *[0]]):
                    p = pygame.mouse.get_pos()
                    screen.blit(reticle_img, (p[0]-12,p[1]-13))

        if self.playing == False:
            for k in self.all_sprites:
                k.kill()
            for k in self.storm:
                k.kill()

        if self.paused:
                self.s.fill((0,0,0))                         # notice the alpha value in the color
                screen.blit(self.s, (0, 0)) 
                draw_text("Game Paused", font100, 0, 100, 100)
                draw_text(f"Press [{ca('P')}] to unpause.", font30, 0, 100, 200)
                if self.pauses > 0:
                    cop = "Use them wisely!"
                else:
                    cop = "No pauses left!"
                draw_text(f"You have used {3-self.pauses}/3 pauses. {cop}", font30, 0, 100, 250)


        pygame.display.flip()

    def events(self):
        # catch all events here
        self.pressing_e = False
        self.count_e = False
        
        global menu_state

        if self.contr:
          if not self.paused:
            self.pressing_m = False
            self.pressing_q = False
            self.pressing_u = False

            for joystick in self.joysticks:
                if thrust(joystick, 2):
                        self.hopoff[0] = True
                else:
                    if self.hopoff[0]:
                        self.hopoff[0] = False
                        if self.player.health > 0:
                            if not self.count_e: 
                                self.pressing_e = True; self.count_e = True
                        else:
                            self.count_e = False

                if thrust(joystick, 7):
                        self.hopoff[1] = True
                else:
                    if self.hopoff[1]:
                        self.hopoff[1] = False
                        if not self.pressing_m:
                            self.map_should_on = not self.map_should_on
                        self.pressing_m = True

                if thrust(joystick, 6):
                        self.hopoff[2] = True
                else:
                    if self.hopoff[2]:
                        self.hopoff[2] = False
                        if not self.pressing_u:
                            self.fry_should_on = not self.fry_should_on
                        self.pressing_u = True

                if thrust(joystick, 8):
                        self.hopoff[3] = True
                else:
                    if self.hopoff[3]:
                        self.hopoff[3] = False
                        if not self.pressing_q:
                            self.chl_should_on = not self.chl_should_on
                        self.pressing_q = True

                
                if thrust(joystick, 1):
                        self.hopoff[4] = True
                else:
                    if self.hopoff[4]:
                        self.hopoff[4] = False
                        if self.deathcd == self.maxdeathcd:
                                if (self.bus_time_over and len(self.mobs)+self.fake_player_count <= 0) or (self.player_died):
                                    self.quit_match()

                if thrust(joystick, 9):
                        self.hopoff[5] = True
                else:
                    if self.hopoff[5]:
                        self.hopoff[5] = False
                        self.paused = not self.paused


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            

                if event.type == pygame.JOYDEVICEREMOVED:
                        self.cremoved = True


            
            
                if event.type == pygame.FULLSCREEN:
                    fullscreen = not fullscreen
                    if fullscreen: global screen; screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, 16); self.screen = screen
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    
                    

                    if not self.contr:
                        if event.key == pygame.K_p:
                            if not self.paused:
                                if self.pauses > 0:
                                    self.paused = True
                                    self.pauses -= 1
                            else:
                                self.paused = False
                        
                        if not self.paused:
                            if event.key == pygame.K_m:
                                if not self.pressing_m:
                                    self.map_should_on = not self.map_should_on
                                self.pressing_m = True

                            if event.key == pygame.K_u:
                                if not self.pressing_u:
                                    self.fry_should_on = not self.fry_should_on
                                self.pressing_u = True
                        
                            if event.key == pygame.K_q:
                                if not self.pressing_q:
                                    self.chl_should_on = not self.chl_should_on
                                self.pressing_q = True

                            if event.key == pygame.K_e:

                                    if self.player.health > 0:
                                        if not self.count_e: 
                                            self.pressing_e = True; self.count_e = True
                                    else:
                                        self.count_e = False
                        
                            if event.key == pygame.K_SPACE:
                                if self.deathcd == self.maxdeathcd:
                                    if (self.bus_time_over and len(self.mobs)+self.fake_player_count <= 0) or (self.player_died):
                                        self.quit_match()

                    if event.key == pygame.K_BACKSLASH:
                            self.quit_match(will=True)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_m:
                        self.pressing_m = False

                    if event.key == pygame.K_u:
                        self.pressing_u = False

                    if event.key == pygame.K_q:
                        self.pressing_q = False


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def quit_match(self, will=False):
        global menu_state
        self.playing = False
        pygame.mouse.set_visible(True)
        menu_state = "main"
        pygame.mixer.music.stop()
        global cf
        if not (self.bus_time_over):
            if ((self.players == 1 and self.player_died) or len(self.mobs) == 1):
                if self.player_at_count <= 2:
                    cf = True
        if not will:
          if ranked:
            global rp
            if rp > 0:
                rp += rp_formula(self.elims, self.player_at_count)
            else:
                rp = get_init_rp(self.elims, self.player_at_count)

            global mrp
            if rp > mrp:    
                if rp >= rank_targs[get_rank(mrp)]:
                    global prems
                mrp = rp

            if rp < 0:
                rp = 0
        else:
            if ranked:
                if rp <= 0:
                    rp = get_init_rp(self.elims, 95)
                if rp > 0:
                    if self.player_died:
                        rp += rp_formula(self.elims, self.player_at_count)
                    else:
                        ffare = BUS_FARE[get_rank(rp)]
                        if (rp - ffare) < rank_targs[get_rank(rp)-1]:
                            ffare = 0
                        rp -= ffare

cf = False
af = False


# create the game object
g = Game()
g.show_start_screen()

def rp_formula(elims, placement):
    fare = BUS_FARE[get_rank(rp)]
    if (math.ceil(1.38 * (100-placement)+(15*elims)) - fare) < 0:
        if (rp + math.ceil(1.38 * (100-placement)+(15*elims)) - fare) < rank_targs[get_rank(rp)-1]:
            fare = 0
    return math.ceil(1.38 * (100-placement)+(15*elims)) - fare

def get_init_rp(e, p):
    df = math.ceil((11 * (100-p) + 15*e) * 1.5)
    if df == 0:
        df = 5
    return df



logo = Button(WIDTH // 2 - 450, 10, Image('menu/logo.png'), 1)

play_b = Button(WIDTH - 250, HEIGHT - 200, Image('menu/button1.svg'), 1.3)

fill0 = True

rot_b = Tick(WIDTH - 227, HEIGHT - 250, 'Change Mode', font30)
fill_b = Tick(WIDTH - 160, HEIGHT - 104, 'Fill', font30)

signup_b = Tick(WIDTH - 270, 150, 'Signup', font30)
login_b = Tick(WIDTH - 150, 150, 'Login', font30)

exit_b = Tick(WIDTH - 150, HEIGHT - 100, 'Exit', font50)
okay_b = Tick(WIDTH - 160, HEIGHT - 100, 'Okay!', font50)

yes_b = Tick(WIDTH - 150, HEIGHT - 100, 'Yes', font50)
no_b = Tick(WIDTH - 300, HEIGHT - 100, 'No', font50)

prev_b = Tick(WIDTH - 300, HEIGHT - 100, 'Last', font50)
next_b = Tick(WIDTH - 150, HEIGHT - 100, 'Next', font50)

bpexit_b = Tick(WIDTH - 150, HEIGHT - 50, 'Exit', font40)

settings_b = Tick(10, 150, 'Settings', font40)
friend_b = Tick(10, 210, 'Friends', font40)
custom_b = Tick(10, 270, 'Customize', font40)
is_b = Tick(10, 330, 'Item Shop', font40)
bp_b = Tick(10, 390, 'Battle Pass', font40)
cc_b = Tick(10, 450, 'Challenges', font40)

chindex = 0 

rl_b = Tick(WIDTH - 475, 150, 'Set Random', font30)
uf_b = Tick(WIDTH - 270, 150, 'Go Up', font30)
df_b = Tick(WIDTH - 150, 150, 'Go Down', font30)

rxl_b = Tick(WIDTH - 475, 150, 'Random', font30)
rxl2_b = Tick(WIDTH - 275, 150, 'Random', font30)

clock = pygame.time.Clock()

lf_b = Tick(WIDTH - 450, HEIGHT - 50, 'Go Left', font30)
rf_b = Tick(WIDTH - 310, HEIGHT - 50, 'Go Right', font30)

buy_bp = Tick(333, 150, 'Buy Battle Pass', font40)
buy_lvl = Tick(333, 210, 'Buy Level (20 PREMS)', font35)

ltm_intros = {
    "Solos": ["Go it alone and be the last one standing.",],
    "Duos": ["Pair up and fight to be the best!",],
    "Squads": ["Play with three other teammates to get the win.",],
    "Team Rumble": ["Two teams battle it out to eliminate the other team first!",],

    "Marvel Mayhem": [
        "Every weapon is a Marvel Weapon! Embrace the Mayhem!",
        "Only a maximum of 50 Health and 50 Shield!",
        "Be the last one standing! (Squads)",
    ], 
    "Solid Gold": [
        "Every weapon is legendary in this mode!",
        "Be the last one standing! (Squads)",
        "",
    ],  
    "Shotgun Special": [
        "Every weapon is a shotgun in this mode!",
        "Be the last one standing! (Squads)",
        "",
    ], 
}

#mode change
LTMs = ["Marvel Mayhem", "Solid Gold", "Shotgun Special"]
LTM = random.choice(LTMs)
all_modes = ["Solos", "Duos", "Squads", "Team Rumble", LTM]
len_all_modes = [1, 2, 4, 50, 4, 4, 4]

mode_bs = []
i = 0
for m in all_modes:
    mode_bs.append(Tick(50, 60 * i + 200, f'{m}', font40, glide=m))
    i += 1

contr = 0

types_of_customization = ["Skin", "Backpack", "Glider", "Emoticon", "Spray", "Loading Screen", "Contrail", "Music Pack"]

ism = Tick(400, 150, f'View Mode', font30)

rank_imgs = []
for i in range(len(rank_names)):
    rank_imgs.append(Image(f"HUD/ranks/{i}.svg"))
    
rank_imgs_scaled = []
for i in range(len(rank_names)):
    rank_imgs_scaled.append(Scale(Image(f"HUD/ranks/{i}.svg"), 0.5))

rpb = Tick(WIDTH - 300, 200, f'Champions: Off', font40)
irpb = Tick(WIDTH - 300, 260, f'Info about Champions', font25)


custom_types_b = []
i = 0
for m in types_of_customization:
    custom_types_b.append(Tick(50, 50 * i + 200, f'Change {m}', font30, glide=m))
    i += 1

# lvl_imgs = []
# for i in range(70):
#     lvl_imgs.append(Image(f'HUD/bp/{i+1}.png'))
    # lvl_imgs.append(Image('ess/bus.png'))

# bpx = 0
# lvl_display = []
# for i in range(70):
#     lvl_display.append(Button(200*i + bpx, 270, lvl_imgs[i], 1, glide=i))

prevls = 0

#text inputs for login
user_type = TrashInput('', ("data/tzt.ttf", 22), ('white'), 10, 10, 100)
newUserName = None

pass_type = TrashInput('', ("data/tzt.ttf", 22), ('white'), 10, 10, 100)
newPassWord = None



trypass_type = TrashInput('', ("data/tzt.ttf", 22), ('white'), 10, 10, 100)
tryUserName = None

tryuser_type = TrashInput('', ("data/tzt.ttf", 22), ('white'), 10, 10, 100)
tryPassWord = None

confirm_b = Tick(WIDTH - 240, HEIGHT - 100, 'Confirm', font50)

purchase_b = Tick(460, HEIGHT - 100, 'Purchase!', font50)

cpass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
pppppp = None

cuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
cccccc = None

lobby = [f'{username} (YOU)']
lobby_kick = []

friendy = 0
customy = 0

hist = False
hist_b = Tick(550, 150, 'Sort by Rarity', font30)

rev = False
rev_b = Tick(550, 200, 'Reverse', font30)

locked_in = False

glider_num = 0
backpack_num = 0
emoticon_num = [0, 0, 0]
trail_num = 0
music_num = 0
spray_num = [0, 0, 0]
ls_num = 0

dskin = Scale(Image(f'customize/skins/{skin_num}.svg'), 2)
dbling = Scale(Image(f'customize/backpacks/{backpack_num}.svg'), 2)

got_new_level = False

reroll_is()

old_level = season_tiers[current_season-2]
old_rank = get_rank(rp)
if not replit:
    pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
    pygame.mixer.music.play(-1)

while 1:
    g.phase_cooldown = 6000
    if menu_state == "game":
        screen.fill((0, 0, 0))
        sc = Button(0, 0, Image(f'customize/ls/{ls_num}.png'), 1.47)
        sc.draw()

        # if g.mode in LTMs:
        s = pygame.Surface((WIDTH, 100), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0,0,0,180))                         # notice the alpha value in the color
        screen.blit(s, (0, 0))

        # draw_text(ltm_intros[g.mode][0], font25, 0, 18, 10, color=BLACK)
        # draw_text(ltm_intros[g.mode][1], font25, 0, 18, 40, color=BLACK)
        # draw_text(ltm_intros[g.mode][2], font25, 0, 18, 70, color=BLACK)

        for i in range(len(ltm_intros[g.mode])):
            screen.blit(render(ltm_intros[g.mode][i], font25, WHITE, BLACK), (20, 10+i*30))

        # draw_text( 0, 20, 10)
        # draw_text(ltm_intros[g.mode][1], font25, 0, )
        # draw_text(ltm_intros[g.mode][2], font25, 0, 20, 70)

        pygame.display.update()

        
        g.new()

        if not replit: pygame.mixer.music.stop()
        

        pygame.mixer.music.load(f"data/sfx/interact/amb.wav")
        pygame.mixer.music.play(-1)

        Audio("interact/hh.wav")

        if rlr:
            ls_num = random.choice(have_ls)

        g.run()
        g.show_go_screen()

    elif menu_state == "new lvls":
        screen.fill((0, 71, 171))
        
        draw_text('New Levels!', font50, 0, 50, 150, color=BLACK)
        draw_text(f'Season {current_season}', font40, 0, 50, 200, color=BLACK)
        draw_text(f'Level {season_tiers[current_season-2]}', font30, 0, 50, 240, color=BLACK)

        if old_level >= 70:
            draw_text(f'Gained +{25 * (season_tiers[current_season-2]-old_level)} Prems!', font30, 0, 450, 240, color=BLACK)

        il = pygame.mouse.get_pos()
        for i, b in enumerate(nbpv):
            h = nbpr[i]
            j = h.copy()
            j.x += bptx

            if mainbp == b:
                if not j.collidepoint(il):
                    co = "#FF7C1C"
                else:
                    co = "#F9BD92"
            elif (season_tiers[current_season-2] >= b.glide) and battle_passes[current_season-2]:
                if not j.collidepoint(il):
                    co = "#707070"
                else:
                    co = "#C0C2C4"

            elif not lvl_grants[b.glide][2]:
                if (season_tiers[current_season-2] >= b.glide):
                    if not j.collidepoint(il):
                        co = "#707070"
                    else:
                        co = "#C0C2C4"
                else:
                    if not j.collidepoint(il):
                        co = "#72FB79"
                    else:
                        co = "#D0FCD4"

            else:
                if not j.collidepoint(il):
                    co = "#0E97FF"
                else:
                    co = "#7BC2FB"
                
            
            pygame.draw.rect(screen, co, j)
            pygame.draw.rect(screen, (220,220,220), j, 5)

            b.draw()
            draw_text(f'{b.glide}', font30, 0, j.x+35, j.y-32, color=BLACK)
         

        if bpexit_b.draw():
            menu_state = "main"
        

    elif menu_state == "main":
        screen.fill((0, 71, 171))

        if got_bp_rewards == False:
                if old_level < season_tiers[current_season-2]:
                    got_bp_rewards = True
                    nlvld = []

                    bptx = 0
                    mbp(old_level, season_tiers[current_season-2], False)


                    menu_state = "new lvls"


        dskin = Scale(Image(f'customize/skins/{skin_num}.svg'), 2)
        dbling = Scale(Image(f'customize/backpacks/{backpack_num}.svg'), 2)

        

        got_new_level = False

        # pygame.mouse.set_visible(True)

        if not replit:
            if pygame.mixer.music.get_busy() == False:
                
                pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
                pygame.mixer.music.play(-1)

        screen.blit(dbling, (WIDTH - 200, HEIGHT - 475))
        screen.blit(dskin, (WIDTH - 177, HEIGHT - 475))

        if play_b.draw():
            old_rank = get_rank(rp)
            estce = False
            cf = False
            af = False
            Audio(f'interact/click.wav')
            got_bp_rewards = False
            if mouse_hide:
                pygame.mouse.set_visible(False)
            old_level = season_tiers[current_season-2]
            got_new_level = False
            
            menu_state = "game"
            # pygame.mouse.set_visible(False)

        if not logged_in_any:
            if signup_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                menu_state = "signup"

        if login_b.draw():
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
                    trypass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                    tryUserName = None

                    tryuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                    tryPassWord = None 
                    
                    locked_in = False

                    menu_state = "login"


                    
        
        if rot_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "modes"

        if len_all_modes[all_modes.index(g.mode)] > 1:
            if fill_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                fill0 = not fill0
                if fill0:
                    fill_b = Tick(WIDTH - 160, HEIGHT - 104, 'Fill', font30)
                else:
                    fill_b = Tick(WIDTH - 200, HEIGHT - 104, 'Don\'t Fill', font30)


        gd = render(g.mode, font25, WHITE, BLACK, 3)
        screen.blit(gd, (892 - gd.get_width() / 2, HEIGHT - 290))

        yyy = 104
        if len_all_modes[all_modes.index(g.mode)] > 1:
            yyy = 56

        if ranked: dwe = "Champions: On"
        else: dwe = "Champions: Off"
        gd = render(dwe, font25, WHITE, BLACK, 3)
        screen.blit(gd, (892 - gd.get_width() / 2, HEIGHT - yyy))

        if friend_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "friends"
            f_b = []
            friendy = 0
            fr_b = []
            foff_b = []
            friendoff = {}
            for i in friend_list:
                tgn = random.randint(1, 3)
                if i in lobby:
                    tgn = 0
                foff_b.append(tgn) 
                friendoff[i] = tgn
            for i, m in enumerate(sorted(friend_list, key=grab_foff)): 
                f_b.append(Tick(50, 60 * i + 200, f'{m}', font40, glide=m, glide2=2424))
                fr_b.append(Tick(370, 60 * i + 200, f'Remove', font40, glide=m, glide2=2424))
                

        if settings_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')

            if w_move: wmove_b = Tick(50, 210, 'W/UP Key Movement & Mouse Rotation', font30)
            else: wmove_b = Tick(50, 210, 'Classic WASD/Arrow Keys Movement & Mouse Rotation', font30)

            menu_state = "settings"

        if custom_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            hist = False
            hist_b = Tick(550, 150, 'Sort by Rarity', font30)
            rev = False
            rev_b = Tick(550, 200, 'Reverse', font30)
            menu_state = "customize"

        if is_b.draw():
            pygame.time.wait(400)
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            ismm = False
            menu_state = "item shop"

        if bp_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            old_level = season_tiers[current_season-2]
            menu_state = "battle pass"

        if cc_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "challenges"

        if len(lobby) > len_all_modes[all_modes.index(g.mode)]:
            g.mode = 'Squads'

        if cf:
            draw_text('You Placed #2 Last Round!', font20, 0, 404, 202, color=RED)
        # elif af:
        #     draw_text('The player you spectated won the match.', font20, 0, 404, 202, color=RED)

        draw_text('Your Lobby', font40, 0, 404, 222, color=BLACK)
        for h, i in enumerate(lobby):
            draw_text(f'{h+1}. {i}', font30, 0, 404, 222 + (h+1)*35, color=BLACK)

        for i in lobby_kick:
            if i.draw():
                if i.glide == f'{username} (YOU)': lobby = [f'{username} (YOU)']
                else: 
                    try: lobby.remove(i.glide)
                    except: pass
                lobby_kick = []
                h=0
                for i in lobby:
                    if i == f'{username} (YOU)':
                      lobby_kick.append(Tick(300, 222 + (h+1)*35, 'Leave', font25, glide=i))
                    else:
                      lobby_kick.append(Tick(300, 222 + (h+1)*35, 'Kick', font25, glide=i))
                    h+=1

        if ranked:
            if rp > 0:
                if get_rank(rp) > old_rank:
                    estce = True
                    prems += 50 * (get_rank(rp) - old_rank)
                    old_rank = get_rank(rp)
                    
                if estce:
                    draw_text(f'You Ranked Up!', font25, 0, 10, 520, color=GOLD)
                draw_text(f'Current Rank: {rank_names[get_rank(rp)]}', font40, 0, 10, 550, color=BLACK)
                if get_rank(rp) >= len(rank_names)-1:
                    draw_text(f'RP: {rp} (Max Rank)', font30, 0, 10, 590, color=BLACK)
                else:
                    draw_text(f'RP: {rp} / {rank_targs[get_rank(rp)]}', font30, 0, 10, 590, color=BLACK)
                    draw_text(f'Reward for Ranking Up: +50 Prems', font20, 0, 100, 700, color=BLACK)
                cd1 = rp - rank_targs[get_rank(rp)-1]
                if get_rank(rp) <= 0:
                    cd1 = rp
                cd2 = (rank_targs[get_rank(rp)] - rank_targs[get_rank(rp)-1])
                if get_rank(rp) <= 0:
                    cd2 = rank_targs[get_rank(rp)]
                draw_bar(screen, 100, 635, ((cd1) / cd2), (0, 0, 255), 1.7)
                
                yy = 617
                yy2 = 617
                if get_rank(rp) == 17:
                    yy -= 7

                try:
                    if (get_rank(rp)+1) == 17:
                        yy2 -= 7
                except: pass

                screen.blit(rank_imgs[get_rank(rp)], (10, yy))
                try: screen.blit(rank_imgs[get_rank(rp)+1], (280, yy2))
                except: pass
            else:
                draw_text(f'Currently Unranked', font40, 0, 10, 550, color=BLACK)
                draw_text(f'Play a game to get your initial Rank!', font30, 0, 10, 590, color=BLACK)
        draw_text('PLAY', font100, 0, WIDTH - 250, HEIGHT - 200, color=BLACK)

    elif menu_state == "new season":
        screen.fill((0, 71, 171))
        if nsx < 0:
            if nsx == (-800 + (8*12)):
                Audio('interact/brass.wav')
            nsx += 8
            if nsx >= 0:
                nsx = 0
                Audio('interact/slam.wav')
        else:
            if okay_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                bp_bg = Scale(Image('menu/promo.png'), 1.0675)
                buy_norm_bp = Tick(200, 500, "Buy Battle Pass", font)
                buy_bund_bp = Tick(590, 500, "Buy Battle Bonus", font)
                if not replit:
                        pygame.mixer.music.load(f'data/sfx/other/bpg.wav')
                        pygame.mixer.music.play(-1)
                menu_state = "buy bp"

        fhb = render(f'Season {current_season}', font100, WHITE, BLACK, opx=6)
        screen.blit(fhb, (WIDTH / 2 - fhb.get_width()/2 + nsx, 150))

        fhb = render(f'is here!', font50, WHITE, BLACK, opx=0)
        screen.blit(fhb, (WIDTH / 2 - fhb.get_width()/2 + nsx, 250))

        fhb = render(f'New Season', font25, WHITE, BLACK, opx=2)
        screen.blit(fhb, (WIDTH / 2 - fhb.get_width()/2 + nsx, 450))

    elif menu_state == "is":
        screen.fill((0, 71, 171))
        cq = cork[cork_index]
        pygame.draw.rect(screen, (0, 51, 151), pygame.Rect(445, 0, WIDTH-445, HEIGHT))
        draw_text(f'{get_skin_info(cq.type_of_offer, cq.num)[0]}', font45, 0, 450, 25, color=BLACK)
        draw_text(f'{RARITY_NAMES[get_skin_info(cq.type_of_offer, cq.num)[1]]} {cq.type_of_offer.capitalize()}', font30, 0, 450, 75, color=BLACK)
        # draw_text(f'', font35, 0, 450, 105, color=BLACK)
        

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "item shop"

        draw_text(f'Price: {cq.price} Prems', font40, 0, 460, HEIGHT-140, color=BLACK)

        for a, c in enumerate(cork):
            r = pygame.Rect(500+(a%3 * 130), 150+(a//3*150), 120, 140)
            ort = RARITY_COLORS[get_skin_info(c.type_of_offer, c.num)[1]]
            if r.collidepoint(pygame.mouse.get_pos()):
                cork_index = a
                ort = RARITY_COLORS_OUT[get_skin_info(c.type_of_offer, c.num)[1]]
            pygame.draw.rect(screen, ort, r)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[get_skin_info(c.type_of_offer, c.num)[1]], r, 8)
            screen.blit(c.image_of_skin, (r.x + r.width/2 - (c.image_of_skin.get_width() / 2), r.y + r.height/2 - (c.image_of_skin.get_height() / 2)))
        
        vts = (Smoothscale(cq.image_of_skin, 3))
        pos = (200 - (vts.get_width() / 2), 340 - (vts.get_height() / 2))
        screen.blit(vts, pos)

        if not (cq.num in cq.corresponding_list):
            if ismm:
                if purchase_b.draw():
                    cq = cork[0]
                    if prems >= cq.price:
                        chindex = 0
                        Audio('interact/purchase.wav')
                        prems -= cq.price
                        if logged_in_any: real_dump(prems, (f"data/users/{username}/{username}_prems.json"))
                        cq.corresponding_list.append(cq.num)

                        checklist.append([cq.type_of_offer, cq.num])
                        menu_state = "bought"
                        checklister.append(Button(50, 300, Scale(cq.image_of_skin, 2), 1, glide=0, glide2=332))
                        boux = 0
                        tiq = 0
                        tnt = 0
                        if (cq.type_of_offer, cq.num) in bundles:
                            for bundle in bundles[(cq.type_of_offer, cq.num)]:
                                if (cq.type_of_offer, cq.num) == bundle:
                                    continue
                                checklist.append([bundle[0], bundle[1]])
                                if bundle[0] == "skin": cor = have_skins; ss = 2
                                elif bundle[0] == "glider": cor = have_gliders; ss = 2*0.3
                                elif bundle[0] == "backpack": cor = have_backpacks; ss = 2
                                elif bundle[0] == "emoticon": cor = have_emoticons; ss = 2
                                elif bundle[0] == "spray": cor = have_sprays; ss = 2*0.5
                                cor.append(bundle[1])

                                tiq += 1
                                checklister.append(Button(50, 300, Scale(Image(f"customize/{bundle[0]}s/{bundle[1]}.svg"), ss), 1, glide=0, glide2=332))
                                tnt += Scale(Image(f"customize/{bundle[0]}s/{bundle[1]}.svg"), ss).get_height()

                        for t in range(tiq+1):
                            checktick.append(Tick(0,0,"Equip",font25,glide=0,glide2=332))
            else:
                draw_text("Turn on Purchase Mode to Purchase.", font20, 0, 465, HEIGHT - 95)
        else:
            draw_text("Owned!", font30, 0, 465, HEIGHT - 95)


    elif menu_state == "challenges":
        screen.fill((0, 71, 171))

        if all(cc_complete): reroll_challenges()

        draw_text('Challenges', font50, 0, 50, 150, color=BLACK)
        draw_text(f'Season {current_season}', font40, 0, 50, 200, color=BLACK)
        draw_text(f'Level {season_tiers[current_season-2]}', font30, 0, 50, 240, color=BLACK)
        draw_text(f'XP:', font30, 0, 50, 270, color=BLACK)
        draw_bar(screen, 100, 270, (season_xp / 10000), (0, 0, 255), 1.5)

        for j, i in enumerate(challenges):
                if cc_complete[j]:
                    draw_text(f"COMPLETE! {challenge_acts[i]}", font, 0, 10, 375 + (j*35), color=(0,0,0))
                else:
                    draw_text(f"{challenge_acts[i]} ({cc_tracker[i]}/{cc_goal[i]})", font, 0, 10, 375 + (j*35), color=(0,0,0))

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "settings":
        screen.fill((0, 71, 171))
        draw_text('Settings', font50, 0, 50, 150, color=BLACK)

        if wmove_b.draw():
            w_move = not w_move
            if w_move: wmove_b = Tick(50, 210, 'W/UP Key Movement & Mouse Rotation', font30)
            else: wmove_b = Tick(50, 210, 'Classic WASD/Arrow Keys Movement & Mouse Rotation', font30)

        if contr_b.draw():
            contr = not contr
            if contr: contr_b = Tick(50, 360, 'Controller in-Game: On', font30)
            else: contr_b = Tick(50, 360, 'Controller in-Game: Off', font30)

        
        if pin_b.draw():
            pin_screen = not pin_screen
            if pin_screen: pin_b = Tick(50, 410, 'Emoji / Spray Screen: On', font30)
            else: pin_b = Tick(50, 410, 'Emoji / Spray Screen: Off', font30)
        
        if instr_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                menu_state = "intro"

        if logged_in_any:
            if cuser_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                menu_state = "cuser"

            if cpass_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                menu_state = "cpass"
        else:
            draw_text('Log In or Sign Up to access this setting.', font30, 0, 50, 260, color=BLACK)
            draw_text('Log In or Sign Up to access this setting.', font30, 0, 50, 310, color=BLACK)


        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "intro":
        screen.fill((0, 71, 171))

        draw_text('Instructions / Controls', font50, 0, 50, 150, color=BLACK)


        if contr:
            draw_text('[RIGHT JOYSTICK] to move.', font20, 0, 50, 200, color=BLACK)
            draw_text('[LEFT JOYSTICK] to Rotate.', font20, 0, 50, 225, color=BLACK)

            draw_text('[RIGHT TRIGGER] to shoot.', font20, 0, 50, 250, color=BLACK)
            draw_text('[X] to reload.', font20, 0, 50, 275, color=BLACK)
            draw_text('[LEFT TRIGGER] to drop a weapon.', font20, 0, 50, 300, color=BLACK)
            draw_text('[X] to pick up a weapon. ', font20, 0, 50, 325, color=BLACK)
            draw_text('[=] to view the map. [CLICK RIGHT JOYSTICK] to Pause.', font20, 0, 50, 350, color=BLACK)
            draw_text('[CLICK LEFT JOYSTICK] to view challenges in-game.', font20, 0, 50, 375, color=BLACK)
            draw_text('[RIGHT TRIGGER] to glide down faster while gliding.', font20, 0, 50, 400, color=BLACK)

            draw_text('Be the last one standing!', font20, 0, 50, 450, color=BLACK)
            draw_text('(GRIDROYALE X-BOX One Controls)', font20, 0, 50, 475, color=BLACK)
        
        else:
            if w_move:
                draw_text('[W / Up Arrow] and [S / Down Arrow] keys to move forward / backward.', font20, 0, 50, 200, color=BLACK)
                draw_text('Mouse to Rotate.', font20, 0, 50, 225, color=BLACK)
            else:
                draw_text('[WASD / Arrow Keys] keys to move.', font20, 0, 50, 200, color=BLACK)
                draw_text('Mouse to Rotate.', font20, 0, 50, 225, color=BLACK)

            draw_text('Click to shoot.', font20, 0, 50, 250, color=BLACK)
            draw_text('[R] to reload.', font20, 0, 50, 275, color=BLACK)
            draw_text('[F] to drop a weapon.', font20, 0, 50, 300, color=BLACK)
            draw_text('[E] to pick up a weapon. ', font20, 0, 50, 325, color=BLACK)
            draw_text('[M] to view the map. [P] to Pause.', font20, 0, 50, 350, color=BLACK)
            draw_text('[Q] to view challenges in-game.', font20, 0, 50, 375, color=BLACK)
            draw_text('[SPACE] to glide down faster while gliding.', font20, 0, 50, 400, color=BLACK)

            draw_text('Be the last one standing!', font20, 0, 50, 450, color=BLACK)
            draw_text('(GRIDROYALE Mouse & Keyboard Controls)', font20, 0, 50, 475, color=BLACK)
        

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"


    elif menu_state == "buy bp":
        screen.fill((0, 0, 0))
        screen.blit(bp_bg, (0,0))

        s = pygame.Surface((WIDTH, 300), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0,0,0,180))                         # notice the alpha value in the color
        screen.blit(s, (0, 490))

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"
            pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
            pygame.mixer.music.play(-1)

        draw_text("400 Prems", font, 0, 200, 550,)
        draw_text("1250 Prems", font, 0, 590, 550,)
        draw_text("INCLUDES 18 LEVELS!", font, 0, 590, 580, )
        if buy_norm_bp.draw():
            if prems >= 400:
                    prems -= 400
                    Audio('interact/purchase.wav')
                    got_bp_rewards = False
                    battle_passes[current_season-2] = True
                    for i in range(season_tiers[current_season-2]):
                        try: grant_item(i+1)
                        except: pass
                    ftf = 0
                    crows = 0
                    menu_state = "bought it"
                    pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
                    pygame.mixer.music.play(-1)

        if buy_bund_bp.draw():
            if prems >= 1250:
                    prems -= 1250
                    got_bp_rewards = False
                    Audio('interact/purchase.wav')
                    battle_passes[current_season-2] = True
                    season_tiers[current_season-2] += 18
                    for i in range(season_tiers[current_season-2]):
                        try: grant_item(i+1)
                        except: pass
                    ftf = 0
                    crows = 0
                    menu_state = "bought it"
                    pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
                    pygame.mixer.music.play(-1)


    elif menu_state == "battle pass":
        screen.fill((0, 71, 171))
        
        draw_text('Battle Pass', font50, 0, 50, 150, color=BLACK)
        draw_text(f'Season {current_season}', font40, 0, 50, 200, color=BLACK)

        draw_text(f'After Level 70,', font30, 0, 50, HEIGHT-160, color=BLACK)
        draw_text(f'Gain +25 Prems for every new level, regardless of Battle Pass ownership!', font15, 0, 50, HEIGHT-130, color=BLACK)

        draw_text(f'Level {season_tiers[current_season-2]}', font30, 0, 50, 240, color=BLACK)
        # else: draw_text(f'Log In to Progress the Season {current_season} Battle Pass!', font30, 0, 50, 240, color=BLACK)

        if 1:
        # if logged_in_any:
            if battle_passes[current_season-2] == False:
                if buy_bp.draw():
                    bp_bg = Scale(Image('menu/promo.png'), 1.0675)
                    buy_norm_bp = Tick(200, 500, "Buy Battle Pass", font)
                    buy_bund_bp = Tick(590, 500, "Buy Battle Bonus", font)
                    if not replit:
                        pygame.mixer.music.load(f'data/sfx/other/bpg.wav')
                        pygame.mixer.music.play(-1)
                    menu_state = "buy bp"
                    # if prems >= 650:
                    #     prems -= 650
                    #     got_bp_rewards = False
                    #     battle_passes[current_season-2] = True
                    #     for i in range(season_tiers[current_season-2]):
                    #         try: grant_item(i+1)
                    #         except: pass
                    #     menu_state = "bought it"
            else:
                draw_text(f"You have the Season {current_season} Battle Pass!", font25, 0, 340, 150)

            if season_tiers[current_season-2] < 70:
                if buy_lvl.draw():
                    if prems >= 20:
                        prems -= 20
                        Audio('interact/purchase.wav')
                        got_bp_rewards = False
                        season_tiers[current_season-2] += 1
                        try: grant_item(season_tiers[current_season-2])
                        except: pass

        il = pygame.mouse.get_pos()
        for i, b in enumerate(bpv):
            h = bpr[i]
            j = h.copy()
            j.x += bptx

            if mainbp == b:
                if not j.collidepoint(il):
                    co = "#FF7C1C"
                else:
                    co = "#F9BD92"
            elif (season_tiers[current_season-2] >= b.glide) and battle_passes[current_season-2]:
                if not j.collidepoint(il):
                    co = "#707070"
                else:
                    co = "#C0C2C4"

            elif not lvl_grants[b.glide][2]:
                if (season_tiers[current_season-2] >= b.glide):
                    if not j.collidepoint(il):
                        co = "#707070"
                    else:
                        co = "#C0C2C4"
                else:
                    if not j.collidepoint(il):
                        co = "#72FB79"
                    else:
                        co = "#D0FCD4"

            else:
                if not j.collidepoint(il):
                    co = "#0E97FF"
                else:
                    co = "#7BC2FB"
                
            
            pygame.draw.rect(screen, co, j)
            pygame.draw.rect(screen, (220,220,220), j, 5)

            b.draw()
            draw_text(f'{b.glide}', font30, 0, j.x+35, j.y-32, color=BLACK)
            if j.collidepoint(il):
                if pygame.mouse.get_pressed()[0]:
                    mainbp = b
        
        hoh = "Reward"
        if lvl_grants[mainbp.glide][1] == "prems":
            hoh = "40 Prems"
        elif lvl_grants[mainbp.glide][1] == "ls":
            hoh = "Loading Screen"
        elif lvl_grants[mainbp.glide][1] == "trail":
            hoh = "Gliding Trail"
        elif lvl_grants[mainbp.glide][1] == "spray":
            hoh = "Cosmetic Spray"
        elif lvl_grants[mainbp.glide][1] == "emoticon":
            hoh = "Cosmetic Emoticon"
        elif lvl_grants[mainbp.glide][1] == "music":
            hoh = "Music Pack"
        elif lvl_grants[mainbp.glide][1] == "skin":
            hoh = NSKINS[mainbp.glide3]
        elif lvl_grants[mainbp.glide][1] == "backpack":
            hoh = NPACKS[mainbp.glide3]
        elif lvl_grants[mainbp.glide][1] == "glider":
            hoh = NGLIDERS[mainbp.glide3]
            

        dfdf = (len(hoh))
        lrewl = dfdf
        hfsd = 0
        if lrewl > 12:
            ll = dfdf - 12
            ff = pygame.font.SysFont("bahnschrift", 50 - (ll*2))
            hfsd = (ll*2)
        else:
            ff = font50
        draw_text(f'{hoh}', ff, 0, 50, 300 + hfsd, color=BLACK)

        vd = lvl_grants[mainbp.glide][1]
        vdd = vd.capitalize()
        if vd == "ls":
            vdd = "Loading Screen"

        draw_text(f'{vdd}', font30, 0, 50, 350, color=BLACK)

        dd = lvl_grants[mainbp.glide][2]
        if not dd:
            sak = "Free!"
            th = GREEN
        else:
            sak = "Battle Pass Exclusive"
            th = BLACK
        draw_text(f'{sak}', font20, 0, 50, 380, color=th)

        if lvl_grants[mainbp.glide][1] == "skin":
            elle = Scale(bpo[mainbp.glide-1], 3)
            screen.blit(elle, (520 - elle.get_width() / 2, 360 - elle.get_height() / 2))
        else:
            elle = bpi[mainbp.glide-1]
            screen.blit(elle, (520 - elle.get_width() / 2, 360 - elle.get_height() / 2))


        # for t in lvl_display:
        #     t.draw()

            # BROKEN:
            # if t.glide+1 == season_tiers[current_season-2]:
            #     if season_tiers[current_season-2] <= 70:
            #         draw_text('You are Here.', font30, 0, 180*(t.glide) + bpx + 15, 180, color=BLACK)

        # if lf_b.draw():
        #     if bpx < 0: bpx += 600
        #     lvl_display = []
        #     for i in range(70):
        #        lvl_display.append(Button(200*i + bpx, 270, lvl_imgs[i], 1, glide=i))

        # if rf_b.draw():
        #     if bpx > -23*600: bpx -= 600
        #     lvl_display = []
        #     for i in range(70):
        #        lvl_display.append(Button(200*i + bpx, 270, lvl_imgs[i], 1, glide=i))

        if bpexit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "bought":
        screen.fill((0, 71, 171))
        
        if boux >= 0:
            draw_text('Rewards!', font50, 0, 50, 50, color=BLACK)
            if len(checklist) != 1: hgr = "s"
            else: hgr = ""
            draw_text(f'You have gained {len(checklist)} new reward{hgr}! ({chindex+1}/{len(checklist)})', font30, 0, 50, 100, color=BLACK)

        
        a = chindex
        i = checklister[a]
        i.rect.x = 510-(i.image.get_width() / 2)
        i.rect.y = 660-(i.image.get_height() / 2)
        

        i.draw()
        cutf = 0
        # if (checklist[a][0]) == "backpack": cutf = 100

        

        

        yyb = render(f'{get_skin_info(checklist[a][0], checklist[a][1])[0]} ({(checklist[a][0]).capitalize()})', font50, BLACK, BLACK, opx=0)
        screen.blit(yyb, (510-(yyb.get_width() / 2), 210-(yyb.get_height() / 2)))

        h = checktick[a]
        h.rect.x, h.rect.y = 460, 250
        
        


        if (checklist[a][0]) == "skin":
            if skin_num != checklist[a][1]:
                if h.draw():
                    skin_num = checklist[a][1]
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
            else:
                draw_text("Equipped!", font30, 0, 432, 251, color=BLACK)
        
        if (checklist[a][0]) == "backpack":
            if backpack_num != checklist[a][1]:
                if h.draw():
                    backpack_num = checklist[a][1]
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
            else:
                draw_text("Equipped!", font30, 0, 432, 251, color=BLACK)

        if (checklist[a][0]) == "glider":
            if glider_num != checklist[a][1]:
                if h.draw():
                    glider_num = checklist[a][1]
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
            else:
                draw_text("Equipped!", font30, 0, 432, 251, color=BLACK)

        if (checklist[a][0]) == "emoticon":
            if emoticon_num[0] != checklist[a][1]:
                if h.draw():
                    emoticon_num[0] = checklist[a][1]
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
            else:
                draw_text("Equipped!", font30, 0, 432, 251, color=BLACK)

        if (checklist[a][0]) == "spray":
            if spray_num[0] != checklist[a][1]:
                if h.draw():
                    spray_num[0] = checklist[a][1]
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
            else:
                draw_text("Equipped!", font30, 0, 432, 251, color=BLACK)

        # for a, i in enumerate(checklister): 
        #     i.draw()

        #     cutf = 0
        #     if (checklist[a][0]) == "backpack": cutf = 100

        #     h = checktick[a]
        #     h.rect.x, h.rect.y = 75+i.image.get_width()-cutf, i.rect.y - 15 + (i.image.get_height() / 2)
            
        #     draw_text(f'{get_skin_info(checklist[a][0], checklist[a][1])[0]} ({(checklist[a][0]).capitalize()})', font30, 0, 75+i.image.get_width()-cutf, i.rect.y - 55 + (i.image.get_height() / 2), color=BLACK)
        #     if (checklist[a][0]) == "skin":
        #         if skin_num != checklist[a][1]:
        #             if h.draw():
        #                 skin_num = checklist[a][1]
        #                 Audio(f'interact/state{random.randint(1, 3)}.wav')
            
        #     if (checklist[a][0]) == "backpack":
        #         if backpack_num != checklist[a][1]:
        #             if h.draw():
        #                 backpack_num = checklist[a][1]
        #                 Audio(f'interact/state{random.randint(1, 3)}.wav')

        #     if (checklist[a][0]) == "glider":
        #         if glider_num != checklist[a][1]:
        #             if h.draw():
        #                 glider_num = checklist[a][1]
        #                 Audio(f'interact/state{random.randint(1, 3)}.wav')

        if chindex != 0:
            if prev_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                chindex -= 1

        if chindex < (len(checklister)-1):
            if next_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                chindex += 1
            
        else:
            if exit_b.draw():
                checklister = []
                checktick = []
                checklist = []
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                menu_state = "item shop"

    elif menu_state == "bought it":
        screen.fill((0, 71, 171))
        screen.blit(bfgfg, (0,0))
        if crows == 0: crows = 0.01
        if crows < 1:
            crows *= 1.03
        else:
            crows = 1
            draw_text("Battle Pass Unlocked!", font45, 0, 290, HEIGHT / 2 + 120 - 75, color=BLACK)
            if len(str(current_season)) == 1: t = 7
            else: t=0
            draw_text(f"Season {current_season}", font30, 0, 440+t, HEIGHT / 2 + 170 - 75, color=BLACK)
            if ftf:
                draw_text(f"   +18 LEVELS!", font20, 0, 395, HEIGHT / 2 + 200 - 75, color=BLACK)
        v = Scale(Image("HUD/bp/crown.svg"), crows)
        vr = v.get_rect()
        vr.x, vr.y = (WIDTH / 2 - (v.get_width() / 2), HEIGHT / 2 - (v.get_height() / 2) - 75)
        screen.blit(v, vr)


        if crows >= 1:
            if exit_b.draw():
                Audio(f'interact/state{random.randint(1, 3)}.wav')
                bptx = 0
                mbp(0, 1, False, minced=True)
                menu_state = "new lvls"
                # menu_state = "battle pass"

    elif menu_state == "champions info":
        screen.fill((0, 71, 171))
        
        draw_text('Champions: What Is It?', font40, 0, 50, 150, color=BLACK)

        draw_text('GRIDROYALE: CHAMPIONS is a mode of play where you rank up by eliminating players and placing high', font20, 0, 50, 200, color=BLACK)
        draw_text('in matches. Climb up the ranks to reach the maximum rank: OFF THE GRID! To start, play your first ', font20, 0, 50, 220, color=BLACK)
        draw_text('match in the Champions mode by turning it on. This match will determine your initial rank, and ', font20, 0, 50, 240, color=BLACK)
        draw_text('you will get +50 Prems as a reward. Then everytime you rank up, you\'ll get +50 Prems again!', font20, 0, 50, 260, color=BLACK)
        draw_text('Are you ready?', font20, 0, 50, 280, color=BLACK)

        dg = round((rp / rank_targs[16])*100, 2)
        if dg > 100:
            dg = 100
        draw_text(f'{dg}% Complete with the Champion Road!', font20, 0, 80, 346, color=BLACK)
        sli = rp
        if sli > rank_targs[16]:
            sli = rank_targs[16]
        draw_bar(screen, 80, 320, (sli / rank_targs[16]), (0,0,255), 1, w=850, h=20)

        if bpexit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

        i = 0
        for x in range(6):
            for y in range(3):
                ix = x*150 + 80
                iy = y*100 + 380

                screen.blit(Scale(rank_imgs[i], 0.7), (ix, iy))

                col = WHITE
                if i < get_rank(rp):
                    col = GREEN
                elif i == get_rank(rp):
                    col = (0,255,255)
                draw_text(f"{rank_names[i]}", font15, 0, ix, iy+60, color=col)
                if i == 17:
                    draw_text(f"{rank_targs[i-1]}+ RP", font15, 0, ix, iy+75, color=col)
                elif i == 0:
                    draw_text(f"0 - {rank_targs[i]} RP", font15, 0, ix, iy+75, color=col)
                else:
                    draw_text(f"{rank_targs[i-1]} - {rank_targs[i]} RP", font15, 0, ix, iy+75, color=col)

                i += 1

        

    elif menu_state == "modes":
        screen.fill((0, 71, 171))
        
        draw_text('Select Your Mode', font40, 0, 50, 150, color=BLACK)
        i=0
        for m in mode_bs:
            if len(lobby) <= len_all_modes[i]:
                if m.draw():
                    g.mode = m.glide
                    if (g.mode in ["Team Rumble", "Marvel Mayhem", "Solid Gold", "Shotgun Special"]):
                        ranked = False
                        rpb = Tick(WIDTH - 300, 200, f'Champions: Off', font40)
            i+=1
            if m.glide == g.mode:
                draw_text('Selected', font40, 0, 365, 60 * (i-1) + 203, color=BLACK)
            elif m.glide in LTMs:
                draw_text('Limited Time Mode!', font25, 0, 365, 60 * (i-1) + 212, color=BLACK)

        draw_text(ltm_intros[g.mode][0], font25, 0, 50, 60 * (i) + 212, color=BLACK)

        if rpb.draw():
            if not (g.mode in ["Team Rumble", "Marvel Mayhem", "Solid Gold", "Shotgun Special"]):
                ranked = not ranked
                if ranked:
                    rpb = Tick(WIDTH - 300, 200, f'Champions: On', font40)
                else:
                    rpb = Tick(WIDTH - 300, 200, f'Champions: Off', font40)

        if irpb.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "champions info"

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "customize":
        screen.fill((0, 71, 171))
        
        draw_text('Type of Customization', font40, 0, 50, 150, color=BLACK)
     
        screen.blit(dbling, (WIDTH - 200 - 150, HEIGHT - 400 - 50))
        screen.blit(dskin, (WIDTH - 177 - 150, HEIGHT - 400 - 50))

        if hist_b.draw():
            hist = not hist
            if not hist:
                hist_b = Tick(550, 150, 'Sort by Rarity', font30)
            else:
                hist_b = Tick(550, 150, 'Sort by New', font30)
        
        if rev_b.draw():
            rev = not rev
            if rev:
                rev_b = Tick(550, 200, 'Reverse', font30)
            else:
                rev_b = Tick(550, 200, 'Reverse', font30)

        for m in custom_types_b:
            if m.draw():
                customy = 0
                menu_state = m.glide

                if m.glide == "Skin":
                    my_skins = []
                    dv = sorted(have_skins, key=get_rar1, reverse=(not rev))
                    if hist: 
                        dv = have_skins.copy()
                        if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        my_skins.append(Button(50 + (i % 7) * 120, 280 + (i//7) * 120, Image(f'customize/skins/{skin}.svg'), 1, glide=skin, glide2=69420))

                if m.glide == "Glider":
                    my_gliders = []
                    dv = sorted(have_gliders, key=get_rar2, reverse=(not rev))
                    if hist: 
                        dv = have_gliders.copy()
                        if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        my_gliders.append(Button(50 + (i % 7) * 120, 220 + (i//7) * 120, Image(f'customize/gliders/{skin}.svg'), 0.3, glide=skin, glide2=69420))

                if m.glide == "Contrail":
                    my_trails = []
                    dv = have_trails.copy()
                    if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        if skin == 0:
                            rr = Image(f'ess/nonatr.svg')
                        else:
                            rr = Image(f'customize/trails/{skin}.svg')
                        customy = 0
                        my_trails.append(Button(50 + (i % 7) * 120, 220 + (i//7) * 120 + customy, rr, 1, glide=skin, glide2=69420))

                if m.glide == "Music Pack":
                    my_musics = []
                    dv = have_musics.copy()
                    if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        rr = Image(f'customize/musics/{skin}.svg')
                        customy = 0
                        my_musics.append(Button(50 + (i % 6) * 130, 220 + (i//6) * 100 + customy, rr, 1, glide=skin, glide2=69420))

                if m.glide == "Backpack":
                    my_backpacks = []
                    dv = sorted(have_backpacks, key=get_rar3, reverse=(not rev))
                    if hist: 
                        dv = have_backpacks.copy()
                        if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        if skin==0: im = Image(f'ess/nonabb.svg')
                        else: im = Image(f'customize/backpacks/{skin}.svg')

                        my_backpacks.append(Button(50 + (i % 7) * 120, 220 + (i//7) * 110, im, 1, glide=skin, glide2=69420))

                if m.glide == "Loading Screen":
                    my_ls = []
                    dv = have_ls.copy()
                    if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        im = Scale(Image(f'customize/ls/{skin}.png'), 0.2)
                        my_ls.append(Button(50 + (i % 5) * 144, 220 + (i//5) * 144, im, 1, glide=skin, glide2=69420))


                if m.glide == "Emoticon":
                    my_emoticons = []
                    dv = sorted(have_emoticons, key=get_rar4, reverse=(not rev))
                    if hist: 
                        dv = have_emoticons.copy()
                        if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        im = Image(f'customize/emoticons/{skin}.svg')
                        my_emoticons.append(Button(75 + (i % 4) * 180, 220 + (i//4) * 180, im, 1, glide=skin, glide2=69420))

                    emoji_index = 0

                    emoti_style = []
                    for i in range(3):
                        emoti_style.append(Tick(450 + i*100, 150, f'Slot {i+1}', font30, glide=i))


                if m.glide == "Spray":
                    my_sprays = []
                    dv = sorted(have_sprays, key=get_rar5, reverse=(not rev))
                    if hist: 
                        dv = have_sprays.copy()
                        if rev: dv.reverse()
                    for i, skin in enumerate(dv):
                        im = Scale(Image(f'customize/sprays/{skin}.svg'), 0.5)
                        my_sprays.append(Button(100 + (i % 8) * 100, 220 + (i//8) * 100, im, 1, glide=skin, glide2=69420))

                    spray_index = 0

                    spray_style = []
                    for i in range(3):
                        spray_style.append(Tick(450 + i*100, 150, f'Slot {i+1}', font30, glide=i))



        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "Skin":
        screen.fill((0, 71, 171))

        if customy >= 0: draw_text('Customize Skin', font40, 0, 50, 150, color=BLACK)
        for m in my_skins:
            rr = pygame.Rect(m.rect.x-10, m.rect.y-15, m.width+25, m.height+25)
            d = get_skin_info("skin", m.glide)
            if d == None:
                d = (None, 5)
            c = RARITY_COLORS[d[1]]
            if m.rect.collidepoint(pygame.mouse.get_pos()):
                c = RARITY_COLORS_OUT[d[1]]
            
            pygame.draw.rect(screen, c, rr)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[d[1]], rr, 5)
            m.draw()
            if rr.collidepoint(pygame.mouse.get_pos()):
             if pygame.mouse.get_pressed()[0]:
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                skin_num = m.glide
            if m.glide == skin_num:
                pygame.draw.rect(screen, (0,255,0), rr, 5)

        if customy >= 0:
          if rxl_b.draw():
            skin_num = random.choice(have_skins)

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_skins = []
        #     for i, skin in enumerate(have_skins):
        #         my_skins.append(Button(50 + (i % 15) * 60, 220 + (i//15) * 60 + customy, Image(f'customize/skins/{skin}.svg'), 1, glide=skin))

        # if df_b.draw():
        #     customy -= 75
        #     my_skins = []
        #     for i, skin in enumerate(have_skins):
        #         my_skins.append(Button(50 + (i % 15) * 60, 220 + (i//15) * 60 + customy, Image(f'customize/skins/{skin}.svg'), 1, glide=skin))

        if exit_b.draw():
            dskin = Scale(Image(f'customize/skins/{skin_num}.svg'), 2)
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"

    elif menu_state == "Glider":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text('Customize Glider', font40, 0, 50, 150, color=BLACK)
        for m in my_gliders:

            rr = pygame.Rect(m.rect.x-10, m.rect.y-15, m.width+25, m.height+25)
            d = get_skin_info("glider", m.glide)
            if d == None:
                d = (None, 5)
            c = RARITY_COLORS[d[1]]
            if m.rect.collidepoint(pygame.mouse.get_pos()):
                c = RARITY_COLORS_OUT[d[1]]
            pygame.draw.rect(screen, c, rr)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[d[1]], rr, 5)
            m.draw()
            # if m.draw():
            if rr.collidepoint(pygame.mouse.get_pos()):
             if pygame.mouse.get_pressed()[0]:
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                glider_num = m.glide
            if m.glide == glider_num:
                pygame.draw.rect(screen, (0,255,0), rr, 5)

        if customy >= 0:
          if rxl_b.draw():
            glider_num = random.choice(have_gliders)

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_gliders = []
        #     for i, skin in enumerate(have_gliders):
        #                 my_gliders.append(Button(50 + (i % 15) * 60, 220 + (i//15) * 100 + customy, Image(f'customize/gliders/{skin}.svg'), 0.3, glide=skin))

        # if df_b.draw():
        #     customy -= 75
        #     my_gliders = []
        #     for i, skin in enumerate(have_gliders):
        #                 my_gliders.append(Button(50 + (i % 15) * 60, 220 + (i//15) * 100 + customy, Image(f'customize/gliders/{skin}.svg'), 0.3, glide=skin))

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"

    elif menu_state == "Contrail":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text('Customize Contrail', font40, 0, 50, 150, color=BLACK)

        


        for m in my_trails:
            rr = pygame.Rect(m.rect.x-10, m.rect.y-15, m.width+25, m.height+25)
            d = (None, 2)
            if m.glide == 0:
                d = (None, 0)
            c = RARITY_COLORS[d[1]]
            if m.rect.collidepoint(pygame.mouse.get_pos()):
                c = RARITY_COLORS_OUT[d[1]]
            pygame.draw.rect(screen, c, rr)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[d[1]], rr, 5)
            m.draw()
            # if m.draw():
            if rr.collidepoint(pygame.mouse.get_pos()):
             if pygame.mouse.get_pressed()[0]:
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                trail_num = m.glide
            if m.glide == trail_num:
                pygame.draw.rect(screen, (0,255,0), rr, 5)

        if customy >= 0:
          if rxl_b.draw():
            trail_num = random.choice(have_trails)

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_trails = []
        #     for i, skin in enumerate(have_trails):
        #                 if skin==0: t = Image(f'ess/nonatr.svg')
        #                 else: t = Image(f'customize/trails/{skin}.svg')
        #                 my_trails.append(Button(50 + (i % 15) * 60, 220 + (i//15) * 60 + customy, t, 1, glide=skin))

        # if df_b.draw():
        #     customy -= 75
        #     my_trails = []
        #     for i, skin in enumerate(have_trails):
        #                 if skin==0: t = Image(f'ess/nonatr.svg')
        #                 else: t = Image(f'customize/trails/{skin}.svg')
        #                 my_trails.append(Button(50 + (i % 15) * 60, 220 + (i//15) * 60 + customy, t, 1, glide=skin))

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"

    elif menu_state == "Music Pack":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text('Customize Music Pack', font40, 0, 50, 150, color=BLACK)
        for m in my_musics:
            if m.draw():
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                music_num = m.glide
                if not replit:
                    pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
                    pygame.mixer.music.play(-1)
            if m.glide == music_num:
                pygame.draw.rect(screen, (0,255,0), pygame.Rect(m.rect.x, m.rect.y, m.width, m.height), 3)
        if customy >= 0:
          if rxl_b.draw():
            music_num = random.choice(have_musics)
            if not replit:
                    pygame.mixer.music.load(f'data/sfx/music/{music_num}.wav')
                    pygame.mixer.music.play(-1)

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_musics = []
        #     for i, skin in enumerate(have_musics):
        #                 t = Image(f'customize/musics/{skin}.svg')
        #                 my_musics.append(Button(50 + (i % 7) * 130, 220 + (i//7) * 100 + customy, t, 1, glide=skin))

        # if df_b.draw():
        #     customy -= 75
        #     my_musics = []
        #     for i, skin in enumerate(have_musics):
        #                 t = Image(f'customize/musics/{skin}.svg')
        #                 my_musics.append(Button(50 + (i % 7) * 130, 220 + (i//7) * 100 + customy, t, 1, glide=skin))

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"

    elif menu_state == "Backpack":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text('Customize Backpack', font40, 0, 50, 150, color=BLACK)
        for m in my_backpacks:
            rr = pygame.Rect(m.rect.x-10, m.rect.y-15, m.width+25, m.height+25)
            d = get_skin_info("backpack", m.glide)
            if d == None:
                d = (None, 5)
            c = RARITY_COLORS[d[1]]
            if m.rect.collidepoint(pygame.mouse.get_pos()):
                c = RARITY_COLORS_OUT[d[1]]
            pygame.draw.rect(screen, c, rr)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[d[1]], rr, 5)
            m.draw()
            # if m.draw():
            if rr.collidepoint(pygame.mouse.get_pos()):
             if pygame.mouse.get_pressed()[0]:
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                backpack_num = m.glide
            if m.glide == backpack_num:
                pygame.draw.rect(screen, (0,255,0), rr, 5)

        if customy >= 0:
            if rxl_b.draw():
                backpack_num = random.choice(have_backpacks)

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_backpacks = []
        #     for i, skin in enumerate(have_backpacks):
        #         if skin==0: im = Image(f'ess/nonabb.svg')
        #         else: im = Image(f'customize/backpacks/{skin}.svg')

        #         my_backpacks.append(Button(50 + (i % 13) * 70, 220 + (i//13) * 60 + customy, im, 1, glide=skin))

        # if df_b.draw():
        #     customy -= 75
        #     my_backpacks = []
        #     for i, skin in enumerate(have_backpacks):
        #         if skin==0: im = Image(f'ess/nonabb.svg')
        #         else: im = Image(f'customize/backpacks/{skin}.svg')

        #         my_backpacks.append(Button(50 + (i % 13) * 70, 220 + (i//13) * 60 + customy, im, 1, glide=skin))


        if exit_b.draw():
            dbling = Scale(Image(f'customize/backpacks/{backpack_num}.svg'), 2)
            Audio(f'interact/state{random.randint(1, 3)}.wav') 
            menu_state = "customize"

    elif menu_state == "Loading Screen":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text('Customize Loading Screen', font40, 0, 50, 150, color=BLACK)
        for m in my_ls:
            if m.draw():
                if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rl_b.rect.collidepoint(pygame.mouse.get_pos()))):
                    ls_num = m.glide
                    rlr = False
                    rl_b = Tick(WIDTH - 475, 150, 'Set Random', font30)
            if m.glide == ls_num:
                pygame.draw.rect(screen, (0,255,0), pygame.Rect(m.rect.x, m.rect.y, m.width, m.height), 3)

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_ls = []
        #     for i, skin in enumerate(have_ls):
        #         im = Scale(Image(f'customize/ls/{skin}.png'), 0.2)

        #         my_ls.append(Button(50 + (i % 6) * 144, 220 + (i//6) * 144 + customy, im, 1, glide=skin, glide2=69420))

        # if df_b.draw():
        #     customy -= 75
        #     my_ls = []
        #     for i, skin in enumerate(have_ls):
        #         im = Scale(Image(f'customize/ls/{skin}.png'), 0.2)

        #         my_ls.append(Button(50 + (i % 6) * 144, 220 + (i//6) * 144 + customy, im, 1, glide=skin, glide2=69420))

        if customy >= 0:
            if rl_b.draw():
                rlr = not rlr
                if rlr:
                    rl_b = Tick(WIDTH - 475, 150, 'Set Custom', font30)
                    prevls = ls_num
                    ls_num = random.choice(have_ls)
                else:
                    rl_b = Tick(WIDTH - 475, 150, 'Set Random', font30)
                    ls_num = prevls


        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"


        
    elif menu_state == "Emoticon":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text(f'Customize Emoticon #{emoji_index+1}', font30, 0, 50, 150, color=BLACK)
        for m in my_emoticons:
            rr = pygame.Rect(m.rect.x-10, m.rect.y-15, m.width+25, m.height+25)
            d = get_skin_info("emoticon", m.glide)
            if d == None:
                d = (None, 5)
            c = RARITY_COLORS[d[1]]
            if m.rect.collidepoint(pygame.mouse.get_pos()):
                c = RARITY_COLORS_OUT[d[1]]
            pygame.draw.rect(screen, c, rr)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[d[1]], rr, 5)
            m.draw()
            # if m.draw():
            if rr.collidepoint(pygame.mouse.get_pos()):
             if pygame.mouse.get_pressed()[0]:
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                emoticon_num[emoji_index] = m.glide
            if m.glide == emoticon_num[emoji_index]:
                pygame.draw.rect(screen, (0,255,0), rr, 5)

        if customy >= 0: 
            if rxl2_b.draw():
                emoticon_num[emoji_index] = random.choice(have_emoticons)

        if customy >= 0: 
            for m in emoti_style:
                if m.draw():
                    
                    emoji_index = m.glide
                    customy = 0
                    # my_emoticons = []
                    # for i, skin in enumerate(have_emoticons):
                    #     im = Image(f'ess/nonabb.svg')
                    #     im = Image(f'customize/emoticons/{skin}.svg')
        
                    #     my_emoticons.append(Button(50 + (i % 8) * 100, 220 + (i//8) * 60 + customy, im, 1, glide=skin, glide2=69420))

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_emoticons = []
        #     for i, skin in enumerate(have_emoticons):
        #         im = Image(f'customize/emoticons/{skin}.svg')

        #         my_emoticons.append(Button(50 + (i % 8) * 100, 220 + (i//8) * 60 + customy, im, 1, glide=skin, glide2=69420))

        # if df_b.draw():
        #     customy -= 75
        #     my_emoticons = []
        #     for i, skin in enumerate(have_emoticons):
        #         im = Image(f'ess/nonabb.svg')
        #         im = Image(f'customize/emoticons/{skin}.svg')

        #         my_emoticons.append(Button(50 + (i % 8) * 100, 220 + (i//8) * 60 + customy, im, 1, glide=skin, glide2=69420))


        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"

    elif menu_state == "Spray":
        screen.fill((0, 71, 171))
        if customy >= 0: draw_text(f'Customize Spray #{spray_index+1}', font30, 0, 50, 150, color=BLACK)
        for m in my_sprays:
            rr = pygame.Rect(m.rect.x-10, m.rect.y-15, m.width+25, m.height+25)
            d = get_skin_info("spray", m.glide)
            if d == None:
                d = (None, 5)
            c = RARITY_COLORS[d[1]]
            if m.rect.collidepoint(pygame.mouse.get_pos()):
                c = RARITY_COLORS_OUT[d[1]]
            pygame.draw.rect(screen, c, rr)
            pygame.draw.rect(screen, RARITY_COLORS_OUT[d[1]], rr, 5)
            m.draw()
            # if m.draw():
            if rr.collidepoint(pygame.mouse.get_pos()):
             if pygame.mouse.get_pressed()[0]:
              if (not (uf_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (df_b.rect.collidepoint(pygame.mouse.get_pos())) and (not (exit_b.rect.collidepoint(pygame.mouse.get_pos()))) and (not (rxl_b.rect.collidepoint(pygame.mouse.get_pos())))):
                spray_num[spray_index] = m.glide
            if m.glide == spray_num[spray_index]:
                pygame.draw.rect(screen, (0,255,0), rr, 5)

        if customy >= 0: 
            if rxl2_b.draw():
                spray_num[spray_index] = random.choice(have_sprays)
        
        if customy >= 0: 
            for m in spray_style:
                if m.draw():
                    customy = 0
                    spray_index = m.glide
                    # my_sprays = []
                  

        # if uf_b.draw():
        #     if customy < 0: customy += 75
        #     my_sprays = []
        #     for i, skin in enumerate(have_sprays):
        #                 im = Scale(Image(f'customize/sprays/{skin}.svg'), 0.5)
        #                 my_sprays.append(Button(50 + (i % 15) * 65, 220 + (i//15) * 60 + customy, im, 1, glide=skin))

        # if df_b.draw():
        #     customy -= 75
        #     my_sprays = []
        #     for i, skin in enumerate(have_sprays):
        #                 im = Scale(Image(f'customize/sprays/{skin}.svg'), 0.5)
        #                 my_sprays.append(Button(50 + (i % 15) * 65, 220 + (i//15) * 60 + customy, im, 1, glide=skin))


        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "customize"
        

    elif menu_state == "item shop":
        screen.fill((0, 71, 171))
        

        draw_text('Item Shop', font40, 0, 50, 150, color=BLACK)

        if ism.draw():
            ismm = not ismm
            if ismm:
                ism = Tick(400, 150, f'Purchase Mode', font30)
            else:
                ism = Tick(400, 150, f'View Mode', font30)

        if ismm:
            if rsm.draw():
                if prems >= 15:
                    prems -= 15
                    Audio("interact/purchase.wav")
                    reroll_is()
                    ismm = False
                    ism = Tick(400, 150, f'View Mode', font30)

        for iss in item_shops:
                iss.draw()
        if not logged_in_any:
            draw_text('You must be logged in to purchase from the item shop.', font30, 0, 50, 670, color=BLACK)


        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "controller":
        screen.fill((0, 71, 171))
        draw_text('Controller Detected!', font50, 0, 50, 150, color=BLACK)
        draw_text('Would you like to play with your controller today?', font25, 0, 50, 200, color=BLACK)

        if yes_b.draw():
            contr = 1
            if contr: contr_b = Tick(50, 360, 'Controller in-Game: On', font30)
            else: contr_b = Tick(50, 360, 'Controller in-Game: Off', font30)
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

        if no_b.draw():
            contr = 0
            if contr: contr_b = Tick(50, 360, 'Controller in-Game: On', font30)
            else: contr_b = Tick(50, 360, 'Controller in-Game: Off', font30)
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"
    
    elif menu_state == "friends":
        screen.fill((0, 71, 171))
        

        lobby_kick = []
        h=0
        for i in lobby:
          if i == f'{username} (YOU)':
            lobby_kick.append(Tick(300, 222 + (h+1)*35, 'Leave', font25, glide=i))
          else:
            lobby_kick.append(Tick(300, 222 + (h+1)*35, 'Kick', font25, glide=i))
          h+=1
        
        if friendy >= 0: draw_text('Your Friends', font40, 0, 50, 150, color=BLACK)
        
        i=0
        for h in (f_b):
            if h.draw():
              if friendoff[h.glide] == 1:
                if len(lobby) < 4:
                  if (h.glide in lobby) == False and (h.glide != 0):
                      g.mode = "Squads"
                      lobby.append(h.glide)
            i+=1
        i=0

        # if uf_b.draw():
        #     if friendy < 0: friendy += 300
        #     f_b = []
        #     fr_b = []
        #     for i, m in enumerate(friend_list): 
        #         f_b.append(Tick(50, 60 * i + 200 + friendy, f'{m}', font40, glide=m))
        #         fr_b.append(Tick(370, 60 * i + 200 + friendy, f'Remove', font40, glide=m))

        # if df_b.draw():
        #     friendy -= 300
        #     f_b = []
        #     fr_b = []
        #     for i, m in enumerate(friend_list): 
        #         f_b.append(Tick(50, 60 * i + 200 + friendy, f'{m}', font40, glide=m))
        #         fr_b.append(Tick(370, 60 * i + 200 + friendy, f'Remove', font40, glide=m))

        i=0
        for h in fr_b:
            if h.draw():
                friend_list.remove(h.glide)
                menu_state = "main"
            if h.glide in lobby:
                draw_text('In Your Lobby', font, 0, 600, 60 * i + 215 + friendy, color=(0, 255, 255))
            elif friendoff[h.glide] != 1 and len(friendoff) > 0:
                draw_text('Offline :(', font, 0, 600, 60 * i + 215 + friendy, color=(0, 0, 0))
            else:
                draw_text('In Lobby', font, 0, 600, 60 * i + 215 + friendy, color=(0, 255, 0))

            i+=1

        
        
            
        
            

        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"
    
    elif menu_state == "error login u":
        screen.fill((0, 0, 0))
        draw_text(f'We were unable to change your username.', pygame.font.SysFont('bahnschrift', 30), (255,0,0), 10, 10)
        draw_text(f'Please try again in a few minutes.', font25, (255,0,0), 10, 40)
        if exit_b.draw():
            Audio(f'interact/state{random.randint(1, 3)}.wav')
            menu_state = "main"

    elif menu_state == "cpass":
            #draw the different options buttons
            screen.fill((0, 0, 0))
            if pppppp != None:
                draw_text(f'Click [CONFIRM] to exit this page and change your password.', pygame.font.SysFont('bahnschrift', 30), 0, 10, 10)
                draw_text(f'You are changing your password to "{pppppp}."', font25, 0, 10, 50)
                if confirm_b.draw():
                    real_dump(pppppp, f"data/users/{username}/{username}_pw.json")
                    cpass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                    pppppp = None
                    Audio(f'interact/state{random.randint(1, 3)}.wav')
                    menu_state =  "main"
            else:
                draw_text(f'Change your password!', pygame.font.SysFont('bahnschrift', 30), 0, 10, 10)
                draw_text(f'Type in the password you would like to use.', pygame.font.SysFont('bahnschrift', 20), 0, 10, 50)
                pppppp = cpass_type.update(10, 300, pygame.font.SysFont('bahnschrift', 40), 0)

                if exit_b.draw():
                        cpass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                        pppppp = None
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state =  "main"

    elif menu_state == "cuser":
            #draw the different options buttons
            screen.fill((0, 0, 0))
            if cccccc != None:
                list_of_users = real_load(f"data/users/@list_of_users.json")
                if cccccc in list_of_users:
                    draw_text(f'Sorry, but that username is unavailable.', font25, (255,0,0), 10, 10)
                    if exit_b.draw():
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state = "cuser"

                        cuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                        cccccc = None
                else:
                    draw_text(f'Click [CONFIRM] to exit this page and change your username.', pygame.font.SysFont('bahnschrift', 30), 0, 10, 10)
                    draw_text(f'You are changing your username to "{cccccc}."', font25, 0, 10, 50)
                    if confirm_b.draw():
                        if 1 == 1:
                            list_of_users = real_load(f"data/users/@list_of_users.json")
                            list_of_users[list_of_users.index(username)] = (cccccc)
                            real_dump(list_of_users, (f"data/users/@list_of_users.json"))


                            os.rename(f"data/users/{username}", f"data/users/{cccccc}")
                            os.rename(f"data/unpack/{username}", f"data/unpack/{cccccc}")
                            username = cccccc
                            for i in os.listdir(f"data/users/{cccccc}"):
                                www = i.split("_", 1)
                                www[0] = ""
                                w = cccccc + "_" + ("".join(www))
                                os.rename(f"data/users/{cccccc}/" + i, f"data/users/{cccccc}/" + w)

                            for i in os.listdir(f"data/unpack/{cccccc}"):
                                www = i.split("_", 1)
                                www[0] = ""
                                w = cccccc + "_" + ("".join(www))
                                os.rename(f"data/unpack/{cccccc}/" + i, f"data/unpack/{cccccc}/" + w)
                                
                            real_dump(cccccc, (f"data/users/{cccccc}/{cccccc}_name.json"))


                            login(cccccc)
                            lobby_kick = []


                            lobby = [f'{username} (YOU)']

                            Audio(f'interact/state{random.randint(1, 3)}.wav')
                            menu_state = "main"

                            cuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                            cccccc = None
                        if 1==0:
                            Audio(f'interact/state{random.randint(1, 3)}.wav')
                            menu_state = "error login u"

                            cuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                            cccccc = None
            else:
                draw_text(f'Change your username!', pygame.font.SysFont('bahnschrift', 30), 0, 10, 10)
                draw_text(f'Type in the name you would like to use.', pygame.font.SysFont('bahnschrift', 20), 0, 10, 50)
                cccccc = cuser_type.update(10, 300, pygame.font.SysFont('bahnschrift', 40), 0)
                if len(cuser_type.str) >= 20:
                    sas = list(cuser_type.str)
                    for i in range(len(sas)-20):
                        sas[20+i] = ""
                    dffd = "".join(sas)
                    cuser_type.str = dffd
                bannedchars = [".", "/", "\\", "`", "@", "-", ":", "["]
                for ch in bannedchars:
                    cuser_type.str = cuser_type.str.replace(ch, "")
                if exit_b.draw():
                        cuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                        cccccc = None
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state =  "main"

    elif menu_state == "signup":
            #draw the different options buttons
            screen.fill((0, 0, 0))
            
            # if exit_b.draw():
            #     Audio(f'interact/state{random.randint(1, 3)}.wav')
            #     menu_state = "main"
            
            if newUserName != None:
                fusername = newUserName
                list_of_users = real_load(f"data/users/@list_of_users.json")
                if fusername in list_of_users:
                    if username != fusername:
                        draw_text(f'Sorry, but that username is unavailable.', font25, (255,0,0), 10, 10)
                        if exit_b.draw():
                            Audio(f'interact/state{random.randint(1, 3)}.wav')
                            user_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                            newUserName = None

                            pass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                            newPassWord = None
                            menu_state = "signup"

                    else:
                        draw_text(f'Account created.', font25, 0, 10, 10)
                        lobby = [f'{username} (YOU)']
                        
                        if exit_b.draw():
                            Audio(f'interact/state{random.randint(1, 3)}.wav')
                            user_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                            newUserName = None

                            pass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), 0, 10, 10, 100)
                            newPassWord = None
                            if username != fusername:
                                menu_state =  'signup'
                            else:
                                menu_state =  'main'
                

                    
                        
                else:
                    if newPassWord != None:
                        fassword = newPassWord
                        draw_text(f'You have created your account!', font25, 0, 10, 10)
                        logged_in_any = True
                        create_account(fusername, fassword)
                        if exit_b.draw():
                            Audio(f'interact/state{random.randint(1, 3)}.wav')
                            menu_state =  "main"
                        
                        
                    else:
                        draw_text(f'Username: {fusername}', pygame.font.SysFont('bahnschrift', 40), 0, 10, 600)
                        draw_text(f'Create a GRIDROYALE account today! We just need your username and password.', font25, 0, 10, 10)
                        draw_text(f'Type in the password you would like to use.', font25, 0, 10, 30)
                        newPassWord = pass_type.update(10, 300, pygame.font.SysFont('bahnschrift', 40), 0)

            else:
                draw_text(f'Create a GRIDROYALE account today! We just need your username and password.', font25, 0, 10, 10)
                draw_text(f'Type in the name you would like to use.', font25, 0, 10, 30)
                newUserName = user_type.update(10, 300, pygame.font.SysFont('bahnschrift', 40), 0)
                if len(user_type.str) >= 20:
                    sas = list(user_type.str)
                    for i in range(len(sas)-20):
                        sas[20+i] = ""
                    dffd = "".join(sas)
                    user_type.str = dffd
                bannedchars = [".", "/", "\\", "`", "@", "-", ":"]
                for ch in bannedchars:
                    user_type.str = user_type.str.replace(ch, "")
                if exit_b.draw():
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state =  "main"
                
    elif menu_state == "e1:login":
            #draw the different options buttons
            screen.fill((0, 0, 0))

            draw_text(f'Error, user "{username}" is already logged in.', pygame.font.SysFont('bahnschrift', 30), 0, 10, 10)

            if exit_b.draw():
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state =  "main"
                

    elif menu_state == "login":
            #draw the different options buttons
            screen.fill((0, 0, 0))

            list_of_users = real_load(f"data/users/@list_of_users.json")

 
            
            if (tryUserName != None):
                if tryPassWord != None:
                    list_of_users = real_load(f"data/users/@list_of_users.json")
                    if tryUserName in list_of_users:
                            if tryPassWord == real_load((f"data/users/{tryUserName}/{tryUserName}_pw.json")):
                                username = tryUserName
                                password = tryPassWord
                                locked_in = True
                                draw_text(f'Hello, {username}. You have logged in successfully.', font25, 0, 10, 10)
                                login(tryUserName)
                                logged_in_any = True
                                lobby = [f'{username} (YOU)']
                                lobby_kick = []

                                

                                if exit_b.draw():
                                    reroll_is()
                                    Audio(f'interact/state{random.randint(1, 3)}.wav')
                                    menu_state =  "main"
                                
                            else:
                                draw_text(f'Invalid password', font25, 0, 10, 10)
                                if exit_b.draw():
                                    Audio(f'interact/state{random.randint(1, 3)}.wav')
                                    menu_state =  "main"
                                    user_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    newUserName = None

                                    pass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    newPassWord = None

                                    trypass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    tryUserName = None

                                    tryuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    tryPassWord = None 
                                
                                
                    else:
                        draw_text(f'Username nonexistent. Perhaps a spelling error?', pygame.font.SysFont('bahnschrift', 15), 0, 10, 10)
                        if exit_b.draw():
                                    Audio(f'interact/state{random.randint(1, 3)}.wav')
                                    menu_state =  "main"
                                    user_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    newUserName = None

                                    pass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    newPassWord = None

                                    trypass_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    tryUserName = None

                                    tryuser_type = TrashInput('', pygame.font.SysFont("bahnschrift", 22), ('white'), 10, 10, 100)
                                    tryPassWord = None
                        

                else:
                    draw_text(f'Login: Type in your password.', font25, 0, 10, 10)
                    tryPassWord = trypass_type.update(10, 300, pygame.font.SysFont('bahnschrift', 40), 0)
                    if exit_b.draw():
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state =  "main"
                    
                    
            else:
                draw_text(f'Login: Type in your username.', font25, 0, 10, 10)
                tryUserName = tryuser_type.update(10, 300, pygame.font.SysFont('bahnschrift', 40), 0)
                if exit_b.draw():
                        Audio(f'interact/state{random.randint(1, 3)}.wav')
                        menu_state =  "main"
                if tryUserName == username:
                    menu_state =  "e1:login"
                

    for tinp in tinps:
                    if tinp.updating:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_BACKSPACE]:
                                if bsco <= 0:
                                    tinp.str = tinp.str[:-1]
                                    bsco = 10
                                else:
                                    bsco -= 1

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks.append(joy)
                if menu_state != "game":
                    # if contr == 0:
                        menu_state = "controller"

      
            
            if event.type == pygame.MOUSEBUTTONUP:
                if menu_state == "battle pass":
                    if event.button == 4:
                            bptx += 35
                    if event.button == 5:
                            bptx -= 35

                if menu_state == "new lvls":
                    if event.button == 4:
                            bptx += 35
                    if event.button == 5:
                            bptx -= 35

                if menu_state == "friends":
                    if event.button == 4:
                            friendy += 35
                    if event.button == 5:
                            friendy -= 35
                
                if menu_state == "bought":
                    if event.button == 4:
                            boux += 35
                    if event.button == 5:
                            boux -= 35

                if menu_state in types_of_customization:
                    if event.button == 4:
                            customy += 35
                    if event.button == 5:
                            customy -= 35
            
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                
                
                for tinp in tinps:
                    if tinp.updating:                        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                    pass
                            #     tinp.str = tinp.str[:-1]
                            elif event.key == pygame.K_RETURN:
                                tinp.returned = True

                            else:
                                if not event.key == pygame.K_SLASH or pygame.K_BACKSLASH:
                                    tinp.str += event.unicode

    if not (menu_state in ["new season", "bought it"]):
        ed=BLACK
        if menu_state == "buy bp":
            ed=WHITE
        if prems == 1:
            draw_text(f'You have {prems} Prem.', font35, 0, 10, HEIGHT - 40, color=ed)
        else: draw_text(f'You have {prems} Prems.', font35, 0, 10, HEIGHT - 40, color=ed)
    g.jdt = 1

    if rp > max_rp:
        max_rp = rp

    if bptx > 0:
        bptx = 0
    if boux > 0: boux = 0
    if customy > 0:
        customy = 0
    if friendy > 0:
        friendy = 0
    if bptx < -(len(lvl_grants)*100):
        bptx = -(len(lvl_grants)*100)

    if (not menu_state.__contains__('login')) and menu_state != "signup" and menu_state != "buy bp" and (not (menu_state in ["new season", "bought it", "cuser", "cpass", "error login u", "is", "bought"])): logo.draw()
    auto_save(username)
    pygame.display.update()
    
    clock.tick(120)
    