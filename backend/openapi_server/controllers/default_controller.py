import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server import util
from flask import make_response

import hashlib 

def get_image(id_):  # noqa: E501
    """Get an image

    Retrieves an image from the backend. # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    try:
        with open(id_, "rb") as f:
            response = make_response(f.read())
            response.headers.set("Content-Type", "image/*")
            return response
    except:
        return 'Not Found', 404


def list_images():  # noqa: E501
    """Get a list of images

    Retrieves a list of available image URLs # noqa: E501


    :rtype: Union[List[str], Tuple[List[str], int], Tuple[List[str], int, Dict[str, str]]
    """
    images = ["/image/test.jpg"]
    return images


def upload_image(sha1checksum, file_name):  # noqa: E501
    """Upload an image

    Store an image to the backend. File is verified with a checksum. # noqa: E501

    :param sha1checksum: 
    :type sha1checksum: str
    :param file_name: 
    :type file_name: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    # This SHOULD just be a string but for some reason the backend wouldn't recognize the parameter unless it is a file
    # (some kind of issue in the API spec?) TODO: use a string instead
    checksum = sha1checksum.read().decode("utf-8").split(' ')[0]

    data = file_name.read()
    m = hashlib.sha1()
    m.update(data)
    calculated_sha1 = m.hexdigest()
    if calculated_sha1 != checksum:
        return f"Checksum mismatch: (received:{checksum} calculated:{calculated_sha1})", 403

    with open("test.jpg", "wb") as f:
        f.write(data)
    
    return "/images/test.jpg", 200
