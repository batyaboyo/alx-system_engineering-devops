# Installs puppet-lint 2.5.0 using puppet
package {'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
}
