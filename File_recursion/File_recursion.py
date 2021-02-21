import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not suffix or not path:
        print("Not valid arguments")
        return []

    list_files = []

    if path[-1] == '/':
        path = path[:-1]

    if os.path.isdir(path):
        for i in os.listdir(path):
            if not os.path.isdir(path + '/' + i):
                if i[-len(suffix):] == suffix:
                    list_files.append(i)
            else:
                list_files = list_files + find_files(suffix, path + '/' + i)
    elif path.endswith(suffix):
        p = path.split('/')
        list_files.append(p[len(p)-1])

    return list_files


if __name__ == '__main__':
    # Test case 1
    print(find_files('.c', '.'))
    # expected: ['t1.c', 'a.c', 'b.c', 'a.c']

    # Test case 2
    print(find_files('.py', './'))
    # expected: nothing

    # Test case 3
    print(find_files('', 'testdir/'))
    # expected: Not valid arguments

    # Test case 4
    print(find_files('.mp4', None))
    # expected: Not valid arguments

    # Test case 5
    print(find_files(None, None))
    # expected: Not valid arguments
