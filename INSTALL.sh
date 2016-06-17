#!/bin/bash

echo "working directory" ${pwd}
sudo cp data/db_displayd.service /etc/systemd/system/
systemctl enable db_displayd
systemctl start db_displayd 

