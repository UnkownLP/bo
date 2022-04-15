def on_button_pressed_a():
    Player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Shoot
    Shoot = game.create_sprite(Player.get(LedSpriteProperty.X),
        Player.get(LedSpriteProperty.Y))
    Shoot.set(LedSpriteProperty.BRIGHTNESS, 100)
    for index in range(4):
        Shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
        if Shoot.is_touching(Enemy):
            game.add_score(1)
        if Shoot.get(LedSpriteProperty.Y) <= 0:
            Shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

EnemyFire: game.LedSprite = None
Shoot: game.LedSprite = None
Enemy: game.LedSprite = None
Player: game.LedSprite = None
game.set_life(4)
game.set_score(0)
Player = game.create_sprite(2, 4)
Enemy = game.create_sprite(0, -4)

def on_forever():
    global EnemyFire
    Enemy.move(1)
    basic.pause(100)
    Enemy.if_on_edge_bounce()
    EnemyFire = game.create_sprite(Enemy.get(LedSpriteProperty.X),
        Enemy.get(LedSpriteProperty.Y))
    EnemyFire.set(LedSpriteProperty.BRIGHTNESS, 100)
    for index2 in range(4):
        EnemyFire.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
        if EnemyFire.is_touching(Player):
            game.remove_life(1)
        if EnemyFire.get(LedSpriteProperty.Y) >= 4:
            EnemyFire.delete()
basic.forever(on_forever)
