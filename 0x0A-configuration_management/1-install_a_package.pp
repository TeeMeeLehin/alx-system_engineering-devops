# Ensure Flask is installed via pip3 with version 2.1.0

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
