# okay so i will try to install flask from pip3
# so i added python so that Puppet knows to install python3-pip
Install Python 3
package { 'python3':
    ensure   => installed,
}
Install Flask using pip3
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3']
}
Install Werkzeug using pip3
package { 'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
    require  => Package['flask']
}
