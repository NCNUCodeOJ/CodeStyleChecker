from unittest import main
from unittest import TestCase
from typing import NoReturn
from service import python


class BaseTestCase(TestCase):

    def test_python(self) -> NoReturn:
        """
        test python style checker
        """

        result = python.check(
            1, "test", "print('hello world')\nprint('hello world')"
        )
        print(result)
        self.assertEqual(0, 0)


if __name__ == '__main__':
    main()
