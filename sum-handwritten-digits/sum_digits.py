import sys
import getopt
from processing_utils import ImageUtils
from classifiers import Classifier

def sum_digits(image_path, clsf='knn'):
    # Initialize classifier, default classifier is kNN
    classifier = Classifier(clsf)

    # Get all regions containing digits, from image
    regions = ImageUtils.regions(image_path)

    # Classify each region into one digit and
    # sum all digits from all regions in given input image
    total = 0
    for region in regions:
        total += classifier.predict(region)

    return total

def main(argv):
    image_path = ''
    clsf = 'knn'

    try:
        opts, args = getopt.getopt(argv, 'hic', ['help=', 'image=', 'classifier='])
    except getopt.GetoptError:
        print '\nusage: python sum_digits.py -i <image>\n'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print '\nusage: python sum_digits.py -i <image>'
            print '\nOptions:'
            print '\t-h [--help],       : Show help'
            print '\t-i [--image],      : Path to the image'
            print '\t-c [--classifier], : Specify classifier. KNN (default) or CNN'
            sys.exit()
        elif opt in ('-i', '--image'):
            input_image = arg
        else:
            clsf = arg.lower()

    print '\nSum: ' + str(sum_digits(image_path))

if __name__ == "__main__":
    main(sys.argv[1:])
