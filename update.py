import urllib.request

print('Beginning file update...')
 
urllib.request.urlretrieve ("https://github.com/xXxHotShotxXx/test/archive/master.zip","update.zip")

print('Update complete')
import zipfile
print('Beginning unzip update...')
zip_ref = zipfile.ZipFile("update.zip", 'r')
zip_ref.extractall("")
zip_ref.close()
print("unzip complete")
