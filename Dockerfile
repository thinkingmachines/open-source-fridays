# Pandoc with a full TexLive installation and FiraSans font
FROM blang/latex:ubuntu 
MAINTAINER Lester James V. Miranda <lj@thinkingmachin.es>

# Install wget
RUN  apt-get update \
  && apt-get install -y wget 

# Install Pandoc
RUN wget https://github.com/jgm/pandoc/releases/download/2.7.1/pandoc-2.7.1-1-amd64.deb \
    && dpkg -i pandoc-2.7.1-1-amd64.deb

# Install Fira Sans Font
RUN wget https://github.com/bBoxType/FiraSans/archive/master.zip \
    && unzip master.zip \
    && mkdir -p /usr/share/fonts/opentype/fira \
    && mkdir -p /usr/share/fonts/truetype/fira \
    && find FiraSans-master/ -name "*.otf" -exec cp {} /usr/share/fonts/opentype/fira/ \; \
    && find FiraSans-master/ -name "*.ttf" -exec cp {} /usr/share/fonts/truetype/fira/ \;


