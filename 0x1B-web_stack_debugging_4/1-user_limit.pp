# lotta files errors in a uers account
exec {'replace-hard':
    provider => shell,
    command  => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
    before   => Exec['replace-soft']
}

exec {'replace-soft':
    provider => shell,
    command  => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
