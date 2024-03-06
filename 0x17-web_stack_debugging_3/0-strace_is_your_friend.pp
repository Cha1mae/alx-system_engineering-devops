# How to fix the Apache 500 error ez
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => file('/var/www/html/wp-settings.php')
                 .content
                 .gsub('phpp', 'php'),
}
