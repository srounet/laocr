import os.path

import cv2


OCR_EXTRACTS_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ocr_extracts')


BUTTON_PET_WINDOW_REPAIR_TOOL = cv2.imread(os.path.join(OCR_EXTRACTS_ROOT, "button_pet_window_repair_tool.png"), 0)
BUTTON_EXIT = cv2.imread(os.path.join(OCR_EXTRACTS_ROOT, "button_exit.png"), 0)
FISHING_BITE = cv2.imread(os.path.join(OCR_EXTRACTS_ROOT, "fishing_bite.png"), 0)
SKILL_FISHING_INACTIVE = cv2.imread(os.path.join(OCR_EXTRACTS_ROOT, "skill_fishing_inactive.png"), 0)
SKILL_FISHING_ACTIVE = cv2.imread(os.path.join(OCR_EXTRACTS_ROOT, "skill_fishing_active.png"), 0)
FISHING_SUCCESS = cv2.imread(os.path.join(OCR_EXTRACTS_ROOT, "fishing_success.png"), 0)
