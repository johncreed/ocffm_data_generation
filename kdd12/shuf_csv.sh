#!/bin/bash

head -n1 $1 > $1.shuf
tail -n +2 $1 | shuf >>  $1.shuf
