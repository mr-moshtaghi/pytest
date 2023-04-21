import func


class TestFunc:
    def test_add(self):
        assert func.add(7, 3) == 10
        assert func.add(15, -4) == 11
        assert func.add(11, 0) == 11

    def test_subtract(self):
        assert func.subtract(7, 3) == 4
        assert func.subtract(15, -4) == 19
        assert func.subtract(11, 0) == 11

    def test_multiply(self):
        assert func.multiply(7, 3) == 21
        assert func.multiply(4, -3) == -12
        assert func.multiply(11, 0) == 0

    def test_division(self):
        assert func.division(21, 3) == 7
        assert func.division(15, -3) == -5
        assert func.division(11, 1) == 11
