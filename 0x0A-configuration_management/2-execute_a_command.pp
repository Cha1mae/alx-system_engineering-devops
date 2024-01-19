# so this will kill a killmenow process
# the only if checks if the process is running bfor killing it
exec
{ 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep -f killmenow',
}
