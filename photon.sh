#!/bin/bash

update()
{
	cd ./photon
	git init
	git pull "https://github.com/nhsmith4/Laser-Tag" main
	cd ../

}

install_packages()
{
	echo "installing required packages..."
	mkdir ./photon
	sudo apt-get install python3-pip
	sudo apt install python3-tk
	python3 -m venv path/to/venv
	source path/to/venv/bin/activate
	pip install psycopg2-binary
	pip install pillow
	pip install pygame
	
	update
}


if [ "$1" == "--install" ]; then
	install_packages
fi
if [ "$1" == "--update" ]; then
	echo "Updating to latest version..."
	update
fi

cd ./photon
python3 main.py $*
