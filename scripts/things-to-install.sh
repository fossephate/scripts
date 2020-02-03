sudo apt install nginx mongodb nodejs build-essential python3 python3-pip certbot

sudo service nginx stop
sudo certbot certonly
sudo service nginx start