# Create a Puppet class for managing SSH config file
class ssh_config {

  file { '/etc/ssh/ssh_config':
    ensure  => present,
    mode    => '0600',
    content => "Host *\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\n",
  }
}

include ssh_config
