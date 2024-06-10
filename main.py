import cv2
import numpy as np
import pyautogui
import time
import keyboard


def check_catch(x_start, x_end, y_start, y_end):
    # Take screenshot and crop the region of interest
    screenshot = np.array(pyautogui.screenshot())
    roi = screenshot[y_start:y_end, x_start:x_end]

    # Convert to grayscale image
    grayscale_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Define threshold for detecting black pixels
    threshold = 10  # Adjust this value as needed

    # Set click position to 0,0 otherwise we get weird camera movements in game
    click_pos = (0, 0)

    # Check if ROI is composed of black pixels
    if np.mean(grayscale_roi) < threshold:
        pyautogui.rightClick(click_pos) # Reel in the fish (or treasure!)
        time.sleep(0.5)
        pyautogui.rightClick(click_pos) # Cast rod again

        return 1

    return 0
    # cv2.imwrite("test.png", grayscale_roi)

def start_init_timer(start_from):
    for count in range(start_from, 0, -1):
        print("{}...".format(count))
        time.sleep(1)

    print("GO! GO! GO! GOOOOOO!!!")


# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Screen is 2560x1440
big_screen_roi = {'x1': 2375, 'x2': 2385, 'y1': 1285, 'y2': 1342}

# Screen is 1920x1080
laptop_screen_roi = {'x1': 1725, 'x2': 1745, 'y1': 930, 'y2': 985}

# roi_width = int(screen_width * 0.1)  # 20% of the screen width
# roi_height = int(screen_height * 0.1)  # 20% of the screen height
#
# roi_x = screen_width - roi_width
# roi_y = screen_height - roi_height

roi = laptop_screen_roi

start_init_timer(5)

catches = 0
while True:
    is_catch = check_catch(roi['x1'], roi['x2'], roi['y1'], roi['y2'])
    if is_catch:
        catches = catches + 1
        print("Catch:", catches)
        # Sleep time must be greater than MC subtitle fade time
        time.sleep(2.5)

    # Stop script when 'p' is pressed
    if keyboard.is_pressed("p"):
        print("IT'S G-OVER")
        print("You caught:", catches)
        break
