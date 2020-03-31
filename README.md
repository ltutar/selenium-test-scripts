These selenium test scripts will be used as sanity test after deployment.

```bash
yum install -y ntp
ntpdate time.apple.com
# install java 1.8
yum install -y java-1.8.0-openjdk-devel
# install unzip
yum install -y unzip
# install wget. just in case
yum install -y wget


# install firefox
# firefox uses too much CPU, switched to Chrome
yum install -y firefox
# install geckodriver for selenium
curl -L "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz" -o /tmp/geckodriver-v0.26.0-linux64.tar.gz
tar xvzf /tmp/geckodriver-v0.26.0-linux64.tar.gz -C /tmp/
chown -R root:root /tmp/geckodriver
mv /tmp/geckodriver /opt/
ln -s /opt/geckodriver /usr/local/bin/geckodriver


# install chrome
{
        echo '[google-chrome]'
        echo 'name=google-chrome'
        echo 'baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch'
        echo 'enabled=1'
        echo 'gpgcheck=1'
        echo 'gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub'  
} >> /etc/yum.repos.d/google-chrome.repo 

yum install -y google-chrome-stable

# download the ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
curl -L "https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip" -o /tmp/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip -d /opt/
ln -s /opt/chromedriver /usr/local/bin/chromedriver


## SELENIUM

# install pip
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python2 get-pip.py

# install selenium
pip2 install selenium


# start selenium test
python2 /vagrant/selenium/good_test_chrome_no_proxy.py

python2 /vagrant/selenium/good_test_firefox_no_proxy.py
```
