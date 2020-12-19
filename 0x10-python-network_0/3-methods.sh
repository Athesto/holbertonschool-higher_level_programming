#!/bin/bash
# commnet
curl -sI "${1}" | grep Allow | sed -e 's/Allow: \(.*\)/\1/'
