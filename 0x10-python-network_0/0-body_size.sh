#!/bin/bash
# takes a url, sends request to the irl and displays the size of the body of the response
curl -sI "$1" | grep 'Content-Length' | cut -f2 -d' '
