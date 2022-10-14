# A manifest that kills a process: killmenow

exec { 'pkill':
  command => '/usr/bin/pkill -f killmenow',
}
