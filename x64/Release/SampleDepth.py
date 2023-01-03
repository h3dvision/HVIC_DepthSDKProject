import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import cv2

dll = ctypes.cdll.LoadLibrary
lib = dll("./HVIC_USBSDK.dll")
lib.HVIC_IniDepthAndOpenDefaultPy()
lib.HVIC_GetXyzIRPy.argtypes = [ndpointer(ctypes.c_float)]
lib.HVIC_GetXyzIRPy.restype = ctypes.c_bool
width = 640
height = 480
h_width = 320
h_height = 240

while (True):
    xyzir = np.zeros((height*4, width), np.float32)
    arrXyzir = np.asarray(xyzir)
    res = lib.HVIC_GetXyzIRPy(arrXyzir)
    showD = xyzir[height*2:height*3, 0:width]
    ir = xyzir[height*3:height*4, 0:width]
    showIR = np.zeros((height, width, 3), np.uint8)
    showIR[:,:,0] = showIR[:,:,1] = showIR[:,:,2] = ir*(255.0/(ir.max()+1.0))
    print("center depth: ")
    print(showD[h_height, h_width])
    cv2.imshow("depth", showD)
    cv2.imshow("ir", showIR)
    if cv2.waitKey(60) == ord('s'):
        lib.HVIC_SaveDepthPly();
    if cv2.waitKey(60) == 27:
        break;
    if not res:
        break;

lib.HVIC_ReleaseDepthAndClose()