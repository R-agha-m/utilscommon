# """ ANSI color codes """
class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    # """ ANSI format end codes """
    END = "\033[0m"


# """ ANSI format codes """
class Formats:
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    # """ ANSI format end codes """
    END = "\033[0m"



if __name__ == "__main__":
    print(Colors.BLACK + "<<<< BLACK >>>>" + Colors.END)
    print(Colors.RED + "<<<< RED >>>>" + Colors.END)
    print(Colors.GREEN + "<<<< GREEN >>>>" + Colors.END)
    print(Colors.BROWN + "<<<< BROWN >>>>" + Colors.END)
    print(Colors.BLUE + "<<<< BLUE >>>>" + Colors.END)
    print(Colors.PURPLE + "<<<< PURPLE >>>>" + Colors.END)
    print(Colors.CYAN + "<<<< CYAN >>>>" + Colors.END)
    print(Colors.LIGHT_GRAY + "<<<< LIGHT_GRAY >>>>" + Colors.END)
    print(Colors.DARK_GRAY + "<<<< DARK_GRAY >>>>" + Colors.END)
    print(Colors.LIGHT_RED + "<<<< LIGHT_RED >>>>" + Colors.END)
    print(Colors.LIGHT_GREEN + "<<<< LIGHT_GREEN >>>>" + Colors.END)
    print(Colors.YELLOW + "<<<< YELLOW >>>>" + Colors.END)
    print(Colors.LIGHT_BLUE + "<<<< LIGHT_BLUE >>>>" + Colors.END)
    print(Colors.LIGHT_PURPLE + "<<<< LIGHT_PURPLE >>>>" + Colors.END)
    print(Colors.LIGHT_CYAN + "<<<< LIGHT_CYAN >>>>" + Colors.END)
    print(Colors.LIGHT_WHITE + "<<<< LIGHT_WHITE >>>>" + Colors.END)

    print(Formats.BOLD + "<<<< BOLD >>>>" + Formats.END)
    print(Formats.FAINT + "<<<< FAINT >>>>" + Formats.END)
    print(Formats.ITALIC + "<<<< ITALIC >>>>" + Formats.END)
    print(Formats.UNDERLINE + "<<<< UNDERLINE >>>>" + Formats.END)
    print(Formats.BLINK + "<<<< BLINK >>>>" + Formats.END)
    print(Formats.NEGATIVE + "<<<< NEGATIVE >>>>" + Formats.END)
    print(Formats.CROSSED + "<<<< CROSSED >>>>" + Formats.END)
