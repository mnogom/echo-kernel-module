#!/usr/bin/env python3

import socket
import struct
import os


EKM_NETLINK = 30  # hardcoded

NLMSG_MIN_TYPE = 0x10
GENL_ID_CTRL = NLMSG_MIN_TYPE
NLM_F_REQUEST = 0x1


def render(msg: bytes) -> tuple:
    (msg_len, msg_type, msg_flags, msg_seq, msg_pid) = struct.unpack("IHHII", msg[:16])
    msg_payload = msg[16:]
    return {
        "len": msg_len,
        "type": msg_type,
        "flags": msg_flags,
        "seq": msg_seq,
        "pid": msg_pid,
        "payload": msg_payload,
    }


def create_msg(
    pid: int,
    text: str,
    type_: int = GENL_ID_CTRL,
    flags: int = NLM_F_REQUEST,
    seq: int = 1,
) -> bytes:
    msg_type = struct.pack("H", type_)
    msg_flags = struct.pack("H", flags)
    msg_seq = struct.pack("I", seq)
    msg_pid = struct.pack("I", pid)
    msg_payload = text.encode()
    msg_tail = msg_type + msg_flags + msg_seq + msg_pid + msg_payload
    msg_len = struct.pack("I", len(msg_tail) + 4)
    return msg_len + msg_tail


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
