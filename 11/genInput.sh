#!/bin/sh

lenght=${1:-10}
shuf -i 0-9 -rn $((lenght * lenght)) | paste -sd '' | fold -w "${lenght}"
