import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import cv2

dll = ctypes.cdll.LoadLibrary
lib = dll("./HVIC_USBSDK.dll")
lib.HVIC_IniRGBDAndOpenDefaultPy()
lib.HVIC_GetXyzRgbPy.argtypes = [ndpointer(ctypes.c_float), ndpointer(ctypes.c_uint8)]
lib.HVIC_GetXyzRgbPy.restype = ctypes.c_bool
width = 640
height = 480
h_width = 320
h_height = 240

while (True):
    xyzir = np.zeros((height*4, width), np.float32)
    arrXyzir = np.asarray(xyzir)
    rgb = np.zeros((height, width, 3), np.uint8)
    arrRgb = np.asarray(rgb)
    res = lib.HVIC_GetXyzRgbPy(arrXyzir, arrRgb)
    showD = xyzir[height*2:height*3, 0:width]
    print("center depth: ")
    print(showD[h_height, h_width])
    cv2.imshow("depth", showD)
    cv2.imshow("rgb", arrRgb)
    if cv2.waitKey(60) == ord('s'):
        lib.HVIC_SaveRgbDPly();
    if cv2.waitKey(60) == 27:
        break;
    if not res:
        break;

lib.HVIC_ReleaseRgbDAndClose()