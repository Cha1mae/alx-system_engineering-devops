0x14-mysql


- these are the steps to download mysql 5.7:

. sudo apt-key add signature.key
. sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
. sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
. sudo apt-get update
. sudo apt-cache policy mysql-server
. sudo apt install -f -y mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

*the signature key can be found in the link provided in the concept*
