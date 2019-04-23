#!/usr/bin/bash
DEST=${HOME}/.fonts
#DEST=/usr/share/fonts/opentype
REPO=https://github.com/adobe-fonts/source-code-pro.git
BRANCH=release

git clone --depth 1 --branch ${BRANCH} ${REPO} ${DEST}
fc-cache -f -v
