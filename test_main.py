import unittest
from main import get_system_info

class TestSystemInfo(unittest.TestCase):

    def test_get_system_info(self):
        system_info = get_system_info()

        # Перевірка чи є відома операційна система
        self.assertIsNotNone(system_info['os_version'])

        # Перевірка чи є відомий процесор
        self.assertIsNotNone(system_info['processor'])

        # Перевірка чи є відома кількість ядер процесора
        self.assertIsNotNone(system_info['num_cores'])

        # Перевірка чи є відомий обсяг пам'яті
        self.assertIsNotNone(system_info['total_memory'])

if __name__ == '__main__':
    unittest.main()
