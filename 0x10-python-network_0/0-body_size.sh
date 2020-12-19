#!/bin/bash
# commnet
curl -sI "${1}" | grep "Content-Len" | cut -d" " -f2
