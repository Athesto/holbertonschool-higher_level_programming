#!/bin/bash
# commnet
curl -sLI "${1}" | grep 200 &>/dev/null && curl -sLX "GET" "${1}"
