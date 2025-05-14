from django.conf import settings
import dropbox
import uuid

DROPBOX_ACCESS_TOKEN = settings.DROPBOX_ACCESS_TOKEN


def upload_to_dropbox(file_obj, filename=None):
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    filename = filename or f"{uuid.uuid4()}.jpg"
    dropbox_path = f"/carros/{filename}"

    dbx.files_upload(file_obj.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    shared_link = dbx.sharing_create_shared_link_with_settings(dropbox_path)
    return shared_link.url.replace("?dl=0", "?raw=1")
