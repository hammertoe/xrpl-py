from unittest import TestCase

from xrpl.models.amount import IssuedCurrency
from xrpl.models.exceptions import XRPLModelValidationException

_ACCOUNT = "r9LqNeG6qHxjeUocjvVki2XR35weJ9mZgQ"


class TestIssuedCurrency(TestCase):
    def test_correct_currency_code_format(self):
        obj = IssuedCurrency(
            currency="USD",
            value="100",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_correct_lower_currency_code_format(self):
        # lower case is discouraged but allowed
        obj = IssuedCurrency(
            currency="usd",
            value="100",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_incorrect_currency_code_format(self):
        # the "+" is not allowed in a currency format"
        with self.assertRaises(XRPLModelValidationException):
            IssuedCurrency(
                currency="+XX",
                value="100",
                issuer=_ACCOUNT,
            )

    def test_correct_hex_format(self):
        obj = IssuedCurrency(
            currency="0158415500000000C1F76FF6ECB0BAC600000000",
            value="100",
            issuer=_ACCOUNT,
        )
        self.assertTrue(obj.is_valid())

    def test_incorrect_hex_format(self):
        # the "+" is not allowed in a currency format"
        with self.assertRaises(XRPLModelValidationException):
            IssuedCurrency(
                currency="+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                value="100",
                issuer=_ACCOUNT,
            )

    def test_invalid_currency_length(self):
        # length of currency must be either 3 or 40
        with self.assertRaises(XRPLModelValidationException):
            IssuedCurrency(
                currency="XXXX",
                value="100",
                issuer=_ACCOUNT,
            )

    def test_xrp_currency_is_invalid(self):
        # issued currencies can't use XRP (just use a string amount then)
        with self.assertRaises(XRPLModelValidationException):
            IssuedCurrency(
                currency="XRP",
                value="100",
                issuer=_ACCOUNT,
            )

    def test_xrp_lower_currency_is_invalid(self):
        # issued currencies can't use XRP (just use a string amount then)
        with self.assertRaises(XRPLModelValidationException):
            IssuedCurrency(
                currency="xrp",
                value="100",
                issuer=_ACCOUNT,
            )
