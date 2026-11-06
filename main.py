import cv2
import numpy as np
import mediapipe as mp
import sounddevice as sd

SAMPLE_RATE = 44100

NOTE_NAMES = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
NOTE_FREQS = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]


