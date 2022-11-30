#pragma once

#ifdef _WINDOWS
#define HVIC_USBSDKDLL __declspec(dllexport)
#else
#define HVIC_USBSDKDLL
#endif

#include <vector>
#include <string>

#ifdef _WINDOWS
#include <Windows.h>
#endif


extern "C" {

	HVIC_USBSDKDLL bool HVIC_IniDepthAndOpenDefault();
	HVIC_USBSDKDLL bool HVIC_GetXyzIR(std::vector<float>& xyzir);
	HVIC_USBSDKDLL bool HVIC_ReleaseDepthAndClose();
	//
    HVIC_USBSDKDLL bool HVIC_IniRGBDAndOpenDefault();
	HVIC_USBSDKDLL bool HVIC_GetXyzRgb(std::vector<float>& xyz, unsigned char* rgb);
	HVIC_USBSDKDLL bool HVIC_ReleaseRgbDAndClose();
    
	HVIC_USBSDKDLL bool HVIC_XyziToColorIrZ(std::vector<float> xyza, unsigned char* color, unsigned char* irz);
    HVIC_USBSDKDLL float HVIC_GetDepthValue(std::vector<float> xyza, int indexX, int indexY);
    HVIC_USBSDKDLL bool HVIC_SaveDepthPoints_Plane(std::string fn, int items, int width, int height,
		                                     std::vector<float> points, std::vector<unsigned char> color);


}