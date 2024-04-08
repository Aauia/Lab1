import pygame
from menu import *
import random


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1200, 800
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'fonts/NotoSansKhojki-Regular.ttf'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        W, H = 1200, 800
        FPS = 60
        screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        done = False
        bg = (0, 0, 0)


        paddleW = 150
        paddleH = 25
        paddleSpeed = 20
        paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


        ballRadius = 20
        ballSpeed = 6
        ball_rect = int(ballRadius * 2 ** 0.5)
        ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
        dx, dy = 1, 1  


        game_score = 0
        game_score_fonts = pygame.font.SysFont('comicsansms', 40)
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        game_score_rect = game_score_text.get_rect()
        game_score_rect.center = (210, 20)


        collision_sound = pygame.mixer.Sound('sound/catch.mp3')

        def detect_collision(dx, dy, ball, rect):
            if dx > 0:
                delta_x = ball.right - rect.left
            else:
                delta_x = rect.right - ball.left
            if dy > 0:
                delta_y = ball.bottom - rect.top
            else:
                delta_y = rect.bottom - ball.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = -dx, -dy
            if delta_x > delta_y:
                dy = -dy
            elif delta_y > delta_x:
                dx = -dx
            return dx, dy

        block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
        color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)] 


        is_breakable = [True] * len(block_list)

        # ex 2: unbreakable bricks 
        unbreakable_indices = [i for i in range(len(block_list)) if i % 5 == 0][:3]  
        unbreakable_hits = [0] * len(unbreakable_indices) 
        for i in unbreakable_indices:
            is_breakable[i] = False

        # ex 5 : Create bonus bricks
        class BonusBrick:
            def __init__(self, rect):
                self.rect = rect
                self.color = (255, 255, 255) 
                self.sign = 'A'  
                self.bonus_points = 50 

        # ex 5 : Create bonus bricks
        bonus_brick_list = [BonusBrick(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)) for i in range(10) for j in range(4)][2:5]  # First 3 bonus bricks

        # ex 5 : Create bonus brickss
        def handle_bonus_brick_collision(ball, bonus_brick_list):
            global game_score  
            for bonus_brick in bonus_brick_list:
                if bonus_brick.rect.colliderect(ball):
                    bonus_brick_list.remove(bonus_brick)  
                    game_score += bonus_brick.bonus_points 


        losefont = pygame.font.SysFont('comicsansms', 40)
        losetext = losefont.render('Game Over', True, (255, 255, 255))
        losetextRect = losetext.get_rect()
        losetextRect.center = (W // 2, H // 2)

        # ex 3 : Increase the speed of a ball with time 
        start_time = pygame.time.get_ticks() 
        timer_font = pygame.font.SysFont('comicsansms', 30)


        winfont = pygame.font.SysFont('comicsansms', 40)
        wintext = winfont.render('You win yay', True, (0, 0, 0))
        wintextRect = wintext.get_rect()
        wintextRect.center = (W // 2, H // 2)


        font = pygame.font.SysFont(None, 30)
        # ex 4 : shrinking paddle over time 
        shrinking_rate = 0.01  
        initial_paddle_width = paddleW
        time_elapsed = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill(bg)
    
            # Drawing blocks
            for i, block in enumerate(block_list):
                if is_breakable[i]:
                    pygame.draw.rect(screen, color_list[i], block)
                # ex 2 : Create unbreakable bricks;
                else:
                    pygame.draw.rect(screen, (255, 255, 0), block)  # Yellow color for unbreakable blocks
                    text = font.render('B', True, (0, 0, 0))
                    text_rect = text.get_rect(center=block.center)
                    screen.blit(text, text_rect)

            # ex 5 : Create bonus bricks
            for bonus_brick in bonus_brick_list:
                pygame.draw.rect(screen, bonus_brick.color, bonus_brick.rect)
                text = font.render(bonus_brick.sign, True, (0, 0, 0))
                text_rect = text.get_rect(center=bonus_brick.rect.center)
                screen.blit(text, text_rect)

            pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
            pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

   
            ball.x += ballSpeed * dx
            ball.y += ballSpeed * dy

  
            if ball.left <= 0 or ball.right >= W:
                dx = -dx
            if ball.top <= 0:
                dy = -dy
            if ball.colliderect(paddle):
                dx, dy = detect_collision(dx, dy, ball, paddle)
                ball.bottom = paddle.top - 1

    
            hitIndex = ball.collidelist(block_list)
            if hitIndex != -1:
                hitRect = block_list[hitIndex]
                if is_breakable[hitIndex]:
                    block_list.pop(hitIndex)
                    dx, dy = detect_collision(dx, dy, ball, hitRect)
                    game_score += 1
                    collision_sound.play()
        # ex 2 : unbreakable breaks 
                else:
           
                    unbreakable_hit_index = unbreakable_indices.index(hitIndex)
                    unbreakable_hits[unbreakable_hit_index] += 1
                    if unbreakable_hits[unbreakable_hit_index] >= 2:
                        block_list.pop(hitIndex)
                        del unbreakable_hits[unbreakable_hit_index]
                        del unbreakable_indices[unbreakable_hit_index]
                        is_breakable[hitIndex] = True  
                    dx, dy = detect_collision(dx, dy, ball, hitRect)

    # ex 5 : bonus break
            handle_bonus_brick_collision(ball, bonus_brick_list)

            # Game score
            game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
            screen.blit(game_score_text, game_score_rect)
            # ex 4 : shrinking paddle over time 
            dt = clock.get_time() / 1000  
            time_elapsed += dt
            if time_elapsed >= 1:  
                time_elapsed -= 1
                paddleW = max(initial_paddle_width * (1 - shrinking_rate * elapsed_time), 50)  
                paddle.width = paddleW
                paddle.x = min(max(paddle.x, 0), W - paddleW)  


        # ex 3 : Increase the speed of a ball with time 
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - start_time) // 1000  
# ex 3 : Increase the speed of a ball with time 
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            timer_text = timer_font.render(f'Time: {minutes:02}:{seconds:02}', True, (255, 255, 255))

            # Win/lose screens
            if ball.bottom > H:
                screen.fill((0, 0, 0))
                screen.blit(losetext, losetextRect)
            elif not len(block_list):
                    screen.fill((255, 255, 255))
                    screen.blit(wintext, wintextRect)
    # ex 3 : Increase the speed of a ball with time 
            else:
                screen.blit(timer_text, (600, 10)) 
                ballSpeed += 0.005
   
            pygame.display.update()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and paddle.left > 0:
                paddle.left -= paddleSpeed
            if key[pygame.K_RIGHT] and paddle.right < W:
                paddle.right += paddleSpeed

            clock.tick(FPS)




    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)




