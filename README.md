# Uploading files to Shutterstock FTP
A script for Shutterstock contributors to upload their files from a given directory with a given extension to Shutterstock ftp.

## Getting Started

These instructions will get you a copy of the script running on your machine in order to upload your files to Shutterstock  

### Prerequisites

1. Python installed
  
2. Add your Shutterstock Contributor user and password as env vars in your bash profile:

```
echo 'export SHUTTERSTOCK_USER="<your user>"' >>~/.bash_profile
echo 'export SHUTTERSTOCK_PASS="<your password>"' >>~/.bash_profile
```
Check if it was added:

```
echo $SHUTTERSTOCK_PASS 
echo $SHUTTERSTOCK_PASS 
```
Reload bash_profile:

```
source .bash_profile
```

### Running the script

```
python ftp-upload.py <absolut path to the directory with images]> <file extension>
```