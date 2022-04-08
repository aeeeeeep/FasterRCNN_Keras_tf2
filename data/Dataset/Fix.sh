#!/bin/bash

for x in *.jpg; do
    convert "$x"  "$x"
done
