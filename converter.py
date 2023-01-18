import cv2
import pygame
from sys import exit
            
class ArtConverter:
    # fps won't be decreasing while font size bigger than 12.
    def __init__(self, surface: pygame.Surface, path , font_size = 12):
        self.surface = surface
        self.path = path
        self.loader = cv2.VideoCapture(self.path)
        self.fps = self.loader.get(cv2.CAP_PROP_FPS)
        
        self.font = pygame.font.SysFont("Arial", font_size, True)
        self.step = int(font_size * 0.7)
        
        self.asciis = " ixzao*#MW&8%B@&"
        self.ascii_range = 255 // (len(self.asciis) - 1)
    
    def convertion(self):
        image_data = []
        for x in range(0, len(self.image[0]), self.step):
            for y in range(0, len(self.image), self.step):
                image_data.append((self.image[y][x][::-1], self.gray_image[y][x], (x, y)))
        return image_data
    
    def load_video(self):
        loading, self.image = self.loader.read()
        if not loading:
            return
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) // self.ascii_range
        self.draw()

    def draw(self):
        image_data = self.convertion()
        for rgb_value, gray_value, (x, y) in image_data:
            text = self.asciis[gray_value]
            self.surface.blit(self.font.render(text, True, rgb_value), (x, y))
    
class Displayer:
    def __init__(self, path, font_size):
        pygame.init()
        self.surface = pygame.display.set_mode((1280, 800))
        self.clock = pygame.time.Clock()
        self.converter = ArtConverter(self.surface, path, font_size)
        
    def run(self):
        while True:
            self.surface.fill((0, 0, 0, 0))
            
            self.check_event()
            self.converter.load_video()
            
            self.clock.tick(self.converter.fps)
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.update()
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
if __name__ == "__main__":
    displayer = Displayer()
    displayer.run()
