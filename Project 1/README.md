# My Project 1

# Create user 'git'

- I used ```sudo adduser git``` to create my user named 'git'.

- Switch over to 'git' using ```sudo su git```

# Give 'git' access to ssh capabilities

- Typing ```mkdir .ssh```, I have created a folder for my ssh keys for 'git' to use.

- Going into the .ssh directory of 'git', ```cd .ssh```, I type ```vim authorized_keys``` to open the vim text editor to create the file 'authorized_keys`.

- Opening another terminal, I type ```cat ceg3120-aws-vm.pem``` and copy the contents of my public key that I created in AWS.

- Back to the previous terminal with the vim text editor for 'authorized_keys' open, I press ```ESC key, i``` to insert the copied contents of my public key.

- I press 'ESC' again, then ```:wq authorized_keys``` to save and exit the file.

- Now I type ```cd ..``` to head back to the home directory.

# Making a connection to git using the 'ssh' command

- To test that I had done everything correctly, I first ```exit``` my AWS instance.

- Now, I type in ``` ssh -i ceg3120-aws-vm.pem git@<AWS_IP> ``` to make a connection to the user 'git' on my AWS instance.

- This will tell me that 'git' now has 'ssh' capabilities.
