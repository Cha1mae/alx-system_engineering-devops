# this will install nginx web server !!!

# This exec resource updates the system's package list
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# This package resource ensures that Nginx is installed
# it actually require 'update system' exec resource

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# This file resource manages the file at /var/www/html/index.html
# this will set the content to the specific html string

file { '/var/www/html/index.html':
  content => '<html><body>Hello World!</body></html>',
}

# This file resource manages the Nginx configuration file at /etc/nginx/sites-available/default
# set the content to the specific config if it changes ppup will refresh cause of the notify attribute

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html;
      server_name _;
      location / {
        try_files \$uri \$uri/ =404;
      }
      location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
  notify  => Service['nginx'],
}


# This service resource manages the Nginx service If the Nginx configuration file changes, Puppet will refresh the service

service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
