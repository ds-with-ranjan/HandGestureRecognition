# ✋ Hand Gesture Recognition System

A real-time hand gesture recognition system built with Python, OpenCV, and MediaPipe. This application tracks your hand movements and translates the number of raised fingers into automated system actions, such as launching AI tools in your browser or closing active windows.

## ✨ Features

- **Real-Time Detection:** Tracks a single hand seamlessly using MediaPipe.
- **Gesture Mapping:**
  - ☝️ **1 Finger:** Opens Claude AI.
  - ✌️ **2 Fingers:** Opens ChatGPT.
  - 🤟 **3 Fingers:** Opens Google Gemini.
  - 🖐️ (4 Fingers) **4 Fingers:** Opens LinkedIn.
  - ✊ **Closed Fist (0 Fingers):** Closes all active browser windows.
- **Smart Cooldown:** Built-in 3-second cooldown mechanism prevents rapid-fire, accidental triggering of actions.
- **Visual Feedback:** Displays hand landmarks, finger count, and current action status directly on the webcam feed.
- **Modular Architecture:** Clean, Object-Oriented code making it easy to extend and modify.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/HandGestureRecognition.git](https://github.com/yourusername/HandGestureRecognition.git)
   cd HandGestureRecognition