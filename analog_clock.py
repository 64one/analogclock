import pygame
import time
import math


pygame.init()
FPS = 30
WIDTH = HEIGHT = 400 # 300 minimum
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()

CLOCK_RADIUS = WIDTH // 2
CENTER_PIN_RADIUS = int(WIDTH / 300 * 4)

# Lengths of clock hands
SECONDS_HAND_LENGTH = 0.8 * CLOCK_RADIUS
SECONDS_HAND_TAIL = 0.1 * SECONDS_HAND_LENGTH

MINUTES_HAND_LENGTH = 0.65 * CLOCK_RADIUS
MINUTES_HAND_TAIL = 0.1 * MINUTES_HAND_LENGTH

HOUR_HAND_LENGTH = 0.45 * CLOCK_RADIUS
HOUR_HAND_TAIL = 0.1 * HOUR_HAND_LENGTH

# These increase in size as clock size increases
HOUR_TICK_LENGTH = int(WIDTH / 300 * 10)
HOUR_TICK_WIDTH = int(WIDTH / 300 * 2)
TICK_PADDING_FROM_EDGE = 15
MIN_TICK_LENGTH = int(WIDTH / 300 * 5)
MIN_TICK_WIDTH = int(WIDTH / 300 * 1)

# Angles in degrees
ANGLE_PER_HOUR = 30
ANGLE_PER_MIN = 6
ANGLE_PER_SEC = 6

numbers_font_size = int(WIDTH / 300 * 24)
NUMBERS_FONT = pygame.font.Font(size=numbers_font_size)
NUMBER_TICK_PADDING = 15

# Colors
BG_COLOR = "white"
NUMBERS_COLOR = "black"
CLOCK_CIRCLE_COLOR = "black"
CENTER_PIN_COLOR = "black"
HOUR_HAND_COLOR = "black"
MINUTES_HAND_COLOR = "blue"
SECONDS_HAND_COLOR = "red"
HOUR_TICKS_COLOR = "black"
MINUTE_TICKS_COLOR = "black"


def rotate_point(
    angle_of_rotation:int, 
    center:tuple, 
    point:tuple
) -> tuple[int, int]:
    # Calculate original vector
    dx = point[0] - center[0]
    dy = point[1] - center[1]

    # Apply 2D rotation formula
    angle_radians = math.radians(angle_of_rotation)
    rotated_dx = dx * math.cos(angle_radians) - dy * math.sin(angle_radians)
    rotated_dy = dx * math.sin(angle_radians) + dy * math.cos(angle_radians)

    # New position after rotation
    rotated_point = (center[0] + rotated_dx, center[1] + rotated_dy)
    return rotated_point


def draw_numbers(number:int, center:tuple) -> None:
    text = str(number)
    width, height = NUMBERS_FONT.size(text)
    text_rect = pygame.Rect(0, 0, width, height)
    text_rect.center = center
    text_surface = NUMBERS_FONT.render(text, True, NUMBERS_COLOR)
    screen.blit(text_surface, text_rect)


running = True
center_x, center_y = WIDTH // 2, HEIGHT // 2
center = (center_x, center_y)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(BG_COLOR)
    pygame.draw.circle(
        surface = screen, 
        color = CLOCK_CIRCLE_COLOR, 
        center = center, 
        radius = CLOCK_RADIUS, 
        width = 4
    )

    # Clock hour ticks
    # Start at 12 tick
    start_pos = center_x, TICK_PADDING_FROM_EDGE
    hour_end_pos = center_x, TICK_PADDING_FROM_EDGE + HOUR_TICK_LENGTH
    minute_end = center_x, TICK_PADDING_FROM_EDGE + MIN_TICK_LENGTH
    number_center = hour_end_pos[0], hour_end_pos[1] + NUMBER_TICK_PADDING
    angle = 0
    for i in range(12):
        # Hours ticks
        width = HOUR_TICK_WIDTH * 2 if angle % 90 == 0 else HOUR_TICK_WIDTH
        start = rotate_point(angle, center, start_pos)
        end = rotate_point(angle, center, hour_end_pos)
        pygame.draw.line(screen, HOUR_TICKS_COLOR, start, end, width)
        number = i if i > 0 else 12
        num_center = rotate_point(angle, center, number_center)
        draw_numbers(number, num_center)

        # Minutes ticks
        for x in range(5):
            start = rotate_point(angle, center, start_pos)
            end = rotate_point(angle, center, minute_end)
            pygame.draw.line(screen, MINUTE_TICKS_COLOR, start, end, MIN_TICK_WIDTH)
            angle += ANGLE_PER_MIN

    # Current Time
    current_time = time.strftime("%H:%M:%S")
    hrs_str, mins_str, secs_str = current_time.split(":")
    seconds = int(secs_str)
    minutes = int(mins_str) + seconds / 60
    hours = int(hrs_str) + minutes / 60

    # Hours hand
    start_pos = center_x, center_y - HOUR_HAND_LENGTH
    end_pos = center_x, center_y + HOUR_HAND_TAIL
    hours_angle = hours * ANGLE_PER_HOUR
    start = rotate_point(hours_angle, center, start_pos)
    end = rotate_point(hours_angle, center, end_pos)
    pygame.draw.line(screen, HOUR_HAND_COLOR, start, end, 6)

    # Minutes hand
    start_pos = center_x, center_y - MINUTES_HAND_LENGTH
    end_pos = center_x, center_y + MINUTES_HAND_TAIL
    minutes_angle = minutes * ANGLE_PER_MIN
    start = rotate_point(minutes_angle, center, start_pos)
    end = rotate_point(minutes_angle, center, end_pos)
    pygame.draw.line(screen, MINUTES_HAND_COLOR, start, end, 5)

    # Seconds hand
    start_pos = center_x, center_y - SECONDS_HAND_LENGTH
    end_pos = center_x, center_y + SECONDS_HAND_TAIL
    seconds_angle = seconds * ANGLE_PER_SEC
    start = rotate_point(seconds_angle, center, start_pos)
    end = rotate_point(seconds_angle, center, end_pos)
    pygame.draw.line(screen, SECONDS_HAND_COLOR, start, end, 4)

    # Center pin
    pygame.draw.circle(screen, CENTER_PIN_COLOR, center, CENTER_PIN_RADIUS)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
