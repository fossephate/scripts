sudo apt install nginx mongodb nodejs npm build-essential python3 python3-pip certbot redis

sudo service nginx stop
sudo certbot certonly
sudo service nginx start