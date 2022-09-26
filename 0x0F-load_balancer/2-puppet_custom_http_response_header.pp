# automate the task of creating a custom HTTP header response

exec {'update-sudo':
  provider => shell,
  command  => 'sudo apt-get -y update'
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx'
}

exec {'create new header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "/server_name _;/a \tadd_header X-Served-By $HOSTNAME;"" /etc/nginx/sites-enabled/default'
}

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart'
}
