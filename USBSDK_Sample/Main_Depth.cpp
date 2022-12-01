#include <iostream>
#include <opencv2/opencv.hpp>
#include <HVIC_USBSDK.h>

int main(void){
	int width = 640; int height = 480;
	std::vector<float> xyzi(width * height * 4, 0);
	cv::Mat confImg(cv::Size(width, height), CV_8UC3, cv::Scalar(0, 0, 0));
	cv::Mat depthImg(cv::Size(width, height), CV_8UC3, cv::Scalar(0, 0, 0));
	if (!HVIC_IniDepthAndOpenDefault())
		return -1;
	while (true) {
		if (!HVIC_GetXyzIR(xyzi))
			return -1;
		if (!HVIC_XyziToColorIrZ(xyzi, depthImg.data, confImg.data))
			return -1;
		cv::imshow("IRImage", confImg); cv::imshow("DepthImage", depthImg);
		std::cout << "Center Depth: " << HVIC_GetDepthValue(xyzi, width / 2, height / 2) << std::endl;
		if (cv::waitKey(60) == 'o') {
			HVIC_SaveDepthPly();
			break;
		}
	}
	HVIC_ReleaseDepthAndClose();
	return 0;
}