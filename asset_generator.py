"""Program Name: Neon Defender Asset Generator
Author: Xavier Chitison
Purpose: Generate original Track 2 ship, backdrop, laser and sound assets.
Starter Code Links: https://github.com/XavierChitison/alien_Invasion_starter
Date Updated: 2026-11-13
"""
from pathlib import Path
from array import array
import math
import random
import wave
import pygame

ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "Assets" / "images"
SOUNDS = ROOT / "Assets" / "sound"
REQUIRED_ASSETS = (
    IMAGES / "neon_ship.png",
    IMAGES / "neon_laser.png",
    IMAGES / "neon_background.png",
    SOUNDS / "neon_laser.wav",
)


def generate_assets(force=False):
    """Build original neon-themed images and a synthesized laser WAV file.

    Existing custom files are kept unless a regeneration is explicitly forced.
    """
    IMAGES.mkdir(parents=True, exist_ok=True)
    SOUNDS.mkdir(parents=True, exist_ok=True)
    if not force and all(path.exists() for path in REQUIRED_ASSETS):
        return

    pygame.init()

    ship = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.polygon(ship, (15, 30, 55), [(50, 3), (92, 91), (50, 70), (8, 91)])
    pygame.draw.polygon(ship, (0, 230, 255), [(50, 3), (92, 91), (50, 70), (8, 91)], 4)
    pygame.draw.polygon(ship, (165, 90, 255), [(50, 23), (64, 66), (50, 57), (36, 66)])
    pygame.draw.ellipse(ship, (255, 175, 50), (35, 76, 12, 22))
    pygame.draw.ellipse(ship, (255, 175, 50), (53, 76, 12, 22))
    pygame.image.save(ship, str(IMAGES / "neon_ship.png"))

    laser = pygame.Surface((22, 72), pygame.SRCALPHA)
    pygame.draw.rect(laser, (0, 110, 160, 110), (1, 0, 20, 72), border_radius=10)
    pygame.draw.rect(laser, (0, 245, 255), (6, 0, 10, 72), border_radius=5)
    pygame.draw.rect(laser, (245, 255, 255), (9, 3, 4, 66), border_radius=2)
    pygame.image.save(laser, str(IMAGES / "neon_laser.png"))

    background = pygame.Surface((1200, 800))
    for y in range(800):
        pygame.draw.line(background, (5 + y // 180, 7 + y // 110, 24 + y // 75), (0, y), (1200, y))
    rng = random.Random(2026)
    for _ in range(220):
        x, y = rng.randrange(1200), rng.randrange(800)
        pygame.draw.circle(background, rng.choice([(120, 170, 220), (220, 240, 255), (85, 110, 190)]), (x, y), rng.choice([1, 1, 2]))
    for center, radius in [((260, 250), 170), ((980, 510), 220)]:
        for r in range(radius, 0, -12):
            shade = int(24 * (1 - r / radius))
            pygame.draw.circle(background, (8 + shade // 3, 9 + shade // 4, 27 + shade), center, r)
    pygame.image.save(background, str(IMAGES / "neon_background.png"))

    sample_rate = 44100
    duration = 0.22
    samples = array("h")
    phase = 0.0
    for i in range(int(sample_rate * duration)):
        t = i / sample_rate
        frequency = 1000 - 780 * (t / duration)
        phase += 2 * math.pi * frequency / sample_rate
        envelope = (1 - t / duration) ** 2
        samples.append(int(15000 * envelope * math.sin(phase)))
    with wave.open(str(SOUNDS / "neon_laser.wav"), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(sample_rate)
        output.writeframes(samples.tobytes())
    pygame.quit()


if __name__ == "__main__":
    generate_assets()
