# My Project 5 Documentation

# How to configure hostnames

- First I will ssh into my proxy server "ssh -i aws-ceg-3120 ubuntu@[server ip address]"

- Next in my home directory, I type "sudo nano /etc/hosts"

- I am then taken into a text editor where I can add the hosts of my two web servers using their private IP addresses

- I then type in the follow hosts in this format " IPAddress DomainName DomainAliases "

- Then I press Ctrl + X to exit and press Y to save my /etc/hosts document

![My /etc/hosts file](project5-1.png)

# How to SSH to your webservers

- First I create a new file to hold my private key using the "touch" command.

- Next, and thanks to adding my webservers to my /etc/hosts file, I can use the ssh command to connect to either webserver through my proxy server.

- I type "ssh -i aws-ceg3120 ubuntu@[hostname of webserver]

![Connecting to web server 1](project5-2.png)

![Connecting to web server 2](project5-3.png)