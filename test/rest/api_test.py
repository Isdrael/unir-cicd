import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
    
    def _assert_400(self, path):
        with self.assertRaises(HTTPError) as cm:
            urlopen(f"{BASE_URL}{path}", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, http.client.BAD_REQUEST)
    
    def test_api_add_success(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        self.assertEqual(response.read().decode(), "4")

    def test_api_add_invalid(self):
        self._assert_400("/calc/add/2/x")

    def test_api_substract_success(self):
        resp = urlopen(f"{BASE_URL}/calc/substract/5/4", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "1")

    def test_api_substract_invalid(self):
        self._assert_400("/calc/substract/5/y")

    def test_api_multiply_success(self):
        resp = urlopen(f"{BASE_URL}/calc/multiply/5/0", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "0")

    def test_api_multiply_invalid(self):
        self._assert_400("/calc/multiply/2/tres")

    def test_api_divide_success(self):
        resp = urlopen(f"{BASE_URL}/calc/divide/16/4", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "4.0")

    def test_api_divide_invalid_param(self):
        self._assert_400("/calc/divide/9/0")
    
    def test_api_power_success(self):
        resp = urlopen(f"{BASE_URL}/calc/power/5/5", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "3125")

    def test_api_power_invalid(self):
        self._assert_400("/calc/power/3/x")

    def test_api_sqrt_success(self):
        resp = urlopen(f"{BASE_URL}/calc/sqrt/49", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "7.0")

    def test_api_sqrt_invalid_param(self):
        self._assert_400("/calc/sqrt/x")

    def test_api_log10_success(self):
        resp = urlopen(f"{BASE_URL}/calc/log10/1000", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "3.0")
    
    def test_api_log10_invalid_param(self):
        self._assert_400("/calc/log10/x")

    def test_api_is_even_success(self):
        resp = urlopen(f"{BASE_URL}/calc/num_par/8", timeout=DEFAULT_TIMEOUT)
        self.assertEqual(resp.status, http.client.OK)
        self.assertEqual(resp.read().decode(), "True")

    def test_api_is_even_invalid_param(self):
        self._assert_400("/calc/num_par/6.6")