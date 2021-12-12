#!/bin/sh

numLines=${1:-100}
shuf -i 0-2500 -rn "${numLines}" | paste -sd ','
