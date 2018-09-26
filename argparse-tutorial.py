import argparse
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

group.add_argument("-v", "--verbosity", action="store_true", help="increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true",  help="decrease output verbosity")

args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
	print(answer)
elif args.verbosity:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
	print("{}^{} == {}".format(args.x, args.y, answer))
