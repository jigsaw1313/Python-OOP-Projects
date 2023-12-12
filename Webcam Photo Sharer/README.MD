
# File Sharing Application

This repository contains a simple file-sharing application built with Kivy and Filestack API.

## Overview

The application consists of two main screens:

1. **CameraScreen:**
   - Start and stop the camera.
   - Capture and display images.

2. **ImageScreen:**
   - Create a shareable link for the captured image.
   - Copy the link to the clipboard.
   - Open the link in the default browser.

## How to Use

1. Run the `main.py` file to launch the application.
2. Use the camera screen to start, stop, and capture images.
3. Navigate to the image screen to create a shareable link.
4. Copy the link or open it in the default browser.

## Dependencies

- Kivy: UI framework for the app.
- Filestack: API for file uploading and sharing.

## FileSharer Class

The `FileSharer` class in `FileSharer.py` utilizes the Filestack API to generate shareable links for uploaded files.

## Installation

1. Install the required dependencies:
   ```
   pip install kivy filestack-python
   ```

2. Get your Filestack API key from [Filestack](https://www.filestack.com/).

3. Replace `<YOUR-API-KEY>` in the `FileSharer` class with your actual API key.

4. Run the application:
   ```
   python main.py
   ```

## Screenshots

Include screenshots or GIFs demonstrating the application in action.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
