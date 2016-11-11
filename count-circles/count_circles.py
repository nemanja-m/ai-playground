import cv2
import numpy as np
import sys, getopt

def count(img_path, DRAW=0):
    # Read image
    original = cv2.imread(img_path)

    # Make red color black
    red_only = original.copy()
    red_only[:, :, 2] = 0

    # Remove noise
    blurred = cv2.medianBlur(red_only, 5)

    # Make binary image
    binary = cv2.threshold(blurred, 50 , 255, cv2.THRESH_BINARY)[1]
    binary = cv2.cvtColor(binary, cv2.COLOR_BGR2GRAY)
    binary = cv2.threshold(binary, 0, 255, cv2.THRESH_BINARY)[1]

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
        cv2.imshow('Keypoints', np.hstack([im_with_keypoints, original, blurred]))
        cv2.waitKey(0)

    return len(keypoints)

def main(argv):
    input_file = ''
    plot = False

    try:
        opts, args = getopt.getopt(argv, 'phi:', ['plot=', 'help=', 'image='])
    except getopt.GetoptError:
        print '\nusage: python count_circles.py -i <image>\n'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ( '-h', '--help' ):
            print '\nusage: python count_circles.py -i <image>'
            print '\nOptions:'
            print '\t-h [--help]  : Show help'
            print '\t-i [--image] : Path to the image'
            print '\t-p [--plot]  : Plot results'
            sys.exit()
        elif opt in ( '-i', '--image' ):
            input_file = arg

        if opt in ( '-p', '--plot' ):
            plot = True

    print count(input_file, plot)

if __name__ == '__main__':
    main(sys.argv[1:])
