# warofemotion
# Virtual Background and Sound Effects Application

This Python application creates an interactive experience by using the computer's camera to display the user with a virtual background and adding sound effects when the spacebar is pressed.

## Prerequisites

Before running this application, you will need:

- Python 3.11.2: Main programming language.
- OpenCV (cv2) 4.5.5: Used for video capture and processing.
- Pygame 2.5.2: Employed for audio playback and user interaction.
- NumPy 1.24.2: Utilized for mathematical operations and video frame processing.

Additionally, a camera connected to your computer and an `audio.mp3` sound file along with a `video.mp4` video file in the same directory as the script are required.

Usage

Once the application is running, you will see the camera feed with the virtual background applied. Press the spacebar to play the sound effect and create random circles on the screen.

Stopping the Application

To stop the application, press the 'q' key on your keyboard.

Additional Information

Ensure your audio.mp3 and video.mp4 files are correctly placed in the same directory as the Python script for the application to function properly. Adjust the screen width and height variables in the script if necessary to match your screen's resolution.

## Installation

First, install the required packages using pip:

```bash
pip install opencv-python pygame numpy
