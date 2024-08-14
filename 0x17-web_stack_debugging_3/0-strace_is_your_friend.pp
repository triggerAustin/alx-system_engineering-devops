# automated fix for apache fail

exec {'fix wordpress site':
	command => 'sudo sed -i s/phpp/php/g /var/www/html/wq-settings.php',
	path => ['/bin', '/usr/bin/', '/usr/loca/bin/'],
}
