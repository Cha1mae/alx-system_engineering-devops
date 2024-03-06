# How to fix the Apache 500 error ez
# This code executes a shell command using sed to
# replace all instances of "phpp" with "php" in the
# file /var/www/html/wp-settings.php
exec 
{ 'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
