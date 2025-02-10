# Script to set up a new Ubuntu server with Nginx
# and add a custom HTTP header

# Update the system
exec { 'update_apt':
    command => '/usr/bin/apt-get update',
}

# Install Nginx
package { 'nginx':
    ensure => 'installed',
    require => Exec['update_apt']
}

# Create a simple index page
file {'/var/www/html/index.html':
    content => 'Hello World!'
}

# Set up a redirection rule
exec {'configure_redirection':
    command => 'sed -i "24i\	rewrite ^/redirect_me https://example.com/ permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

# Add a custom HTTP header
exec {'add_custom_http_header':
    command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

# Ensure Nginx service is running
service {'nginx':
    ensure => running,
    require => Package['nginx']
}
