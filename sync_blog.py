import pathlib
import os
import re
from time import ctime
from pytz import timezone

from django.conf import settings
# settings.configure()
from django.utils import timezone as dtz

import mysite.blog.apps
from mysite.blog.models import Post


# only these methods would be needed to run the script from import
__all__ = ["sync_db", "load_content"]

content_path = os.path.join(os.getcwd(), "content", "blog")


def iter_files(path=content_path):
    """Generator to iterate through md blog post files"""
    directory = pathlib.Path(path)
    pattern = "*.md"

    for file in directory.glob(pattern):
        yield file


def fetch_data(file_text):
    """Fetch title and content from post file"""
    data = {}
    title = file_text.split("\n")[0][2:].strip()
    content = "\n".join(file_text.split("\n")[1:]).strip()
    return title, content


def get_id_from_filename(path):
    """Get id from filename.

    (e.g.: '1' in 'posts/1-hello-world.md')
    """
    pattern = re.compile(r"(\d+)-")
    filename = os.path.basename(path)
    return pattern.search(filename).group(1)


def load_content(path=content_path):
    """Return a data for each post as a list"""

    data_list = []
    ctime_format = "%a %b %d %H:%M:%S %Y"

    for file in iter_files(path):
        title, content = fetch_data(pathlib.Path(file).read_text())
        created = ctime(os.path.getctime(file))  # getting creation date/time
        created = dtz.datetime.strptime(created, ctime_format)
        # created.replace(tzinfo=timezone(settings.TIME_ZONE))

        data_list.append({
            "id": get_id_from_filename(file),
            "title": title,
            "content": content,
            "created": created
        })

    return data_list

def sync_db(data_list):
    """Check post files data against database"""
    all_rows = Post.objects.all()
    if len(all_rows) > len(data_list):
        # if any of the posts needs to be deleted
        ids = [item.get('id') for item in data_list]
        to_del = []
        for obj in all_rows:
            if not (obj.id in ids):
                obj.delete()

    # loop and check if any post needs to be created or updated
    for item in data_list:
        obj = Post.objects.filter(pk=item["id"])
        if not obj:  # if a file has not been created in DB yet
            post = Post(
                title=item["title"],
                content=item["content"],
                pub_date=item["created"],
            )
            post.save()
            continue
        if not (
            (obj.title == item["title"]) and
            (obj.content == item["content"])):
            # if any of the data needs to be updated
            obj.title = item["title"]
            obj.content = item["content"]
            obj.save()

# if __name__ == '__main__':
#     sync_db(load_content(content_path))