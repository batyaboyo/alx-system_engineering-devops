# Client SSH configuration file so that you can
# connect to a server without typing a password.
include stdlib
file_line { 'Set private key file' :
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school'
}
file_line { 'Turn off password authenticaion':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no'
}
