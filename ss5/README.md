
# apt install libssl1.0.0 libpam0g-dev 	libldap2-dev libssl-dev 
# cd ss5-3.8.9
# make && make install 

in /etc/opt/ss5/ss5.conf setup appropriate networks to be accepted:

 auth    0.0.0.0/0               -               -

 permit -        188.26.0.0/16   -       0.0.0.0/0       -       -       -       -       -

 permit -        141.85.0.0/16   -       0.0.0.0/0       -       -       -       -       -

 permit -        93.0.0.0/8      -       0.0.0.0/0       -       -       -       -       -

# ss5 -u root -b 141.85.241.250:5201 
