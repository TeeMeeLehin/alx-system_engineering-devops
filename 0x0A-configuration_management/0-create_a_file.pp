# Create a file resource with the path '/tmp/school'.

file { '/tmp/school':
    ensure  => 'file',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}
