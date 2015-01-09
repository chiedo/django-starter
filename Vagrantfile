VAGRANTFILE_API_VERSION = "2"

# These are the scripts that will be run by the terminal upon creation of a new machine.
# The answer 'yes' is piped into the commands that require 'Y' as user input
$script = <<SCRIPT
sudo debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password root'
sudo apt-get install -y python-software-properties software-properties-common
sudo add-apt-repository -y ppa:pi-rho/dev
sudo apt-get update
sudo apt-get install -y tmux=1.9a-1~ppa1~t
sudo apt-get -y install mysql-server-5.5
sudo apt-get -y install libmysqlclient-dev
sudo apt-get -y install unzip
sudo apt-get -y remove git 
sudo apt-get -y install libpq-dev
sudo apt-get -y install nodejs nodejs-legacy npm
sudo apt-get -y install python2.7 python2.7-dev
sudo apt-get -y install libjpeg-dev libfreetype6-dev zlib1g-dev
sudo apt-get -y install python-django
sudo apt-get -y install python-pip build-essential 
sudo apt-get -y install python-mysqldb
sudo pip install --upgrade pip
sudo pip install django==1.7
sudo apt-get -y install git
sudo gem install sass
sudo apt-get -y install vim-nox
sudo apt-get -y install sqlite3 libsqlite3-dev
sudo npm install -g yuglify
sudo update-rc.d mysql defaults

# sets up mysql server
if [ ! -f /var/log/databasesetup ];
then
    echo "CREATE DATABASE django_app_default" | mysql -uroot -proot

    touch /var/log/databasesetup
    echo "CREATE USER 'root'@'%' IDENTIFIED BY 'root';" | mysql -uroot -proot
    #make mysql listen to connections from the outside
    echo "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;" | mysql -uroot -proot
    echo "FLUSH PRIVILEGES;" | mysql -uroot -proot
    sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/my.cnf
    sudo service mysql restart
fi

# This sets up dev environment variables
if [ ! -f /var/log/devenv ];
then
  cd
  #DJANGO
  echo 'export DJANGO_ENV="development"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export DJANGO_SECRET_KEY="NONE"' | sudo tee -a /home/vagrant/.bashrc
  #MYSQL
  echo 'export MYSQL_DATABASE="django_app_default"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export MYSQL_USERNAME="root"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export MYSQL_PASSWORD="root"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export MYSQL_HOSTNAME="127.0.0.1"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export MYSQL_PORT=3306' | sudo tee -a /home/vagrant/.bashrc
  # AWS
  echo 'export AWS_ACCESS_KEY_ID="NONE"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export AWS_SECRET_ACCESS_KEY="NONE"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export AWS_STORAGE_BUCKET_NAME="NONE"' | sudo tee -a /home/vagrant/.bashrc
  echo 'export AWS_S3_BUCKETLESS_DOMAIN="NONE"' | sudo tee -a /home/vagrant/.bashrc
  touch /var/log/devenv
fi


SCRIPT


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # forward the python runserver port
  config.vm.network "forwarded_port", guest: 8000, host: 3001
  # forward postgresql
  config.vm.network "forwarded_port", guest: 3306, host: 5433

  # run the script from above
  config.vm.provision "shell", inline: $script
  config.vm.synced_folder ".", "/vagrant", :mount_options => ['dmode=777,fmode=666']
end
