import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'(youtube)', s):
        if re.search(r'(iframe)', s):
            s_parse = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
            groups = s_parse.groups()
            id = groups[3]
            return f"https://youtu.be/{id}"


if __name__ == "__main__":
    main()