import sys 
sys.path.insert(0, '../')
from src.cfg import RagCFG, ChromaStorage


def main():
    print(dir(RagCFG))
    print(dir(ChromaStorage))

if __name__ == '__main__':
    main()