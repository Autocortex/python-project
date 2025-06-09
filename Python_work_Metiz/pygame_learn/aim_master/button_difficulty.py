import pygame.font

class ButtonDifficulty():

    def __init__(self, aimmaster):
        """Initial resourses for class button"""
        self.screen = aimmaster.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (211,211,211)
        self.text_color = (45,41,38)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0,0, self.width, self.height)

    def difficulty_easy(self,msg):
        """Easy difficulty button rect."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - self.height - 5
        self.prep_msg(msg)

    def difficulty_hard(self, msg):
        """Easy difficulty button rect."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - (2 * self.height) - 10
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Converts msg to rectangle, aligns text to center."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw button"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)