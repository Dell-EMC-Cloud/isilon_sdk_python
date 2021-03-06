# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ChangelistsChangelistLinsExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ChangelistsChangelistLinsExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lins': 'list[ChangelistsChangelistLins]',
            'resume': 'str',
            'path': 'str',
            'total': 'int',
            'atime': 'ChangelistsChangelistLinsCtime',
            'size': 'int',
            'ctime': 'ChangelistsChangelistLinsCtime',
            'id': 'str',
            'mtime': 'ChangelistsChangelistLinsCtime',
            'type': 'str'
        }

        self.attribute_map = {
            'lins': 'lins',
            'resume': 'resume',
            'path': 'path',
            'total': 'total',
            'atime': 'atime',
            'size': 'size',
            'ctime': 'ctime',
            'id': 'id',
            'mtime': 'mtime',
            'type': 'type'
        }

        self._lins = None
        self._resume = None
        self._path = None
        self._total = None
        self._atime = None
        self._size = None
        self._ctime = None
        self._id = None
        self._mtime = None
        self._type = None

    @property
    def lins(self):
        """
        Gets the lins of this ChangelistsChangelistLinsExtended.


        :return: The lins of this ChangelistsChangelistLinsExtended.
        :rtype: list[ChangelistsChangelistLins]
        """
        return self._lins

    @lins.setter
    def lins(self, lins):
        """
        Sets the lins of this ChangelistsChangelistLinsExtended.


        :param lins: The lins of this ChangelistsChangelistLinsExtended.
        :type: list[ChangelistsChangelistLins]
        """
        self._lins = lins

    @property
    def resume(self):
        """
        Gets the resume of this ChangelistsChangelistLinsExtended.
        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).

        :return: The resume of this ChangelistsChangelistLinsExtended.
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """
        Sets the resume of this ChangelistsChangelistLinsExtended.
        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).

        :param resume: The resume of this ChangelistsChangelistLinsExtended.
        :type: str
        """
        self._resume = resume

    @property
    def path(self):
        """
        Gets the path of this ChangelistsChangelistLinsExtended.
        The path to the file associated with the entry.

        :return: The path of this ChangelistsChangelistLinsExtended.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ChangelistsChangelistLinsExtended.
        The path to the file associated with the entry.

        :param path: The path of this ChangelistsChangelistLinsExtended.
        :type: str
        """
        self._path = path

    @property
    def total(self):
        """
        Gets the total of this ChangelistsChangelistLinsExtended.
        Total number of items available.

        :return: The total of this ChangelistsChangelistLinsExtended.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ChangelistsChangelistLinsExtended.
        Total number of items available.

        :param total: The total of this ChangelistsChangelistLinsExtended.
        :type: int
        """
        self._total = total

    @property
    def atime(self):
        """
        Gets the atime of this ChangelistsChangelistLinsExtended.
        

        :return: The atime of this ChangelistsChangelistLinsExtended.
        :rtype: ChangelistsChangelistLinsCtime
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """
        Sets the atime of this ChangelistsChangelistLinsExtended.
        

        :param atime: The atime of this ChangelistsChangelistLinsExtended.
        :type: ChangelistsChangelistLinsCtime
        """
        self._atime = atime

    @property
    def size(self):
        """
        Gets the size of this ChangelistsChangelistLinsExtended.
        The size of the file associated with the entry.

        :return: The size of this ChangelistsChangelistLinsExtended.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ChangelistsChangelistLinsExtended.
        The size of the file associated with the entry.

        :param size: The size of this ChangelistsChangelistLinsExtended.
        :type: int
        """
        self._size = size

    @property
    def ctime(self):
        """
        Gets the ctime of this ChangelistsChangelistLinsExtended.
        

        :return: The ctime of this ChangelistsChangelistLinsExtended.
        :rtype: ChangelistsChangelistLinsCtime
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """
        Sets the ctime of this ChangelistsChangelistLinsExtended.
        

        :param ctime: The ctime of this ChangelistsChangelistLinsExtended.
        :type: ChangelistsChangelistLinsCtime
        """
        self._ctime = ctime

    @property
    def id(self):
        """
        Gets the id of this ChangelistsChangelistLinsExtended.
        The LIN number of the file associated with the entry.

        :return: The id of this ChangelistsChangelistLinsExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ChangelistsChangelistLinsExtended.
        The LIN number of the file associated with the entry.

        :param id: The id of this ChangelistsChangelistLinsExtended.
        :type: str
        """
        self._id = id

    @property
    def mtime(self):
        """
        Gets the mtime of this ChangelistsChangelistLinsExtended.
        

        :return: The mtime of this ChangelistsChangelistLinsExtended.
        :rtype: ChangelistsChangelistLinsCtime
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """
        Sets the mtime of this ChangelistsChangelistLinsExtended.
        

        :param mtime: The mtime of this ChangelistsChangelistLinsExtended.
        :type: ChangelistsChangelistLinsCtime
        """
        self._mtime = mtime

    @property
    def type(self):
        """
        Gets the type of this ChangelistsChangelistLinsExtended.
        Type of file.

        :return: The type of this ChangelistsChangelistLinsExtended.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ChangelistsChangelistLinsExtended.
        Type of file.

        :param type: The type of this ChangelistsChangelistLinsExtended.
        :type: str
        """
        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

