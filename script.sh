
apt-get -qq update && apt-get -qq --yes install zabbix_agent
sudo systemctl stop zabbix_agent.service
wget https://github.com/Clublicious/zabbix/archive/refs/heads/main.zip
sudo unzip main.zip
sudo mkdir /home/zabbix/
sudo mv temp.py /home/zabbix/
sudo mv zabbix_agentd.conf /etc/zabbix/
sudo mv temp.conf /etc/zabbix/zabbix_agentd.conf.d/
sudo systemctl start zabbix_agent.service
