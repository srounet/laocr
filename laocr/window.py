from typing import Optional, Tuple

import random
import time

import cv2
import numpy
import pyautogui

from laocr.capture import capture
from laocr.resources import BUTTON_EXIT


def find_in_window(source_image: numpy.ndarray, threshold: float = 0.9, screenshot: Optional[numpy.ndarray] = None) -> Optional[Tuple]:
    """
    Given a source image and a default threshold will search within currently displayed image a potential match.

    Args:
        source_image (numpy.ndarray): An image to search within captured screen or given screenshot
        threshold (float): The accepted quality to consider matches (default to .9)
        screenshot (numpy.ndarray): Optionally an image to search from. This is useful if you don t want to search the entire screen

    Returns:
        coordinates: A tuple with first match coordinates (top left coordinates of full screen or relative to given ss)
    """
    if screenshot is None:
        screenshot = capture()

    template_picture_coordinates = cv2.matchTemplate(screenshot, source_image, cv2.TM_CCOEFF_NORMED)
    template_picture_coordinates_loc = numpy.where(template_picture_coordinates >= threshold)
    if template_picture_coordinates_loc[0].any():
        coordinates = list(zip(*template_picture_coordinates_loc))
        coordinates = tuple(reversed(coordinates[0]))
        return coordinates


def click_at(x: int, y: int, move_to: bool = False):
    """
    Will left click at given coordinates (x/y), optionally will 'move' the cursor in to the corresponding location
    instead of directly replacing coordinates (more like a human behavior).

    Args:
        x (int): An integer representing the X coordinate to click at
        y (int): An integer representing the Y coordinate to click at
        move_to (bool): Humanize the cursor shift from actual position (default false)
    """
    if move_to:
        pyautogui.moveTo(x, y, random.uniform(.1, .5))
        pyautogui.click()
    else:
        pyautogui.click(x=x, y=y)


def press(key: str):
    """
    Will press a given key with a random threshold between .05 and .1 (human behavior)

    Args:
        key (str): a character representing key to press
    """
    pyautogui.keyDown(key)
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp(key)


def reset():
    """
    Trigger the exit button (escape), will loop until main menu is found and stop iteration.
    Will sleep between iteration so catch changes.
    """
    while not find_in_window(BUTTON_EXIT):
        pyautogui.hotkey('escape')
        time.sleep(random.uniform(.3, .5))
    # we are now displayed with the main exit menu, let's get rid of it
    pyautogui.hotkey('escape')
