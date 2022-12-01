import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import cv2

dll = ctypes.cdll.LoadLibrary
lib = dll("./HVIC_USBSDK.dll")
lib.HVIC_IniRGBDAndOpenDefaultPy()
lib.HVIC_GetXyzRgbPy.argtypes = [ndpointer(ctypes.c_float), ndpointer(ctypes.c_uint8)]
lib.restype = bool

while (True):
    xyzir = np.zeros((480*4, 640), np.float32)
    arrXyzir = np.asarray(xyzir)
    rgb = np.zeros((480, 640, 3), np.uint8)
    arrRgb = np.asarray(rgb)
    res = lib.HVIC_GetXyzRgbPy(arrXyzir, arrRgb)
    showD = xyzir[960:1440, 0:640]
    print(showD[240, 320])
    cv2.imshow("depth", showD)
    cv2.imshow("rgb", arrRgb)
    key = cv2.waitKey(60)
    if key == ord('s'):
        lib.HVIC_SaveRgbDPly();
    if key == ord('q'):
        break;
    if not res:
        break;

lib.HVIC_ReleaseRgbDAndClose()