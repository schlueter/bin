#!/usr/bin/env bash

function find_above_curdir() {
  filename=$1
  if [[ -f "$filename" || -d "$filename" ]]; then
    echo $filename
  else
    find_above_curdir "../$filename"
  fi
}

find_above_curdir $1
