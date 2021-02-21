import ftplib
import os
import glob
import argparse

FTP_HOST = "ftps.shutterstock.com"

ftp_user = os.environ.get('SHUTTERSTOCK_USER')
frt_pass = os.environ.get('SHUTTERSTOCK_PASS')

parser = argparse.ArgumentParser(description='A script to upload photos from a given directory to Shutterstock ftp')
parser.add_argument("path", help="Absolut path to the directory with images.")
parser.add_argument("extension", help="File extension, for example jpg or jpeg.")
args = parser.parse_args()
path = args.path
extension = args.extension

# connect to the FTP server
session = ftplib.FTP_TLS(FTP_HOST, ftp_user, frt_pass)
session.prot_p()

count = 0
foundFiles = glob.glob(os.path.join(path, '*.' + extension))
for filenameWithPath in foundFiles:
    file = open(os.path.join(os.getcwd(), filenameWithPath), 'rb') # open in readonly mode
    basename = os.path.basename(filenameWithPath)
    session.storbinary('STOR ' + basename, file)  # send the file
    count = count + 1

    print('Uploaded file ' + basename)
    file.close()

session.quit()

print('Finished')
print('Number of found images with given extension: ', len(foundFiles))
print('Number of uploaded images: ', count)
