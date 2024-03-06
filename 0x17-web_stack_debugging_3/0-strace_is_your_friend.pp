# How to fix the Apache 500 error ez
file { '0-strace_is_your_friend.pp':
  ensure  => file,
  path    => '/root/0-strace_is_your_friend.pp',
  content => '
    # Use the exec resource type to run shell commands
    exec { "fix-apache":
      command => "/usr/bin/apt-get install -y apache2 && service apache2 restart",
      path    => ["/usr/bin", "/usr/sbin"],
    }
  ',
}
