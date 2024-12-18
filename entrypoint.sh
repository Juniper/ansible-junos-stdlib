#!/bin/bash

set +e

## Functions
function apk_add {
    echo "Installing additional OS packages"
    while IFS= read -r pkg
        do
        echo "Installing ${pkg}"
        apk add --no-cache -q "${pkg}"
        done < "$1"
}

function pip_install {
    echo "Installing Python packages"
    pip install -r "$1"
}

function galaxy_install {
    echo "Install Ansible Collections"
    ansible-galaxy install -r "$1"
}

function run_command {
    echo "Executing given commands"
    bash -c "$*"
}


if [ "$APK" ]; then APK=$APK
elif [ -f "/extras/apk.txt" ]; then APK="/extras/apk.txt"
else APK=''
fi

if [ "$REQ" ]; then REQ=$REQ
elif [ -f "/extras/requirements.txt" ];then REQ="/extras/requirements.txt"
else REQ=''
fi

if [ "$COLLECTIONS" ]; then COLLECTIONS=$COLLECTIONS
elif [ -f "/extras/requirements.yml" ]; then COLLECTIONS="/extras/requirements.yml"
else COLLECTIONS=''
fi


[[ -z "$APK" ]] || apk_add "$APK"

[[ -z "$REQ" ]] || pip_install "$REQ"

[[ -z "$COLLECTIONS" ]] || galaxy_install "$COLLECTIONS"

if [ -z "$1" ]
then
    echo "Starting an interactive Bash session"
    /bin/bash
else run_command "$*"
fi
