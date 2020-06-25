import mp3treesim as mp3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='MP3 tree similarity measure',
        add_help=True)

    parser.add_argument('trees', metavar='TREE', nargs=2,
                        help='Paths to the trees')

    group_mode = parser.add_mutually_exclusive_group()
    group_mode.add_argument('-i', action='store_true', default=False,
                            help='Run MP3-treesim in Intersection mode.')
    group_mode.add_argument('-u', action='store_true', default=False,
                            help='Run MP3-treesim in Union mode.')
    group_mode.add_argument('-g', action='store_true', default=False,
                            help='Run MP3-treesim in Geometric mode.')
    parser.add_argument('-c', '--cores', action="store", default=1, type=int,
                        help='Number of cores to be used in computation. ' +
                        'Set to 0 to use all the cores available on the machine. ' +
                        '(Default 1)')
    parser.add_argument('--labeled-only', action='store_true', default=False,
                        help='Ingore nodes without "label" attribute. ' +
                        'The trees will be interpred as partially-label trees.')
    parser.add_argument('--exclude', nargs='*', required=False, type=str,
                        help='String(s) of comma separated labels to exclude from computation. ' +
                        'If only one string is provided the labels will be excluded from both trees. ' +
                        'If two strings are provided they will be excluded from the respective tree. ' +
                        'E.g.: --exclude "A,D,E" will exclude labels from both trees; ' +
                        '--exclude "A,B" "C,F" will exclude A,B from Tree 1 and C,F from Tree 2; ' +
                        '--exclude "" "C" will exclude C from Tree 2 and nothing from Tree 1')
    args = parser.parse_args()

    if args.i:
        mode = 'intersection'
    elif args.u:
        mode = 'union'
    elif args.g:
        mode = 'geometric'
    else:
        mode = 'sigmoid'

    exclude_t1 = list()
    exclude_t2 = list()

    if args.exclude == None:
        exclude_t1 = exclude_t2 = None
    else:
        if len(args.exclude) == 0:
            exclude_t1 = exclude_t2 = None
        elif len(args.exclude) == 1:
            exclude_t1 = exclude_t2 = args.exclude[0].strip().split(',')
        elif len(args.exclude) == 2:
            exclude_t1 = args.exclude[0].strip().split(',')
            exclude_t2 = args.exclude[1].strip().split(',')
            if len(exclude_t1) == 0:
                exclude_t1 = None
            if len(exclude_t2) == 0:
                exclude_t2 = None
        else:
            print('Error: --exclude must have 0, 1 or 2 arguments')
            exit(1)

    tree1 = mp3.read_dotfile(
        args.trees[0], labeled_only=args.labeled_only, exclude=exclude_t1)
    tree2 = mp3.read_dotfile(
        args.trees[1], labeled_only=args.labeled_only, exclude=exclude_t2)

    score = mp3.similarity(tree1, tree2, mode=mode, cores=args.cores)
    print(score)


if __name__ == "__main__":
    main()
