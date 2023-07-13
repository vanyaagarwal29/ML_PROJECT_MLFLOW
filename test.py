import argparse

#if you want to pass anything from the command line

if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--name", "-n", default="sunny", type=str)
    args.add_argument("--age", "-a", default=25.0, type=float)
    parse_args=args.parse_args()
    
    print(parse_args.name,parse_args.age)