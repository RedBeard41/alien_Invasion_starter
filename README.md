# Neon Defender — Track 2: Custom Assets

This is **Milestone 1** of the Alien Invasion customization project.

## Original custom assets

The project includes the generated Milestone 1 assets in the `Assets/` folders:
- `Assets/images/neon_ship.png` — cyan/purple spaceship
- `Assets/images/neon_background.png` — deep-space starfield
- `Assets/images/neon_laser.png` — glowing cyan laser
- `Assets/sound/neon_laser.wav` — original synthesized descending laser sound

The reproducible source for these files is `asset_generator.py`. All paths use `pathlib`. The generator preserves existing custom files and only creates missing assets, so manual edits are not overwritten unexpectedly.

## Installation and play

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe alien_invasion.py
```

If your Windows Python launcher is available on PATH, the equivalent commands are:
```powershell
py -m pip install -r requirements.txt
py alien_invasion.py
```

Use **A/D** or **Left/Right** to move, **Space** to fire, and **Q/Esc** to quit.

## Milestone boundaries

**Active in Milestone 1:** ship, background, laser art, custom laser sound, movement and firing.

**Disabled until Milestone 2:** alien fleet, alien animations, collision detection, explosion sound.

**Disabled until Final:** scoring, lives, HUD, buttons, music, and game-over screen.

## Submission

**Milestone 1 GitHub branch:** https://github.com/XavierChitison/alien_Invasion_starter/tree/track_2_assets

**Milestone 1 YouTube demo:** _Add your unlisted YouTube URL here after recording (2 minutes maximum)._

**Milestone 2 GitHub branch:** _Update when complete._

**Milestone 2 YouTube demo:** _Update when complete._

**Final GitHub branch:** _Update when complete._

**Final YouTube demo:** _Update when complete._

## Starter code credit

Based on https://github.com/XavierChitison/alien_Invasion_starter. Original custom artwork and sound are generated programmatically by this project.
