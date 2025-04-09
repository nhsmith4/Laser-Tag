import tkinter as tk
import random
import pygame
import os
import globe

from globe.view import omni_dir, WIDTH, HEIGHT

# Initialize pygame mixer
pygame.mixer.init()
music_playing = False

# List of 7 MP3 tracks (Ensure these exist in the same directory as the script)
music_tracks = [omni_dir("Track01.mp3"), omni_dir("Track02.mp3"), omni_dir("Track03.mp3"), omni_dir("Track04.mp3"), 
                omni_dir("Track05.mp3"), omni_dir("Track06.mp3"), omni_dir("Track07.mp3"), omni_dir("Track08.mp3")]

# Function to play a random track
def play_random_music():
    global music_playing  

    if not music_playing and not pygame.mixer.music.get_busy():
        track = random.choice(music_tracks)
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        music_playing = True

# Function to stop the music
def stop_music():
    global music_playing  # Modify the global variable
    music_playing = False
    pygame.mixer.music.stop()

    