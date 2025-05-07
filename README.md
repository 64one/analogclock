# Analog Clock

A Python-based analog clock simulation built with Pygame. This project renders a customizable analog clock with hour, minute, and second hands that display the current system time.
![analog_clock](https://github.com/user-attachments/assets/e16799bb-d228-4661-8eba-c0dba6615da1)

## Features
- Real-time display of the current system time
- Aesthetic design with distinct hour, minute, and second hands
- Hour markers with numbers for easy reading
- Minute markers for precise time interpretation
- Customizable colors and dimensions
- Smooth hand movements

## Requirements
- Python 3.x
- Pygame

## Installation
1. Clone this repository:
```bash
git clone https://github.com/64one/analogclock.git
cd analogclock
```

2. Install the required packages:
```bash
pip install pygame
```

## Usage
Run the program with:

```bash
python analog_clock.py
```

The clock window will appear, displaying the current system time.

## Customization
You can easily customize the clock by modifying the following parameters at the top of the script:
- `WIDTH` and `HEIGHT`: Change the size of the clock window
- `CLOCK_RADIUS`: Adjust the clock face size
- Various hand lengths and thicknesses
- Colors for different clock elements

## Controls
- Close the window to exit the application

## How It Works
The program:
1. Initializes a Pygame window
2. Draws the clock face with hour and minute markers
3. Gets the current system time
4. Calculates the positions of hour, minute, and second hands
5. Renders the hands on the clock face
6. Updates the display at regular intervals (30 FPS)

## License
This project is licensed under the MIT License.

## Author
Martin Chege

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
