#!/bin/bash

update()
{
	git init
	git pull "https://github.com/nhsmith4/Laser-Tag" main

}

install_packages()
{
	echo "installing required packages..."
	sudo apt install python3-tk
	python3 -m venv path/to/venv
	source path/to/venv/bin/activate
	pip install psycopg2-binary
	
	update
}


if [ "$1" == "--install" ]; then
	install_packages
fi
if [ "$1" == "--update" ]; then
	echo "Updating to latest version..."
	update
fi

python3 main.py $*
