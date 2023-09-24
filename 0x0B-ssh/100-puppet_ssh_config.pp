# Create a Puppet class for managing SSH config file
class ssh_config {

  file { '~/.ssh/config':
    ensure  => present,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
    content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
  }
}

include ssh_config
