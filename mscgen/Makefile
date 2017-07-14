
SRC :=\
no_no_no_socks4\
no_no_no_tcp\
yes_yes_no_socks6\
no_no_no_socks6\
yes_yes_yes_socks6\
socks6\
socks6_short\
socks5\
trans_conv\
mp_convert

MSC := $(SRC:%=%.msc)
EPS := $(SRC:%=%.eps)
PNG := $(SRC:%=%.png)
SVG := $(SRC:%=%.svg)

all: $(EPS)

eps: $(EPS)

png: $(PNG)

svg: $(SVG)

%.eps: %.msc  
	mscgen -T eps -o $@ -i $< 

%.png: %.msc  
	mscgen -T png -o $@ -i $< 

%.svg: %.msc  
	mscgen -T svg -o $@ -i $< 

clean:
	rm -f $(EPS) $(PNG) $(SVG)
