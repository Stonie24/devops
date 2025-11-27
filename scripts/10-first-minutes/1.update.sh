password="<password>"

echo "root:$password" | chpasswd
apt-get -y update
apt-get -y upgrade
