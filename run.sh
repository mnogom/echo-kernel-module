#!/bin/bash

function build() {
  make
}

function clean() {
  make clean
}

function install() {
  insmod ./ekm.ko
}

function uninstall() {
  rmmod ekm
}

function status() {
  echo $(lsmod | grep "ekm") || echo "ekm is not installed"
}

function log() {
  dmesg | grep -i "ekm"
}

case $1 in
build | b)
  build
  ;;
clean | c)
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
*)
  echo "Command '$1' not found"
  ;;
esac
