#!/bin/bash

set -e

for f in images/*.webp images/*.jpg; do
    if [[ ! -e $f ]]; then
        continue
    fi
    filename=$(basename "$f")
    if [[ $f == *.webp ]]; then
        dwebp "$f" -o "dataset/${filename%.webp}.png"
    elif [[ $f == *.jpg ]]; then
        magick "$f" "dataset/${filename%.jpg}.png"
    fi
done
