# automated fix for apache fail

exec {'fix wordpress site':
	provider => shell,
	command => 'sudo sed -i "s/phpp/php/g" /var/www/html/wq-settings.php'
}
