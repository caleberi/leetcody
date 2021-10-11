from optparse import OptionParser
def main():
    parser =  OptionParser()
    parser.add_option("-f","--file",dest="filename",help="write report to FILE",metavar="FILE")
    parser.add_option("-x","--xray",dest="xray",help="specify xray strength factor")
    parser.add_option(
        "-q",
        "--quiet",
        dest="verbose",
        default=True,
        action="store_false",
        help="don't print status message to stdout"
    )
    (options,args) = parser.parse_args()

    print("options: ",str(options))
    print("argument: ",args)

if __name__ == "__main__":
    main()