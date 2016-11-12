
def main(argv):
    input_image = ''

    try:
        opts, args = getopt.getopt(argv, 'hi', ['help=', 'image='])
    except getopt.GetoptError:
        print '\nusage: python sum_digits.py -i <image>\n'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print '\nusage: python sum_digits.py -i <image>'
            print '\nOptions:'
            print '\t-h [--help], : Show help'
            print '\t-i [--image], : Path to the image'
            sys.exit()
        elif opt in ('-i', '--image'):
            input_image = arg

    print '\n' + str(sum_digits(input_image))

def __init__ == "__main__":
    main(sys.argv[1:])
