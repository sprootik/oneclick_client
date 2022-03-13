#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import requests
from urllib3.exceptions import ConnectTimeoutError
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


class Logic:
    def _query(self, method: str, app: str, params: dict = None, data: str = None, out_format: str = 'xml', in_format: str = 'xml') -> dict | BeautifulSoup:
        """
        Args:
            method(str): defines the request method. GET, POST, PUT or DELETE.
            app (str): api object link
            params (dict, optional): request parameters. Defaults to None.
            data (str, optional): request data. Defaults to None.
            out_format (str, optional): out format in header, json or xml. Defaults to 'xml'.
            in_format (str, optional): in format in header, json or xml. Defaults to 'xml'..

        """
        if method == "GET":
            req = requests.get
        elif method == "POST":
            req = requests.post
        elif method == "PUT":
            req = requests.put
        elif method == "DELETE":
            req = requests.delete
        if out_format != "json" and out_format != "xml":
            raise AttributeError("incorrect out_format")
        if in_format != "json" and in_format != "xml":
            raise AttributeError("incorrect in_format")
        headers = {
            'accept': f"application/{out_format}; charset=UTF-8",
            'Content-Type': f"application/{in_format}; charset=UTF-8"
        }
        url = f"{self.server}/spectrum/restful/{app}"
        try:
            response = req(url, headers=headers, data=data, params=params, verify=self.verify,
                           timeout=self.timeout, auth=HTTPBasicAuth(self.user, self.password))
        except Exception as e:
            raise ConnectTimeoutError(e)
        else:
            answer = response.text
            soup = BeautifulSoup(answer, 'xml')
            try:
                err = soup.title.string
            except:
                if out_format == 'json':
                    try:
                        data = response.json()
                    except:
                        pass
                    else:
                        return data
                elif out_format == 'xml':
                    return soup
            else:
                raise RuntimeError(err)


class SpectrumClient(Logic):

    def __init__(self, server: str, user: str, password: str, verify: bool = True,
                 timeout: int = 60):
        """

        Args:
            server (str): link to server
            user (str): user
            password (str): password
            verify (bool, optional): verify ssl. Defaults to True.
            timeout (int, optional): connection timeout. Defaults to 60.
        """
        self.server = server
        self.user = user
        self.password = password
        self.verify = verify
        self.timeout = timeout

    def get(self, app: str, params: dict = None, data: str = None, out_format: str = 'xml',
            in_format: str = 'xml') -> dict | BeautifulSoup:
        """GET method

        Args:
            app (str): api object link
            params (dict, optional): request parameters. Defaults to None.
            data (str, optional): request data. Defaults to None.
            out_format (str, optional): out format in header, json or xml. Defaults to 'xml'.
            in_format (str, optional): in format in header, json or xml. Defaults to 'xml'.

        Raises:
            AttributeError:
            ConnectTimeoutError:
            RuntimeError:

        Returns:
            dict | BeautifulSoup: if out_format is json will return dict, if out_format is xml will return bs4 object
        """
        method = "GET"
        app = app
        params = params
        data = data
        out_format = out_format
        in_format = in_format
        self._query(method, app, params, data, out_format, in_format)

    def post(self, app: str, params: dict = None, data: str = None, out_format: str = 'xml',
             in_format: str = 'xml') -> dict | BeautifulSoup:
        """POST method

        Args:
            app (str): api object link
            params (dict, optional): request parameters. Defaults to None.
            data (str, optional): request data. Defaults to None.
            out_format (str, optional): out format in header, json or xml. Defaults to 'xml'.
            in_format (str, optional): in format in header, json or xml. Defaults to 'xml'.

        Raises:
            AttributeError:
            ConnectTimeoutError:
            RuntimeError:

        Returns:
            dict | BeautifulSoup: if out_format is json will return dict, if out_format is xml will return bs4 object
        """
        method = "POST"
        app = app
        params = params
        data = data
        out_format = out_format
        in_format = in_format
        self._query(method, app, params, data, out_format, in_format)

    def delete(self, app: str, params: dict = None, data: str = None, out_format: str = 'xml',
               in_format: str = 'xml') -> dict | BeautifulSoup:
        """DELETE method

        Args:
            app (str): api object link
            params (dict, optional): request parameters. Defaults to None.
            data (str, optional): request data. Defaults to None.
            out_format (str, optional): out format in header, json or xml. Defaults to 'xml'.
            in_format (str, optional): in format in header, json or xml. Defaults to 'xml'.

        Raises:
            AttributeError:
            ConnectTimeoutError:
            RuntimeError:

        Returns:
            dict | BeautifulSoup: if out_format is json will return dict, if out_format is xml will return bs4 object
        """
        method = "DELETE"
        app = app
        params = params
        data = data
        out_format = out_format
        in_format = in_format
        self._query(method, app, params, data, out_format, in_format)

    def put(self, app: str, params: dict = None, data: str = None, out_format: str = 'xml',
            in_format: str = 'xml') -> dict | BeautifulSoup:
        """PUT method

        Args:
            app (str): api object link
            params (dict, optional): request parameters. Defaults to None.
            data (str, optional): request data. Defaults to None.
            out_format (str, optional): out format in header, json or xml. Defaults to 'xml'.
            in_format (str, optional): in format in header, json or xml. Defaults to 'xml'.

        Raises:
            AttributeError:
            ConnectTimeoutError:
            RuntimeError:

        Returns:
            dict | BeautifulSoup: if out_format is json will return dict, if out_format is xml will return bs4 object
        """
        method = "PUT"
        app = app
        params = params
        data = data
        out_format = out_format
        in_format = in_format
        self._query(method, app, params, data, out_format, in_format)
