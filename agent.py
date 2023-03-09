import os.path
import sys


def pre_main():
    current_file_path = os.path.relpath(__file__)
    current_dir = os.path.dirname(current_file_path)
    hook_dir = os.path.join(current_dir, 'hook')
    os.environ['PYTHONPATH'] = hook_dir


def main():
    command_args = sys.argv[1:]
    os.execl(sys.executable, sys.executable, *command_args)


if __name__ == '__main__':
    print("Agent start!")
    pre_main()
    print("Agent installation completed!")
    main()
