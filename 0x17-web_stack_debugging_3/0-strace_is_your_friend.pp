# This Puppet manifest is used to fix the Apache 500 error

file_line { 'fix-apache':
  path  => '/var/www/html/wp-settings.php',
  line  => 'php',
  match => 'phpp',
}
