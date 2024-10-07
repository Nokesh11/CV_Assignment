# Computer Vision Project - README (macOS)

## Overview
This project implements a computer vision application using **OpenCV** in **Python** to demonstrate key concepts such as feature detection, description, and matching of images. The project was developed on **macOS** using **Python 3.x** and **OpenCV 4.10.0**.

## Assignment Objectives
The assignment has three parts:

1. **Keypoint detection**: Identify points of interest in the image using the Harris corner detection method.
2. **Feature description**: Compute the Scale-Invariant Feature Transform (SIFT) descriptor at each keypoint.
3. **Feature matching**: Match features using Sum of Squared Differences (SSD) and ratio distance. For ratio distance, find the closest and second closest features by SSD distance. The ratio is their division (i.e., SSD of the closest match divided by the SSD of the second closest).

## Prerequisites
* **Python 3.x** (ensure it's installed on macOS)
* **OpenCV 4.10.0** (with `contrib` modules for SIFT)
* **NumPy**
* Install packages via `pip` or Homebrew where needed.

## Installation & Setup

1. **OpenCV Installation with Homebrew**: Install OpenCV with Python support:
   ```bash
   brew install opencv
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install opencv-python opencv-contrib-python numpy
   ```

3. **Verify OpenCV Installation**: Ensure OpenCV is installed correctly:
   ```bash
   python -c "import cv2; print(cv2.__version__)"
   ```

4. **Project Setup**:
   * Ensure that image files (`img1.png` and `img2.png`) are in the same directory as the Python script, or adjust the paths accordingly.
   * The Python script provided implements Harris corner detection, SIFT feature extraction, and feature matching.

5. **Running the Code**: Navigate to the project directory and run the Python script:
   ```bash
   python new.py
   ```

## Troubleshooting

* **File Not Found**: If you encounter `can't open/read file` errors, verify that the image files are in the correct location and the file paths in the script are correct.

* **Missing Libraries**: If a library is missing, install it via `pip`:
   ```bash
   pip install <package_name>
   ```

## Key Steps

1. **Harris Corner Detection**: Detect and highlight corners in the image using the Harris algorithm.

2. **SIFT Feature Extraction**: Detect and describe features using the Scale-Invariant Feature Transform.

3. **Feature Matching**: Match keypoints between two images using SSD and apply the ratio test to filter out good matches.

## Conclusion

This project demonstrates the implementation of feature detection, description, and matching using OpenCV on macOS. The use of Python simplifies the development process while maintaining strong performance and functionality.

---
**Note**: For any additional questions or issues, please open an issue in this repository.
