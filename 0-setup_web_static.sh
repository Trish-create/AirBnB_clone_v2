#!/usr/bin/env bash
## Sets up the web server to serve web_static content using Nginx

## Install Nginx if it is not installed
if ! command -v nginx >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create the required directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a test HTML file
sudo tee /data/web_static/releases/test/index.html > /dev/null <<'EOF'
<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>
EOF

# Create or recreate the symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Ths command will give ubuntu ownership of everything inside /data
sudo chown -R ubuntu:ubuntu /data

#This will Configure Nginx to serve the static files
sudo tee /etc/nginx/sites-available/default > /dev/null <<'EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
       alias /data/web_static/current/;
       autoindex off;
    }
}
EOF

# This will test the Nginx configuration and restart Nginx
sudo nginx -t && sudo systemctl restart nginx

exit 0
