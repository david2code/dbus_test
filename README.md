# reference
> http://just4coding.com/2018/07/31/dbus/

# install
sudo apt install libdbus-1-dev

# compile
gcc -o dbus-server dbus-server.c `pkg-config --libs --cflags dbus-1`
gcc -o dbus-client dbus-client.c `pkg-config --libs --cflags dbus-1`

# tools
busctl
