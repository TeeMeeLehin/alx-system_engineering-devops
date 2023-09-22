# manifest to kill a process

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin:/usr/local/bin',
  refreshonly => true,
}
