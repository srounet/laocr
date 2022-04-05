from typing import Optional

import cv2
import numpy
import pyautogui


def capture(
        left: Optional[int] = None, top: Optional[int] = None,
        width: Optional[int] = None, height: Optional[int] = None) -> numpy.ndarray:
    """
    Take a screenshot for actual focused screen.
    Image is returned as a numpy array
    """
    region = (left or 0, top or 0, width or 0, height or 0)
    if any(region):
        image = pyautogui.screenshot(region=region)
    else:
        image = pyautogui.screenshot()
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image


def capture_center(width: int = 300, height: int = 300) -> numpy.ndarray:
    """
    Take a screenshot of lost ark center. The default rectangle size is 300 per 300 pixels.
    Image is returned as a numpy array.
    """

    screen_size = pyautogui.size()
    center_region = (screen_size.width / 2 - 100, screen_size.height / 2 - 150, width, height)
    center_image = capture(*center_region)
    return center_image


def capture_toolbar() -> numpy.ndarray:
    """
    Take a screenshot of lost ark left toolbar (attacks).
    Image is returned as a numpy array
    """

    screen_size = pyautogui.size()
    toolbar_region = (screen_size.width / 2 - 340, screen_size.height - 130, 260, 120)
    toolbar_image = capture(*toolbar_region)
    return toolbar_image





image = capture_toolbar()
cv2.imwrite('test.png', image)
