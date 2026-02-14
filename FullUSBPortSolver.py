#!/usr/bin/env python3

import sys
import os
import pyshark

def read_pcap(file_path: str) -> None:
    """
    Read a PCAP file using PyShark
    """


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pcap_file>")
        sys.exit(1)

    pcap_file = sys.argv[1]

    if not os.path.isfile(pcap_file):
        print(f"[ERROR] File not found: {pcap_file}")
        sys.exit(1)

    read_pcap(pcap_file)


if __name__ == "__main__":
    main()
