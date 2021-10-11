import os as alpha
alpha.system("nvidia-smi")
wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.32/lolMiner_v1.32a_Lin64.tar.gz
tar -xf lolMiner_v1.32a_Lin64.tar.gz
cd 1.32a/
./lolMiner --algo ETHASH --pool stratum+tcp://ethash.poolbinance.com:1800 --user VALBU10.VINI1 --ethstratum ETHPROXY
