# https://askubuntu.com/questions/1065542/how-to-disable-mouse-acceleration-on-ubuntu-18-04
# sudo apt install dconf-editor

# sets the accelleration profile to 'flat'
gsettings set org.gnome.desktop.peripherals.mouse accel-profile "flat"