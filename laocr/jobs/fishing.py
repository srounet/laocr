import random
import time

from laocr.resources import FISHING_BITE, SKILL_FISHING_ACTIVE
from laocr.capture import capture_center, capture_toolbar
from laocr.window import find_in_window, press


def is_fishing():
    """
    Returns whether or not we are currently fishing.

    Returns:
        fishing_active_displayed: A boolean indicating if are in the process of fishing
    """
    toolbar_image = capture_toolbar()

    fishing_active_displayed = find_in_window(source_image=SKILL_FISHING_ACTIVE, screenshot=toolbar_image, threshold=.7)
    fishing_active_displayed = bool(fishing_active_displayed)
    return fishing_active_displayed


def is_bite_event_displayed() -> bool:
    """
    Detects fish bites by searching for bite icon '!' on screen center.
    Will return True in case a bite icon is found.

    Returns:
        bite_event_displayed: A boolean indicating if a bite event has been detected
    """
    center_image = capture_center()

    bite_event_displayed = find_in_window(source_image=FISHING_BITE, screenshot=center_image, threshold=.7)
    bite_event_displayed = bool(bite_event_displayed)
    return bite_event_displayed


def throw(fishing_key: str) -> bool:
    """
    Given Fishing skill key will throw lure and start fishing.
    Return success if the active fishing skill is found.

    Args:
        fishing_key (str): a character representing key to press

    Returns:
        is_fishing: A boolean indicating if are currently in the process of fishing
    """
    press(fishing_key)
    time.sleep(random.uniform(1.3, 1.5))
    return is_fishing()


def catch(fishing_key: str) -> bool:
    """
    Given Fishing skill key will press the catch key to hook fish and collect loot.

    Args:
        fishing_key (str): a character representing key to press

    Returns:
        is_fishing: A boolean indicating if we successfully exited the process of fishing
    """
    press(fishing_key)
    time.sleep(random.uniform(1.3, 1.5))
    return not is_fishing()
