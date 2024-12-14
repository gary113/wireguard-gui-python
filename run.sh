#!/bin/bash

LOCKFILE=/tmp/wgp.lock

if [ -f "$LOCKFILE" ]; then
  zenity --error --text="Another instance of wgp is already running"
  exit 1
fi

trap "rm -f $LOCKFILE" EXIT

touch $LOCKFILE

while true; do
  if output=$(zenity --password --title="Sudo password required"); then
    if echo "$output" | sudo -S true; then
      sudo /opt/wireguard-gui-python/venv/bin/python3 /opt/wireguard-gui-python/wgp.py
      break
    else
      zenity --error --text="Invalid sudo password"
    fi
  else
    break
  fi
done

exit 0
