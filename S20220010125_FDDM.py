import cv2
import numpy as np

def main():
    # Load input image
    img1 = cv2.imread('./image1.png', cv2.IMREAD_GRAYSCALE)
    if img1 is None:
        print("Error loading image1!")
        return

    # 1. Keypoint Detection using Harris Corner
    harris_corners = np.zeros_like(img1, dtype=np.float32)
    
    # Harris corner detection
    harris_corners = cv2.cornerHarris(img1, 2, 3, 0.04)
    harris_normalized = np.empty_like(harris_corners)
    cv2.normalize(harris_corners, harris_normalized, 0, 255, cv2.NORM_MINMAX)

    # Convert to 8-bit image
    harris_scaled = cv2.convertScaleAbs(harris_normalized)

    # Mark corners on the image
    for i in range(harris_normalized.shape[0]):
        for j in range(harris_normalized.shape[1]):
            if int(harris_normalized[i, j]) > 200:
                cv2.circle(img1, (j, i), 5, (255,), 2)

    # 2. Feature Description using SIFT
    sift = cv2.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)

    # Draw keypoints on the image
    img_keypoints1 = cv2.drawKeypoints(img1, keypoints1, None, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    # 3. Feature Matching using SSD and Ratio Distance
    img2 = cv2.imread('./image2.png', cv2.IMREAD_GRAYSCALE)
    if img2 is None:
        print("Error loading image2!")
        return

    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # BFMatcher with L2 norm (since SIFT uses Euclidean distance)
    bf_matcher = cv2.BFMatcher(cv2.NORM_L2)
    knn_matches = bf_matcher.knnMatch(descriptors1, descriptors2, k=2)

    # Apply the ratio test for good matches
    good_matches = []
    for m, n in knn_matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Draw matches
    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Show results
    cv2.imshow("Harris Corners", harris_scaled)
    cv2.imshow("Keypoints 1", img_keypoints1)
    cv2.imshow("Matches", img_matches)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
