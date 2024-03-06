# fixin the Apache 500 error ez

exec { 'fix-apache':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
