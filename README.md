# Touchless-MacOS-Control

Touchless-MacOS-Control is a hands-free control system for macOS that enables users to interact with their computer using **gesture recognition** and **voice commands**. Leveraging MediaPipe for real-time gesture detection and Google Speech Recognition for voice commands, this project provides an intuitive, touchless interface to perform common system actions.

---

## Features

- **Gesture Recognition:** Detects predefined hand gestures via webcam to trigger system actions.
- **Voice Control:** Recognizes voice commands to perform actions without touching the keyboard or mouse.
- **AppleScript Integration:** Executes macOS system commands through AppleScript for seamless control.
- **Real-time Video Preview:** Displays live webcam feed with gesture detection feedback.
- **Configurable Commands:** Easily customize gestures and voice commands via YAML configuration files.

---

## Demo

![Demo GIF or Screenshot](path/to/demo.gif)

---

## Getting Started

### Prerequisites

- macOS system with webcam and microphone
- Python 3.9+
- Homebrew (for installing dependencies)

### Installation

1. **Clone the repository:**
git clone https://github.com/preeteshchoudhary/Touchless-MacOS-Control.git
cd Touchless-MacOS-Control

text

2. **Install dependencies:**
brew install portaudio
pip install -r requirements.txt

text

3. **Download the MediaPipe gesture recognition model:**
curl -O https://storage.googleapis.com/mediapipe-tasks/gesture_recognizer/gesture_recognizer.task

text

4. **Grant Accessibility and Microphone permissions:**
- Go to **System Preferences > Security & Privacy > Privacy**
- Enable permissions for Terminal (or your IDE) under **Accessibility** and **Microphone**

---

## Usage

Run the main application:

python3 main.py

text

- The system will start listening for gestures and voice commands.
- Use the configured gestures or speak commands to control macOS actions like volume control, locking the screen, switching tabs, and more.
- Press `Ctrl+C` to stop the application.

---

## Configuration

### Gesture Commands

Modify `config/gestures.yaml` to customize gesture-to-action mappings.

Example:

Thumb_Up: volume_up
Thumb_Down: volume_down
Victory: mute_volume

text

### Voice Commands

Modify `config/voice_commands.yaml` to customize voice command mappings.

Example:

volume up: volume_up
volume down: volume_down
mute: mute_volume

text

---

## AppleScript Actions

AppleScript files located in `core/system/applescripts/` define system actions. You can add or modify scripts to extend functionality.

---

## Troubleshooting

- **Microphone or Camera not detected:**  
  Ensure your macOS privacy settings allow access to these devices.

- **Gesture not recognized:**  
  Make sure your webcam is properly connected and the lighting is sufficient.

- **Voice commands not recognized:**  
  Speak clearly and ensure your microphone is working.

- **Permission errors:**  
  Confirm that Terminal or your IDE has Accessibility and Automation permissions.

---

## Contributing

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for gesture recognition.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for voice command processing.
- AppleScript for macOS system automation.

---

**Enjoy touchless control of your Mac!** 🚀
