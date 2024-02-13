0x14-mysql


# these are the steps to download mysql 5.7:

1. sudo apt-key add signature.key

2. sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C

3. sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

4. sudo apt-get update

5. sudo apt-cache policy mysql-server

6. sudo apt install -f -y mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*


*the signature key can be found in the link provided in the concept*
