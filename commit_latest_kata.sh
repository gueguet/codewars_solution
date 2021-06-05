#!/bin/bash

# $1 is your commit name, to be under " "

git add --all
git commit -m "$1"
git push origin master
