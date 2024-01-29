# lets add a custum headr using puppet
# (i love puppet)

# Updating the  package list
exec { 'update':
  command  => 'apt-get update',
  provider => shell,
}

# Installing the  nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Adding the  custom HTTP response header to N config
file_line { 'headercustom':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => ':80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

# Ensuring the nginx service is running !
service { 'nginx':
  ensure  => running,
  require => File_line['headercustom'],
}
