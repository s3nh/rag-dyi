from cfg import RetrCFG
from huggingface_hub import snapshot_download


def main():
    snapshot_download(RetrCFG.model_name, local_dir = '../assets/retriever')

if __name__ == '__main__':
    main()
