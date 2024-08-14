# automated fix for apache fail

file { '/var/www/html/wp-settings.php':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
  source => 'puppet:///modules/mymodule/wp-settings.php', # Ensure this file is managed by Puppet
  notify => Service['apache2'],
}

exec { 'fix_wordpress_inclusion':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  unless  => 'grep -q "class-wp-locale.php" /var/www/html/wp-settings.php',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_wordpress_inclusion'], # Restart Apache if the exec changes the file
}

