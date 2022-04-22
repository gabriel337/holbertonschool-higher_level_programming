#!/bin/bash
# Takes in URL, send DELETE request, display response body
curl -sX DELETE "$1"
