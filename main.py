import time
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import api_hash, api_id
from datetime import datetime, timedelta
import argparse
import pytz
from telethon.tl.functions.account import UpdateProfileRequest

def valid_tz(s):
    try:
        return pytz.timezone(s)
    except:
        msg = "Not a valid tz: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser()
parser.add_argument("--api_id", required=False, help="user api ID", type=str, default=api_id)
parser.add_argument("--api_hash", required=False, help="user api Hash", type=str, default=api_hash)
parser.add_argument("--tz", required=False,  help="user api Hash", type=valid_tz, default=valid_tz('Asia/Tashkent'))

args = parser.parse_args()

client = TelegramClient("carpediem", args.api_id, args.api_hash)
client.start()


async def main():

    while True:
        await client(DeletePhotosRequest(await client.get_profile_photos('me')))  
        await client(UpdateProfileRequest(about='Forza Napoli'))
        await client(UploadProfilePhotoRequest(
            await client.upload_file('123.jpg')
        ))        
        time.sleep(30)
        await client(UpdateProfileRequest(about='Die Schwarzgelben'))
        await client(UploadProfilePhotoRequest(
            await client.upload_file('1234.jpg')
        ))
        time.sleep(30)
        await client(UpdateProfileRequest(about='Aupa Atleti'))
        await client(UploadProfilePhotoRequest(
            await client.upload_file('12345.jpg')
        ))
        time.sleep(30)

if __name__ == '__main__':
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
 