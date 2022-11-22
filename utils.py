import numpy as np
import cv2


def read_img(filename, mode=cv2.IMREAD_COLOR, return_np=False):
    raw_data = np.fromfile(filename, dtype=np.uint8)
    cv_img = cv2.imdecode(raw_data, mode)
    return cv_img if return_np else cv_img
