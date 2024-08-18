# automated fix for apache fail

exec { 'fix_wordpress_inclusion':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/loca/bin/'],
}

