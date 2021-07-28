import pygame
import random
import os
import sys
from pygame import mixer

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Açılan oyun ekranını ortalama
pygame.font.init()

## Oyundaki Sekiller ####
S = [['.....',
      '.....',  # __
      '..00.',  # |
      '.00..',  # __|
      '.....'],
     ['.....',
      '..0..',  # |
      '..00.',  # |__
      '...0.',  # |
      '.....'],
     ['.....',
      '.....',  # __
      '.00..',  # |
      '..00.',  # |__
      '.....'],
     ['.....',
      '...0.',  # |
      '..00.',  # __|
      '..0..',  # |
      '.....']
     ]              ##
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']
     ]              ##
O = [['.....',
      '..00.',
      '..00.',
      '.....',
      '.....']
     ]              ##
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']
     ]              ##
T = [['.....',
      '..0..',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '.0...',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.000.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '...0.',
      '.000.',
      '...0.',
      '.....']
     ]              ##
Diktortgen = [['.....',
               '00000',
               '00000',
               '00000',
               '.....'],
              ['000..',
               '000..',
               '000..',
               '000.',
               '000..']
              ]     ##
i = [['..0..',
      '.....',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '000.0',
      '.....',
      '.....'],
     ['..0.',
      '..0..',
      '..0..',
      '.....',
      '..0..'],
     ['.....',
      '.....',
      '0.000',
      '.....',
      '.....']
     ]              ##
H = [['.....',
      '.000.',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '.0.0.',
      '.000.',
      '.0.0.',
      '.....']
     ]              ##
U = [['.....',
      '.000.',
      '...0.',
      '.000.',
      '.....'],
     ['.....',
      '.0.0.',
      '.0.0.',
      '.000',
      '.....'],
     ['.....',
      '.000.',
      '.0...',
      '.000',
      '.....'],
     ['.....',
      '.000.',
      '.0.0.',
      '.0.0.',
      '.....']
     ]              ##
Y = [['.....',
      '.0.0.',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..00.',
      '.00..',
      '..00',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '.0.0',
      '.....'],
     ['.....',
      '.00..',
      '..00.',
      '.00..',
      '.....']
     ]              ##
M = [['.....',
      '0.0.0',
      '0.0.0',
      '00000',
      '.....'],
     ['.000.',
      '...0.',
      '.000.',
      '...0',
      '.000.'],
     ['.....',
      '00000',
      '0.0.0',
      '0.0.0',
      '.....'],
     ['.000.',
      '.0...',
      '.000.',
      '.0..',
      '.000.'],
     ]              ##
#########################

############################ Ekran ve Oyun Büyüklükleri ##############################################
ekran_genislik = 800  # Ekran'ın x düzlemi uzunlugu                                                 ##
ekran_yükseklik = 700  # Ekran'ın y düzlemi uzunlugu                                                ##
                                                                                                    ##
oyun_genislik = 420  # Oyun'un  x düzlemi uzunlugu                                                  ##
oyun_yükseklik = 600  # Oyun'un  y düzlemi uzunlugu                                                 ##
                                                                                                    ##
oyun_x_düzlemi = (ekran_genislik - oyun_genislik) // 2  # Oyun'un tam x düzlemi                     ##
oyun_y_düzlemi = ekran_yükseklik - oyun_yükseklik - 30  # Oyun'un tam y düzlemi                     ##
                                                                                                    ##
blok_boyut = 30  # 300//30 x uzunlugu, 600//30 y uzunlugu                                           ##
######################################################################################################

sekiller = [S, I, O, L, T, i, H, U, Y, M, Diktortgen]
sekil_renkleri = [(255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128), (139,0,0),(255,215,0), (0,100,0), (238,130,238), (30,144,255)]

# Tek tek kutucuklar olusturma.
class Parca(object):
    def __init__(self, x, y, sekil):
        self.x = x
        self.y = y
        self.sekil = sekil
        self.color = sekil_renkleri[sekiller.index(sekil)]
        self.donme = 0

# Oyun alanini burada matrisler gibi olusturuyorum.
def oyun_alanı_olusturma(disina_cikilmayan_alan_Gozuken={}):
    alan = [[(0, 0, 0) for k in range(14)] for k in range(20)]
    for i in range(len(alan)):
        for j in range(len(alan[i])):
            if (j, i) in disina_cikilmayan_alan_Gozuken:
                alan[i][j] = disina_cikilmayan_alan_Gozuken[(j, i)]
    return alan

# Oyun Alanı'nın Kullanılabilinir Alanı'nı olusturuyorum.Kullanabilirden kasit gelen sekillerin hareket edebilecegi maksimum kutu sayisi.
def gecerli_alan(sekil, alan):
    disina_cikilmayan_alan_Gozukmeyen = [[(j, i) for j in range(14) if alan[i][j] == (0, 0, 0)] for i in range(20)]
    disina_cikilmayan_alan_Gozukmeyen = [j for x in disina_cikilmayan_alan_Gozukmeyen for j in x]

    format_Edildi = seklin_yonunu_degistirme(sekil)
    for merkez in format_Edildi:
        if merkez not in disina_cikilmayan_alan_Gozukmeyen and merkez[1] > -1:
            return False
    return True

# Oyundaki şekillerin yön tuşları ile değiştirmemizi sağlayan fonksiyon
def seklin_yonunu_degistirme(sekil):
    konum = []
    yon = sekil.sekil[sekil.donme % len(sekil.sekil)]
    for i, line in enumerate(yon):
        satir = list(line)
        for j, column in enumerate(satir):
            if column == '0':
                konum.append((sekil.x + j, sekil.y + i))
    for i, pos in enumerate(konum):
        konum[i] = (pos[0] - 2, pos[1] - 4)
    return konum

# Sekillerin ust uste gelip tavana ulastimi diye kontrol edilen fonksiyon
def oyunu_Kaybetme_Kontrol(konum):
    for kon in konum:
        x, y = kon
        if y < 1:
            return True
    return False

# Random sekil yukaridan getiren fonksiyon
def random_Sekil():
    return Parca(7, 0, random.choice(sekiller))

# Oyunu Kaybettigimiz Zaman Gelen Ekran Fonksiyonu
def kaybettiniz(ekran):
    pic = pygame.image.load("game_over.jpg")
    ekran.blit(pygame.transform.scale(pic, (800, 875)), (0, 0))
    pygame.display.update()
    pygame.time.delay(1500)
    ana_menu(win)

# Oyun Alaninin Cizgilerini Olusturdugum Fonksiyon
def alan_Cizgileri(ekran, alan):
    alan_x = oyun_x_düzlemi
    alan_y = oyun_y_düzlemi

    for i in range(len(alan)):
        pygame.draw.line(ekran, (139,0,139), (alan_x, alan_y + i * blok_boyut), (alan_x + oyun_genislik, alan_y + i * blok_boyut))
        for j in range(len(alan[i])):
            pygame.draw.line(ekran, (139,0,139), (alan_x + j * blok_boyut, alan_y),(alan_x + j * blok_boyut, alan_y +  oyun_yükseklik))

# Puan Kazandigimiz zaman skorun artmasini ve o satirin silinmesini saglayan fonksiyon
def satir_Sil(alan, locked):
    skor = 0
    for i in range(len(alan) - 1, -1, -1):
        row = alan[i]
        if (0, 0, 0) not in row:
            skor += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if skor > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                yeni_Anahtar = (x, y + skor)
                locked[yeni_Anahtar] = locked.pop(key)
    return skor

# Sonraki Sekili Yan Tarafta Onizleme Olarak Gostermemizi Saglayan Fonksiyon
def sonraki_Sekili_Ciz(sekil, ekran):
    alan_x = oyun_x_düzlemi + oyun_genislik + 20
    alan_y = oyun_y_düzlemi + oyun_yükseklik / 2 - 100
    format = sekil.sekil[sekil.donme % len(sekil.sekil)]

    a = 0
    if a == 0:
        pic = pygame.image.load("Sekil_Arkaplan.jpg")
        win.blit(pygame.transform.scale(pic, (170, 170)), (alan_x-10, alan_y-10))
        a = a + 1

    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Sıradaki Şekil', 1, (0, 255, 0))

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(ekran, sekil.color,(alan_x + j * blok_boyut, alan_y + i * blok_boyut, blok_boyut, blok_boyut), 0)
    ekran.blit(label, (alan_x + 10, alan_y - 40 ))

# Yatay kutucuklar tamamlandiginda skoru guncelleyen fonksiyon
def skoru_Guncelle(nskor):
    skor = max_Skor()

    with open('scores.txt', 'w') as file:
        if int(skor) > nskor:
            file.write(str(skor))
        else:
            file.write(str(nskor))
    file.close()

# Max Skoru Getiren Fonksiyon(Ayrı bir fonksiyon yapmamaın sebebi her defasında dosya okumayarak oyunu yavaşlatmamak)
def max_Skor():
    with open('scores.txt', 'r') as file:
        lines = file.readlines()
        skor = lines[0].strip()
    file.close()
    return skor

# Oyun Ekraninin Arkaplan,Skor vb. Bilgilerinin Girildigi Fonksiyon
def oyun_Ekrani(ekran, alan, skor=0, rekor=0):
    ekran.fill((0, 0, 0))
    pygame.font.init()
    a=0
    if a==0:
        pic = pygame.image.load("Arkaplan.jpg")
        ekran.blit(pygame.transform.scale(pic, (1000, 1000)), (0, 0))
        a=a+1

    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Legendary Tetris  ', 1, (255,99,71))
    ekran.blit(label, (oyun_x_düzlemi + oyun_genislik / 2 - (label.get_width() / 2), 10))

    font = pygame.font.SysFont('comicsans', 30)
    
    label = font.render('Skor:   ' + str(skor)+'   Puan', 1, (0, 255, 0))
    alan_x = oyun_x_düzlemi - 160
    alan_y = oyun_y_düzlemi + 230
    ekran.blit(label, (alan_x, alan_y))

    label = font.render('Rekor: ' + rekor + ' Puan', 1, (135, 206, 235))
    alan_x = oyun_x_düzlemi - 180
    alan_y = oyun_y_düzlemi + 120
    ekran.blit(label, (alan_x + 20, alan_y + 160))

    for i in range(len(alan)):
        for j in range(len(alan[i])):
            pygame.draw.rect(ekran, alan[i][j],(oyun_x_düzlemi + j * blok_boyut, oyun_y_düzlemi + i * blok_boyut, blok_boyut, blok_boyut),0)
            
    pygame.draw.rect(ekran, (255, 0, 0), (oyun_x_düzlemi, oyun_y_düzlemi, oyun_genislik, oyun_yükseklik), 5)
    alan_Cizgileri(ekran, alan)

# Menu Ekraninin Arkaplan,Skor vb. Bilgilerinin Girildigi Fonksiyon
def ana_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        a = 0
        if a == 0:
            pic = pygame.image.load("Arkaplan.jpg")
            pic1 = pygame.image.load("Buton.png")
            pic2 = pygame.image.load("puan.jpg")
            pic3= pygame.image.load("Yon_Tuslari.png")
            pic4 = pygame.image.load("Space_Tusu.png")
            win.blit(pygame.transform.scale(pic, (1000, 1000)), (0, 0))
            win.blit(pygame.transform.scale(pic1, (650, 100)), (80, 320))
            win.blit(pygame.transform.scale(pic2, (130, 50)), (520, 530))
            win.blit(pygame.transform.scale(pic3, (200, 100)), (120, 470))
            win.blit(pygame.transform.scale(pic4, (200, 60)), (120, 570))
            a=a+1

        font = pygame.font.SysFont("Helvetica", 30, bold=True)
        font1 = pygame.font.SysFont("courier", 110, bold=True)
        font2 = pygame.font.SysFont("tahoma", 30, bold=True)

        label = font.render('Rekor:  ', 1, (255, 99, 71))
        label1 = font.render(max_Skor(), 1, (255,215,0))
        alan_x = oyun_x_düzlemi +120
        alan_y = oyun_y_düzlemi + 280
        win.blit(label, (alan_x +220, alan_y + 185))
        win.blit(label1, (alan_x + 300, alan_y + 187))

        basla = font.render("Başlamak İçin Bir Tuşa Basınız", 1, (0, 0, 0))
        isim1 = font1.render("LEGENDARY", 1, (255, 99, 71))
        isim2 = font1.render("TETRIS", 1, (255, 215, 0))
        imza = font2.render("devoloped by ATİX                                              2020", 2, (224, 255, 255))

        win.blit(basla, (oyun_x_düzlemi + oyun_genislik / 2 - (basla.get_width() / 2),oyun_y_düzlemi + oyun_yükseklik / 2 - (basla.get_height() / 2)))
        win.blit(isim1, (oyun_x_düzlemi + oyun_genislik - 300 - (basla.get_width() / 2), oyun_y_düzlemi + 20 - (basla.get_height() / 2)))
        win.blit(isim2, (oyun_x_düzlemi + oyun_genislik - 205 - (basla.get_width() / 2), oyun_y_düzlemi + 90 - (basla.get_height() / 2)))
        win.blit(imza, (oyun_x_düzlemi + oyun_genislik - 410 - (basla.get_width() / 2), oyun_y_düzlemi + 600 - (basla.get_height() / 2)))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mixer.quit()
                sys.exit(0)
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    mixer.quit()
                    sys.exit(0)
                    pygame.quit()
                else:
                    main(win)

    pygame.display.quit()

# Şekilleri hareket ettirmemize saglayan genel sinif
def main(win):
    pygame.mixer.init()
    mixer.music.load("Tetris_Muzik.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.4)

    rekor = max_Skor()
    disina_cikilmayan_alan_Gozuken = {}

    degistirilebilinir_Parca = False
    run = True
    anlik_Parca = random_Sekil()
    sonraki_Parca = random_Sekil()
    clock = pygame.time.Clock()
    düsme_Zamani = 0
    düsme_Hizi = 0.25
    level_Hizi = 0
    skor = 0
    while run:
        alan = oyun_alanı_olusturma(disina_cikilmayan_alan_Gozuken)
        düsme_Zamani += clock.get_rawtime()
        level_Hizi += clock.get_rawtime()
        clock.tick()

        if level_Hizi / 1000 > 5:
            level_Hizi = 0
            if level_Hizi > 0.12:
                level_Hizi -= 0.005

        if düsme_Zamani / 1000 > düsme_Hizi:
            düsme_Zamani = 0
            anlik_Parca.y += 1
            if not (gecerli_alan(anlik_Parca, alan)) and anlik_Parca.y > 0:
                anlik_Parca.y -= 1
                degistirilebilinir_Parca = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    anlik_Parca.x -= 1
                    if not (gecerli_alan(anlik_Parca, alan)):
                        anlik_Parca.x += 1
                if event.key == pygame.K_RIGHT:
                    anlik_Parca.x += 1
                    if not (gecerli_alan(anlik_Parca, alan)):
                        anlik_Parca.x -= 1
                if event.key == pygame.K_DOWN:
                    anlik_Parca.y += 1
                    if not (gecerli_alan(anlik_Parca, alan)):
                        anlik_Parca.y -= 1
                if event.key == pygame.K_UP:
                    anlik_Parca.donme += 1
                    if not (gecerli_alan(anlik_Parca, alan)):
                        anlik_Parca.donme -= 1
                if event.key == pygame.K_SPACE:
                    anlik_Parca.y += 5
                    if not (gecerli_alan(anlik_Parca, alan)):
                        anlik_Parca.y -= 5
                if event.key == pygame.K_ESCAPE:
                    mixer.quit()
                    sys.exit(0)
                    pygame.quit()

        sekil_pos = seklin_yonunu_degistirme(anlik_Parca)

        for i in range(len(sekil_pos)):
            x, y = sekil_pos[i]
            if y > -1:
                alan[y][x] = anlik_Parca.color

        if degistirilebilinir_Parca:
            for pos in sekil_pos:
                p = (pos[0], pos[1])
                disina_cikilmayan_alan_Gozuken[p] = anlik_Parca.color
            anlik_Parca = sonraki_Parca
            sonraki_Parca = random_Sekil()
            degistirilebilinir_Parca = False
            skor += satir_Sil(alan, disina_cikilmayan_alan_Gozuken) * 10

        oyun_Ekrani(win, alan, skor, rekor)
        sonraki_Sekili_Ciz(sonraki_Parca, win)
        pygame.display.update()

        if oyunu_Kaybetme_Kontrol(disina_cikilmayan_alan_Gozuken):
            skoru_Guncelle(skor)
            run = False
            kaybettiniz(win)

win = pygame.display.set_mode((ekran_genislik, ekran_yükseklik))
pygame.display.set_caption('Legendary Tetris')
ana_menu(win)

mixer.quit()
sys.exit(0)
pygame.quit()