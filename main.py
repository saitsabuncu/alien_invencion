import sys
import pygame

def initialize_game():
    """
    Oyunu başlat ve ekran ile diğer kaynakları oluştur.
    """
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    return screen, bg_color

def check_events():
    """
    Klavye ve fare olaylarını kontrol et.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, bg_color):
    """
    Ekranı her döngüde yeniden çizdir ve güncelle.
    """
    screen.fill(bg_color)
    pygame.display.flip()

def run_game():
    """
    Oyunun ana döngüsünü çalıştır.
    """
    screen, bg_color = initialize_game()

    while True:
        check_events()
        update_screen(screen, bg_color)

if __name__ == '__main__':
    run_game()
