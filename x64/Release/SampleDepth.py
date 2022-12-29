import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import cv2

dll = ctypes.cdll.LoadLibrary
lib = dll("./HVIC_USBSDK.dll")
#lib = dll("/usr/local/lib/libHVIC_USBSDK.so")
lib.HVIC_IniDepthAndOpenDefaultPy()
lib.HVIC_GetXyzIRPy.argtypes = [ndpointer(ctypes.c_float)]
lib.HVIC_GetXyzIRPy.restype = ctypes.c_bool

while (True):
    xyzir = np.zeros((480*4, 640), np.float32)
    arrXyzir = np.asarray(xyzir)
    res = lib.HVIC_GetXyzIRPy(arrXyzir)
    showD = xyzir[960:1440, 0:640]
    ir = xyzir[1440:1920, 0:640]
    showIR = np.zeros((480, 640, 3), np.uint8)
    showIR[:,:,0] = showIR[:,:,1] = showIR[:,:,2] = ir*(255.0/(ir.max()+1.0))
    print("center depth: ") 
    print(showD[240, 320])
    cv2.imshow("depth", showD)
    cv2.imshow("ir", showIR)
    if cv2.waitKey(60) == ord('s'):
        lib.HVIC_SaveDepthPly();
    if cv2.waitKey(60) == 27:
        break;
    if not res:
        break;

lib.HVIC_ReleaseDepthAndClose()