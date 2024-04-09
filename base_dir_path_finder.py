from pathlib import Path


def base_dir_path_finder(
        file_path: str,
        number_of_going_up: int = 2
) -> Path:
    """
    Find the base directory path based on the current file's location.

    This function takes the path of a file and determines the base
    directory path by going up a specified number of levels in the directory hierarchy.
    The base directory path is obtained by resolving the absolute path of the file and
    then repeatedly accessing its parent directory until the desired number of levels
    are reached.

    Args:
        file_path (str): The path of the file that runs this function, typically provided as the `__file__`
            global variable.
        number_of_going_up (int, optional): The number of levels to go up in the directory
            hierarchy to find the base directory. Defaults to 2.

    Returns:
        pathlib.Path: The base directory path as a `Path` object.

    Raises:
        None

    Notes:
        - The `file_path` argument should be passed as `__file__` to capture the current
          file's path automatically.
        - The `number_of_going_up` argument specifies the number of parent directory levels
          to traverse upwards from the file's location. By default, it is set to 2, which
          typically corresponds to going up two levels from the current file's directory
          to reach the base directory.
        - The base directory path is returned as a `Path` object from the `pathlib` module,
          which provides convenient methods for working with file and directory paths.

    """
    base_dir_path = Path(file_path).resolve()

    for i in range(number_of_going_up):
        base_dir_path = base_dir_path.parent

    return base_dir_path
