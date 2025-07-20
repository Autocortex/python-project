import pygame
import sys

from settings import Settings
from player import Player
from target import Target
from bullet import Bullet
from button import Button
from game_stats import GameStats
from button_difficulty import ButtonDifficulty

class AimMaster():

    def __init__(self):
        """Initial resourse for AimMaster."""
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption('Aim Master')
        self.player = Player(self)
        self.target = Target(self)
        self.play_button = Button(self, 'Play')
        self.easy_button = ButtonDifficulty(self)
        self.easy_button.difficulty_easy('Easy')
        self.hard_button = ButtonDifficulty(self)
        self.hard_button.difficulty_hard('Hard')
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Run game."""
        while True:
            self._check_events()
            if self.stats.game_active == True:
                self.player.update()
                self.target.update()
                self._bullets_update()
                self._check_active_game()
            self._update_screen()

    def _check_events(self):
        """Check events keyboard or mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_menu_buttons(mouse_pos)

    def _check_menu_buttons(self, mouse_pos):
        """Start game and choise difficulty."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
        elif self.easy_button.rect.collidepoint(mouse_pos):
            self.settings.easy_difficulty()
            self.stats.game_active = True
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.hard_difficulty()
            self.stats.game_active = True

    def _check_events_keydown(self, event):
        """Check events keydown."""
        if event.key == pygame.K_w:
            self.player.moving_top = True
        elif event.key == pygame.K_s:
            self.player.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_events_keyup(self, event):
        """Check events keyup."""
        if event.key == pygame.K_w:
            self.player.moving_top = False
        elif event.key == pygame.K_s:
            self.player.moving_bottom = False

    def _fire_bullet(self):
        """Fire bullet."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _bullets_update(self):
        """Update bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen.get_rect().right:
                self.stats.available_miss_counter -= 1
                self.bullets.remove(bullet)
            self._count_collisions(bullet)

    def _check_active_game(self):
        """Check active game."""
        if self.stats.available_miss_counter <= 0:
            self.stats.game_active = False
            self.stats.reset_stats()

    def _count_collisions(self, bullet):
        """Count collisions bullets with target."""
        if pygame.sprite.collide_rect(self.target, bullet):
            self.stats.count_collisions += 1
            self.bullets.remove(bullet)
            self._increasing_game_difficulty()

    def _increasing_game_difficulty(self):
        """Increasing game difficulty."""
        count = self.stats.count_collisions
        if count > 0 and count % 3 == 0 and count != self.settings.last_difficulty_trigger:
            self.settings. increase_speed()
            self.settings.last_difficulty_trigger = count

    def _update_screen(self):
        """Update screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.hard_button.draw_button()
        self.target.blittarget()
        pygame.display.flip()

if __name__ == '__main__':
    am = AimMaster()
    am.run_game()
