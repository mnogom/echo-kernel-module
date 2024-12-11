#!/bin/bash -e

function build() {
  cd ./ekm-km/
  make
  echo "Kernel module was built"
  modinfo ./ekm.ko
}

function clean() {
  cd ./ekm-km/
  make clean
}

function install() {
  insmod ./ekm-km/ekm.ko
}

function uninstall() {
  rmmod ekm
}

function status() {
  [[ $(lsmod | grep "ekm") ]] && echo "Kernel EKM is installed" || echo "Kernel EKM is not installed"
}

function log() {
  dmesg -H --color=always | grep -i "ekm"
}

function client() {
  ./ekm-cl/client.py
}

case $1 in
build | b)
  build
  ;;
clean)
  clean
  ;;
install | i)
  install
  ;;
uninstall | u)
  uninstall
  ;;
status | s)
  status
  ;;
log | l)
  log
  ;;
client | c)
  client
  ;;
*)
  echo "Command '$1' not found"
  ;;
esac
