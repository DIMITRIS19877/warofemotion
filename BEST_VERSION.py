import cv2
import pygame
import numpy as np
import random

# Initialize Pygame for audio playback
pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play(-1)  # Loop the audio

# Load the virtual background video clip
background = cv2.VideoCapture("video.mp4")

# Load the video capture device (i.e., your camera)
cap = cv2.VideoCapture(0)

# Check if the camera was successfully loaded
if not cap.isOpened():
    print("Error: could not open camera")
    exit()

# Set the camera resolution to match your screen's resolution (1280x720)
screen_width = 2560
screen_height = 1600

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Initialize variables for the circles
circles = []  # List to store circle information (center, radius, color)
circle_color = (0, 255, 0)  # Green circle
circle_black_color = (0, 0, 0)  # Black circle
num_circles = 0  # Number of circles to show

# Load a sound effect for "c" key press
sound_effect = pygame.mixer.Sound("gun.wav")

# Loop through frames from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error: could not read frame")
        break

    # Read a frame from the background video clip
    ret, bg_frame = background.read()

    # Check if the background frame was successfully read
    if not ret:
        # Restart the video clip from the beginning if it reaches the end
        background.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, bg_frame = background.read()

    # Resize the background frame to match the screen resolution
    bg_frame = cv2.resize(bg_frame, (screen_width, screen_height))

    # Resize the camera frame to match the screen resolution
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Resize the frame to add a mosaic effect
    pixel_size = 20
    small_frame = cv2.resize(frame, None, fx=1/pixel_size, fy=1/pixel_size, interpolation=cv2.INTER_NEAREST)
    pixelated_frame = cv2.resize(small_frame, (screen_width, screen_height), interpolation=cv2.INTER_NEAREST)

    # Combine the pixelated camera frame with the background frame
    output = cv2.addWeighted(pixelated_frame, 0.7, bg_frame, 0.3, 0)

    # Display the "Press Spacebar to shoot" text in the center of the screen
    text = "Press SPACE for shooting"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)  # White color
    font_thickness = 2
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (screen_width - text_size[0]) // 2
    text_y = (screen_height + text_size[1]) // 2
    cv2.putText(output, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

    # Show the circles
    for circle_info in circles:
        circle_center, circle_radius, circle_color = circle_info
        cv2.circle(output, circle_center, circle_radius, circle_color, -1)  # Draw colored circle
        cv2.circle(output, circle_center, 5, circle_black_color, -1)  # Draw black center circle

    # Display the output
    cv2.imshow("Virtual Background", output)

    # Check for key presses
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == 32:
        # Remove the previous circle (if any)
        if num_circles > 0:
            circles.pop()
        # Generate random circle information
        random_center = (random.randint(0, screen_width), random.randint(0, screen_height))
        random_radius = random.randint(20, 300)
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circles.append((random_center, random_radius, random_color))
        num_circles += 1
        # Play the sound effect
        sound_effect.play()

# Release the capture device and close the window
cap.release()
background.release()
cv2.destroyAllWindows()
