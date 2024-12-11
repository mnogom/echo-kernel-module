#!/usr/bin/env python3

import socket
import struct
import os


EKM_NETLINK = 30  # hardcoded

NLMSG_MIN_TYPE = 0x10
GENL_ID_CTRL = NLMSG_MIN_TYPE
NLM_F_REQUEST = 0x1

NETLINK_HEADERS_TYPES = "IHHII"


def render(msg: bytes) -> tuple:
    final_string = "|> Headers\n"
    final_string += (
        "|len: {} | type: {} | flags: {} | seq: {} | pid: {}\n"
    ).format(*struct.unpack(NETLINK_HEADERS_TYPES, msg[:16]))
    final_string += "|> Payload\n"
    final_string += f"|{msg[16:]}"
    return final_string


def create_msg(
    pid: int,
    text: str,
    type_: int = GENL_ID_CTRL,
    flags: int = NLM_F_REQUEST,
    seq: int = 1,
) -> bytes:
    payload = text.encode()
    len_ = struct.calcsize(NETLINK_HEADERS_TYPES) + len(payload)
    return struct.pack(
        NETLINK_HEADERS_TYPES, len_, type_, flags, seq, pid
    ) + payload


def main():
    pid = os.getpid()
    sock = socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, EKM_NETLINK)
    sock.bind((0, pid))
    try:
        print("--> Print message to send")
        text = input("# ")
        request = create_msg(pid=pid, text=text)
        sock.send(request)
        print("--> Sent message:\n%s" % render(request))
        response = sock.recv(4096)
        print("--> Receive message:\n%s" % render(response))
    except KeyboardInterrupt:
        print("Interrupt")
    finally:
        sock.close()
        print("--> Socket was closed")


if __name__ == "__main__":
    main()
