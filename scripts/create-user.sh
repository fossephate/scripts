
# todo: make fully automatic:

# create user
adduser fosse
usermod -aG sudo fosse

# copy ssh keys from root:
mkdir -p /home/fosse/.ssh
cp ~/.ssh/authorized_keys /home/fosse/.ssh/authorized_keys


# remove root ssh key:
rm ~/.ssh/authorized_keys

# disable root login:
sudo nano /etc/ssh/sshd_config
# set "PermitRootLogin no"
# set "PermitEmptyPasswords yes"
sudo service sshd restart
# set root password to something else:
passwd