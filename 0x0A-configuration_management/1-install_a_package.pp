# okay so i will try to install flask from pip3
# so i added python so that Puppet knows to install python3-pip
package
{ 'python3-pip':
  ensure => installed,
}

package
{ 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
