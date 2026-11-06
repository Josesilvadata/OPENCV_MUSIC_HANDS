import cv2
import numpy as np
import mediapipe as mp
import sounddevice as sd

SAMPLE_RATE = 44100

NOTE_NAMES = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
