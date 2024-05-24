# Using Puppet to change our server configuration files
file_line { 'configure using private key ~/.ssh/school':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '  IdentityFile ~/.ssh/school',
}

# Disable password authentication
file_line { 'authenticate using a password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '  PasswordAuthentication no',
}

file { '/etc/ssh/ssh_config':
  ensure => present,
}
