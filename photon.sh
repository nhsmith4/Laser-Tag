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
	echo "installing..."
	mkdir ./photon
	
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
