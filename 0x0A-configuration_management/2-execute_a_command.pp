# A manifest that kills a process: killmenow

exec { 'killmenow':
  command => 'pkill killmenow',
}
