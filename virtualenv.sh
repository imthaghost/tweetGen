#!/usr/bin/env bash
# 28/05/2016 16:24:27
# devnull@libcrack.so

# V=3
VENV='venv'
# PYTHON='/usr/bin/python'      # 2.7
PYTHON='/usr/local/bin/python3' # 3.9

# [[ -n "${1}" ]] && V="${1}"

[[ "$BASH_SOURCE" == "${0}" ]] && {
    # myself="$(readlink -f "${0#-*}")"
    myself="$(realpath -e "${0#-*}")"
    # mydir="$(dirname "${myself}")"
    [[ -f "${PWD}/${myself##*/}" ]] && {
        printf ". ${myself##*/}\n" > /dev/stdout
    } || {
        printf "cp ${myself} . && . ${myself##*/}\n" > /dev/stdout
    }
    # printf "Usage: cp ${mydir}/${myself##*/} ${PWD}/ && . ${PWD}/${myself##*/}\n" > /dev/stderr
    exit 1
} || {
    [[ -d "${VENV}" ]] || {
        printf "\e[33m[W]\e[0m Creating virtual environment at \"${VENV}\"\n" > /dev/stdout
        # "virtualenv${V}" -p "${PYTHON}${V}" "${VENV}"
        virtualenv -p "${PYTHON}" "${VENV}"
    }
    printf "\e[32m[+]\e[0m Entering virtual environment \"${VENV}\"\n" > /dev/stdout
    if [ -f  "${VENV}/bin/activate" ]; then
        source "${VENV}/bin/activate"
    elif [ -f  "${VENV}/usr/local/bin/activate" ]; then
        source "${VENV}/usr/local/bin/activate"
    fi
    printf "\e[32m[+]\e[0m Done\n" > /dev/stdout
}

