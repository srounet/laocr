from typing import Optional

import cv2
import numpy
import pyautogui


def capture(
        left: Optional[int] = None, top: Optional[int] = None,
        width: Optional[int] = None, height: Optional[int] = None) -> numpy.ndarray:
    """
    Take a screenshot for actual focused screen.

    Args:
        left (int): An integer representing left coordinates to capture from
        top (int): An integer representing top coordinates to capture from
        width (int): An integer representing width of the rectangle to capture
        height (int): An integer representing height of the rectangle to capture

    Returns:
        capture_image: A Gray captured image translated to a numpy.ndarray
    """
    region = (left or 0, top or 0, width or 0, height or 0)
    if any(region):
        capture_image = pyautogui.screenshot(region=region)
    else:
        capture_image = pyautogui.screenshot()
    capture_image = cv2.cvtColor(numpy.array(capture_image), 0)
    capture_image = cv2.cvtColor(capture_image, cv2.COLOR_BGR2GRAY)
    return capture_image


def capture_center(width: int = 300, height: int = 300) -> numpy.ndarray:
    """
    Take a screenshot of lost ark center. The default rectangle size is 300 per 300 pixels.

    Args:
        width (int): An integer representing width of the rectangle to capture
        height (int): An integer representing height of the rectangle to capture

    Returns:
        center_image: A Gray captured image translated to a numpy.ndarray
    """
    screen_size = pyautogui.size()
    center_region = (screen_size.width / 2 - 100, screen_size.height / 2 - 150, width, height)
    center_image = capture(*center_region)
    return center_image


def capture_toolbar() -> numpy.ndarray:
    """
    Take a screenshot of lost ark left toolbar (attacks).

    Returns:
        center_image: A Gray captured image translated to a numpy.ndarray
    """
    screen_size = pyautogui.size()
    toolbar_region = (screen_size.width / 2 - 340, screen_size.height - 130, 260, 120)
    toolbar_image = capture(*toolbar_region)
    return toolbar_image
