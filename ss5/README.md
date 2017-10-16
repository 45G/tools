
apt install libssl1.0.0 libpam0g-dev 	libldap2-dev libssl-dev 

cd ss5-3.8.9

make && make install 

in /etc/opt/ss5/ss5.conf uncomment these lines:

auth    0.0.0.0/0               -               -

permit -        0.0.0.0/0       -       0.0.0.0/0       -       -       -       -       -



./src/ss5 -u root -b 141.85.241.250:5201 
