# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_image(self):
        """Test case for get_image

        Get an image
        """
        headers = { 
            'Accept': 'text/plain',
        }
        response = self.client.open(
            '/image/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_images(self):
        """Test case for list_images

        Get a list of images
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/list_images',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_upload_image(self):
        """Test case for upload_image

        Upload an image
        """
        headers = { 
            'Accept': 'text/plain',
            'Content-Type': 'multipart/form-data',
        }
        data = dict(sha1checksum='sha1checksum_example',
                    file_name='/path/to/file')
        response = self.client.open(
            '/upload_image',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
