# my first puppet, a i love school file creation
file
{ '/tmp/school':
  ensure  => 'file',
  path    => '/tmp/school',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
