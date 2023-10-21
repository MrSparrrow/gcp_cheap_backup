from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Paul David\\Admin\\backups-361622-914538c2dd57.json"

client = storage.Client()
bucket = client.get_bucket('pd_cold_storage')
folder = sys.argv[1]
dirList = os.listdir("R:\\Backups\\Ashampoo\\" + folder)

count = 0
for dir in dirList:
    count += 1
#Will need to change based on how your backup software stores things
dirToUpload = dirList[count-3]

root = 'R:\\Backups\\Ashampoo\\' + folder + '\\' + dirToUpload

for root, dirs, files in os.walk(root):
    for dir in dirs:
        current = root + "\\" + dir
        print("current:" + current)
        for root2, dirs2, files2 in os.walk(current):
            for currentFile in files2:
                localPath = current + "\\" + currentFile
                remotePath = "Ashampoo\\" + folder + "\\" + localPath[localPath.index(folder)+11:]
                remotePath = remotePath.replace("\\", "/")
                blob = bucket.blob(remotePath)
                print("checking: " + remotePath)
                if (blob.exists()):
                    print("already exists...")
                else:
                    print("uploading...")
                    blob.upload_from_filename(localPath)
                    print("done")

        print("\n\n")

print("\n\nComplete\n\n")
exit()