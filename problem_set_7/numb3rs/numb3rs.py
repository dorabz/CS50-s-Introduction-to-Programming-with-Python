import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    isip = re.match(r"^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$", ip)
    return bool(isip)


...


if __name__ == "__main__":
    main()