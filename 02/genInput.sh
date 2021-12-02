#!/bin/sh

MAXLINE=${1:-10}
MAXVAL=${2:-100}
feed=$(head -c 10 /dev/urandom)

printf 'up\ndown\nforward\n' |
    shuf -r -n "$MAXLINE" | awk -v seed="$feed" -v max="$MAXVAL" 'BEGIN{srand(seed);}{print $0" "int(rand() * max)}'
