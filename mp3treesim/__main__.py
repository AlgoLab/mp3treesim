import mp3treesim as mp3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='mp3treesim',  # TODO: fix this
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

    args = parser.parse_args()

    if args.i:
        mode = 'intersection'
    elif args.u:
        mode = 'union'
    elif args.g:
        mode = 'geometric'
    else:
        mode = 'sigmoid'

    tree1 = mp3.read_dotfile(args.trees[0])
    tree2 = mp3.read_dotfile(args.trees[1])

    score = mp3.similarity(tree1, tree2, mode=mode)
    print(score)


if __name__ == "__main__":
    main()
