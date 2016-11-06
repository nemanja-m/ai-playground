import cv2
import numpy as np

def count(img_path, DRAW=0):
    # Read image
    original = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Remove noise
    blurred = cv2.medianBlur(original, 5)
    binary = cv2.adaptiveThreshold(blurred.copy(),
                                   255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV,
                                   11,
                                   2)

    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()

    # Detect blobs.
    keypoints = detector.detect(binary)

    if DRAW:
        # Draw detected blobs as red circles.
        im_with_keypoints = cv2.drawKeypoints(blurred,
                                              keypoints,
                                              np.array( [] ),
                                              (0, 0, 255),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show keypoints
        cv2.imshow('Keypoints', im_with_keypoints)
        cv2.waitKey(0)

    return len(keypoints)

if __name__ == '__main__':
    print count('img-2.png')
