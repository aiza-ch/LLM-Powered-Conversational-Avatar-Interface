import asyncio
import edge_tts
import pygame
import os
import uuid

async def speak(text, voice="en-US-GuyNeural"):
    filename = f"temp_{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

    # Initialize and play using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait until playback finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Unload the file to release it
    pygame.mixer.music.unload()

    # Now safely delete the file
    os.remove(filename)

def speak_text(text, voice="en-US-GuyNeural"):
    asyncio.run(speak(text, voice))
