import argparse
from foo_parameterization.core import foo_volume

def main():
    parser = argparse.ArgumentParser(description="Calculate the Foo et al. volume of a sphere.")
    parser.add_argument("radius", type=float, help="The radius of the sphere.")
    
    args = parser.parse_args()
    try:
        volume = foo_volume(args.radius)
        print(f"The volume of the sphere with radius {args.radius} is {volume:.2f}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()