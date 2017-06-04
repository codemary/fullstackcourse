#!/bin/bash

#Shell envioronment setup for linux and mac OS ased systems to install all the components
platform="unknown"
unamestr=`uname`

#Detect the OS type
echo $OSTYPE

if [ "$unamestr" = "Darwin" ]; then
    platform="MacOS"

    #Install home brew

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install bash-completion
    brew install python3
    brew link python3
    brew install gsl
    brew install git
    brew install nginx	
    brew install rsync
    brew install hadoop
    brew update
    pip3 install --upgrade pip

    pip3 install virtualenv
    pip3 install numpy
    pip3 install wget
    pip3 install sublime
    pip3 install pandas
    pip3 install statsmodels
    pip3 install pandas
    pip3 install bs4
    pip3 install requests
    pip3 install statsmodels
    pip3 install scikit-learn
    pip3 install clang
    pip3 install nltk
    pip3 install scrapy
    pip3 install seaborn
    pip3 install bokeh
    pip3 install networkX
    pip3 install flask
    pip3 install sed
    pip3 install awk
    pip3 install redis
    pip3 install psycopg2
    pip3 install mongodb
    pip3 install pystan
    pip3 install pymysql
    pip3 install django
    pip3 install sqlalchemy
    pip3 install spark
    pip3 install tensorflow
    pip3 install lxml
    
elif [ "$unamestr" = "Linux" ]; then
    platform="Linux"
 
#Python and Linux based package installation
   
    sudo apt-get install build-essential
    sudo apt-get install git
    sudo apt-get install bash-completion
    sudo apt-get install wget

    sudo apt-get install python3 python3-dev
    sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    sudo apt-get install python3-setuptools
    sudo apt-get install gsl-bin libgsl-dev
    sudo apt-get install mongodb
    sudo easy_install3 pip
    sudo pip3 install virtualenv
    sudo pip3 install requests

#Data Engineering and Full Stack Python Modules
 
    sudo pip3 install numpy
    sudo pip3 install scipy
    sudo pip3 install pandas
    sudo pip3 install bs4
    sudo pip3 install statsmodels
    sudo pip3 install nltk
    sudo pip3 install scrapy
    sudo pip3 install seaborn
    sudo pip3 install bokeh
    sudo pip3 install networkX
    sudo pip3 install flask
    sudo pip3 install redis
    sudo pip3 install psycopg2
    
    sudo pip3 install pymongo
    sudo pip3 install pystan
    sudo pip3 install pymysql
    sudo pip3 install django
    sudo pip3 install sqlalchemy
    sudo pip3 install spark
    sudo pip3 install tensorflow
    sudo pip3 install lxml
     
fi

#Setup mlpy module - Python Machine Learning Module
tar -xvf mlpy-3.5.0.tar
cd mlpy-3.5.0
sudo python3 setup.py install
