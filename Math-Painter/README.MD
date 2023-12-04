# Drawing Application

This is a simple drawing application written in Object-Oriented Python. The application allows users to create a canvas and draw rectangles or squares on it. Each shape can be customized with different dimensions and colors.

## Usage

1. Run `main.py` to start the drawing application.
2. Enter the canvas width, canvas height, and choose the canvas color (white or black).
3. Follow the prompts to draw rectangles or squares by entering the desired shape type, position, size, and color.
4. Enter 'quit' to exit the application.
5. The drawn canvas will be saved as 'canvas.png' in the root directory.

## Modules

### 1. main.py
The main script that initializes the canvas, interacts with the user, and draws shapes on the canvas.

### 2. canvas.py
Contains the `Canvas` class responsible for creating and saving the canvas image.

### 3. shapes.py
Defines the `Rectangle` and `Square` classes, representing the shapes that can be drawn on the canvas.

## Dependencies
- `numpy`: For array operations.
- `PIL`: For creating and saving images.

## Running the Application
Ensure you have the required dependencies installed:
```bash
pip install numpy pillow
```

Run the application:
```bash
python main.py
```


Feel free to explore, draw, and create colorful canvases with this simple drawing application!