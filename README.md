# Echo Kernel Module (TBD)

## Limitations & Dependencies
_TBD_


## Usage:
```bash
# Build kernel module
./run.sh build  # or `b`
# Clean build dir
./run.sh clean
# Install kernel module
./run.sh install  # or `i`
# Remove kernel module
./run.sh uninstall  # or `u`
# Show if kernel module is installed
./run.sh status  # or `s`
# Show message from `dmesg` grepped by kernel module
./run.sh log  # or `l`
# Send request to kernel module
./run.sh request  # or `r`
# Run client from userspace. Send/Receive message
./run.sh client  # or `c`
```

## Roadmap

- [x] "Hello, World!" `tag: 0.1.0`
- [x] Kernel that answer something on client request via NetLink `tag: 0.2.x`
- [ ] Kernel that echo payload to client request
- [ ] Using Generic NetLink
- [ ] [libnl](https://www.infradead.org/~tgr/libnl/)
- [ ] ???


## Sources
1. Hello, World: https://www.cyberciti.biz/tips/compiling-linux-kernel-module.html
2. Netlink example: https://dev.to/zqiu/netlink-communication-between-kernel-and-user-space-2mg1
3. https://docs.kernel.org/userspace-api/netlink/intro.html

