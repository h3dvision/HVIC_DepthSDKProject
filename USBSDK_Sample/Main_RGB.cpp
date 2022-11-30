#include <iostream>
#include <opencv2/opencv.hpp>
#include <HVIC_USBSDK.h>

int main(void){
	int width = 640; int height = 480;
	std::vector<float> xyzir(width * height * 4, 0);
	cv::Mat confImg(cv::Size(width, height), CV_8UC3, cv::Scalar(0, 0, 0));
	cv::Mat depthImg(cv::Size(width, height), CV_8UC3, cv::Scalar(0, 0, 0));
	cv::Mat rgbImg(cv::Size(width, height), CV_8UC3, cv::Scalar(0, 0, 0));
	if (!HVIC_IniRGBDAndOpenDefault())
		return -1;
	while (true) {
		if (!HVIC_GetXyzRgb(xyzir, rgbImg.data))
			return -1;
		if (!HVIC_XyziToColorIrZ(xyzir, depthImg.data, confImg.data))
			return -1;
		cv::imshow("DepthImage", depthImg); cv::imshow("RGbImage", rgbImg); // cv::imshow("IRImage", confImg); 
		std::cout << "Center Depth: " << HVIC_GetDepthValue(xyzir, width / 2, height / 2) << std::endl;
		if (cv::waitKey(60) == 'o')
			break;
	}
	HVIC_ReleaseRgbDAndClose();
	return 0;
}