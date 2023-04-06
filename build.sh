#!/bin/bash
source ~/miniconda3/etc/profile.d/conda.sh

set -e
rm -rf ./python-x86_64.tar.bz2
rm -rf ./python
rm -rf ./piplist.txt
rm -rf ./python3.tbz

apt-get update
apt-get install python3-dev
apt install cmake
apt-get -y install g++
apt-get -y install gdb

conda activate
conda install -y nomkl
conda remove -y -n python-x86_64 --all
conda create -y -n python-x86_64 python=3.10

conda activate python-x86_64
conda install -y nomkl
conda install -y numpy
conda install -y scikit-image
conda install -y scipy
conda install -y pandas

conda install -y -c conda-forge matplotlib-base
conda install -y pip
yes | pip install ./autochain-6.2.3-py3-none-any.whl
yes | pip install ./daemontool-4.1.0.tar.gz
yes | pip install smbus
yes | pip install -r requirements.txt
conda deactivate

conda install -y -c conda-forge conda-pack
conda pack -p /root/miniconda3/envs/python-x86_64 -o ./python-x86_64.tar.bz2
conda deactivate

mkdir -p ./python
tar xf python-x86_64.tar.bz2 -C ./python
cd ./python/bin/
ln -s python3.10 python3.6
./python3.10 pip install cryptography==36.0.2
./python3.10 pip list --format=freeze > ../../piplist.txt
cd ../../
tar -cjf ./python3.tbz ./python/
echo "Done! you can diff the requirements.txt vs. the piplist.txt"
