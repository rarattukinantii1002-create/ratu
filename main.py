import pgzrun
import random

# Dimensi Layar
WIDTH = 800
HEIGHT = 400

# Variabel Pemain (Karakter Jumper)
jumper = Actor('hero')  # Gambar hero.png
jumper.x = 100
jumper.y = 300
vy = 0                  # Kecepatan vertikal (y-velocity)
GRAVITY = 0.8           # Logika gravitasi Scratch

# Variabel Rintangan
obstacle = Actor('obstacle')  # Gambar obstacle.png
obstacle.x = 800
obstacle.y = 330
obstacle_speed = 5

# Variabel Game State & Skor
score = 0
game_over = False

def draw():
    """Merender tampilan ke layar (Sama seperti Tampilan Stage Scratch)"""
    screen.clear()
    screen.fill((135, 206, 235))  # Warna latar langit biru
    
    # Gambar tanah
    screen.draw.filled_rect(Rect((0, 350), (800, 50)), (34, 139, 34))
    
    # Gambar elemen game
    jumper.draw()
    obstacle.draw()
    
    # Menampilkan Skor
    screen.draw.text(f"Skor: {score}", (20, 20), fontsize=35, color="white")
    
    if game_over:
        screen.draw.text("GAME OVER!", center=(400, 180), fontsize=60, color="red")
        screen.draw.text("Tekan SPASI untuk Ulang", center=(400, 230), fontsize=30, color="black")

def update():
    """Fungsi ini berjalan terus-menerus (Sama seperti blok 'Forever' Scratch)"""
    global vy, score, game_over, obstacle_speed
    
    if not game_over:
        # 1. LOGIKA GRAVITASI (Pemain jatuh ke bawah)
        vy += GRAVITY
        jumper.y += vy
        
        # Batas Tanah (Pemain tidak tembus tanah)
        if jumper.y >= 300:
            jumper.y = 300
            vy = 0
            
        # 2. LOGIKA RINTANGAN (Gerak ke kiri)
        obstacle.x -= obstacle_speed
        
        # Reset posisi rintangan jika keluar layar kiri
        if obstacle.x < -20:
            obstacle.x = 800
            score += 1
            obstacle_speed += 0.2  # Game makin lama makin cepat!
            
        # 3. DETEKSI TABRAKAN (Sama seperti 'touching sprite?' di Scratch)
        if jumper.colliderect(obstacle):
            game_over = True

def on_key_down(key):
    """Event saat tombol keyboard ditekan (Sama seperti 'When key pressed')"""
    global vy, game_over, score, obstacle_speed
    
    # Lompat jika menekan Spasi dan pemain sedang di tanah
    if key == keys.SPACE and jumper.y == 300 and not game_over:
        vy = -14  # Memberi dorongan ke atas
        
    # Restart Game jika Game Over
    if key == keys.SPACE and game_over:
        game_over = False
        score = 0
        obstacle_speed = 5
        obstacle.x = 800
        jumper.y = 300

pgzrun.go()
