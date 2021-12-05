from unittest import main
from unittest import TestCase
from typing import NoReturn
from service import python
from service import java


class BaseTestCase(TestCase):

    def test_python(self) -> NoReturn:
        """
        test python style checker
        """

        result = python.check(
            1, "print('hello world')\nprint('hello world')"
        )
        self.assertEqual(type(result["score"]), type(""))
        self.assertEqual(type(result["wrong"]), type([]))

    def test_java(self) -> NoReturn:
        """
        test java style checker
        """

        src = '''
import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();
        System.out.println((a+b+1));  
    }
}
'''

        result = java.check(
            1, src
        )
        self.assertEqual(type(result["score"]), type(""))
        self.assertEqual(type(result["wrong"]), type([]))

if __name__ == '__main__':
    main()
