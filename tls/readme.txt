Client/Server exemplu de TLS 1.2
 - cules de la https://github.com/brandon-rhodes/fopnp/tree/m/py3/chapter06
 - de studiat și tst_tls.py și features.py 




#run server on localhost:
# python3.6 safe_tls.py -s localhost.pem '' 1060 


# verify 
# openssl s_client -CAfile ./ca.crt -connect localhost:1060 -tls1_2
# should return 
#  TLSv1.2
#  return code 0 (OK)
#  see sample in openssl.txt.out

#client also on localhost
# python3 safe_tls.py -a ca.crt localhost 1060 

#other examples
#check TLS 1.2 at Google:
# openssl s_client -connect google.com:443 -tls1_2

#check ciphers used by HTTPS at Google:
# nmap --script ssl-enum-ciphers -p 443 google.com


