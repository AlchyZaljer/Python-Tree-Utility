from pathlib import Path


DIR_NAME = None
MAX_LEVEL = None
ONLY_DIRS = None


def initialize(dir_name, only_dirs, max_level):
    global DIR_NAME, MAX_LEVEL, ONLY_DIRS
    DIR_NAME = dir_name
    MAX_LEVEL = max_level
    ONLY_DIRS = only_dirs


def process_tree():
    p = get_path()
    print_root()
    dirs_count, files_count = print_tree(p)
    print_calculations(dirs_count, files_count)


def print_root():
    print(DIR_NAME)


def print_tree(path):
    children = get_children(path)

    dirs_count = 1
    files_count = 0

    def traverse(children, level=1, prefix=""):
        nonlocal dirs_count, files_count

        for i, child_p in enumerate(children):
            child_name = child_p.name

            is_last = i == len(children) - 1
            print(prefix + ("└── " if is_last else "├── ") + child_name)

            if child_p.is_file():
                files_count += 1
            else:
                dirs_count += 1
                new_level = level + 1

                if MAX_LEVEL is None or new_level <= MAX_LEVEL:
                    sub_children = get_children(child_p)
                    new_prefix = prefix + ("    " if is_last else "│   ")

                    traverse(sub_children, new_level, new_prefix)

    traverse(children)

    return dirs_count, files_count


def print_calculations(dirs_count, files_count):
    output_str = dir_str(dirs_count)

    if not ONLY_DIRS:
        output_str += file_str(files_count)

    print(f"\n{output_str}")


def get_path():
    return Path(DIR_NAME) if DIR_NAME != "." else Path.cwd()


def get_children(parent_p):
    if ONLY_DIRS:
        children = [child_p for child_p in parent_p.iterdir() if child_p.is_dir()]
    else:
        children = [child_p for child_p in parent_p.iterdir() if not child_p.name.startswith("__")]

    return sorted(children)


def dir_str(dirs_count):
    return f"{dirs_count} {"directory" if dirs_count == 1 else "directories"}"


def file_str(files_count):
    return f", {files_count} {"file" if files_count == 1 else "files"}"
