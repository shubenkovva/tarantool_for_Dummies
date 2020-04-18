'''import azure.storage.blob.aio as storage
import asyncio
import datetime
from os import listdir
from os.path import isfile, join

mypath = '/Users/mac/Project/GeekBrains/tarantool_for_Dummies/Azure_Data_Lake/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

async def uploadBlob(blob_client,filename):
    async with blob_client as blob:
        with open(mypath+filename, "rb") as data:
            await blob.upload_blob(data)

blob = storage.BlobClient.from_connection_string("DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=dlshubenkov;AccountKey=zGkMO6aCF3CncktB9m7RzuxUUApWuzXq22AUoaYiJFIYQ4n8eoqRDwwOOb6OVGSRncxnGcIPJdK4NHB2DkY5Ow==", container_name="dlcontainer", blob_name="my_blob_asynch_1.txt")
loop = asyncio.get_event_loop()
for i in onlyfiles:
    print('Start=', i,' ',datetime.datetime.now())
    loop.run_until_complete(uploadBlob(blob,i))
    print('End=', i, ' ',datetime.datetime.now())'''


from azure.storage.blob import BlobClient
blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=dlshubenkov;AccountKey=zGkMO6aCF3CncktB9m7RzuxUUApWuzXq22AUoaYiJFIYQ4n8eoqRDwwOOb6OVGSRncxnGcIPJdK4NHB2DkY5Ow==", container_name="dlcontainer", blob_name="my_blob_synch_1.txt")

with open("/Users/mac/Project/GeekBrains/tarantool_for_Dummies/Azure_Data_Lake/testfile_1", "rb") as data:
    blob.upload_blob(data)