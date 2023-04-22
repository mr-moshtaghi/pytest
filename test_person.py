from person import Person
import pytest
import time


class TestPerson:
    @pytest.fixture
    def setup(self):
        self.p1 = Person("sajjad", "moshtaghi")
        self.p2 = Person("jack", "stark")
        yield 'setup'
        print("helllllllllllllllllllllowwwwwwwwwwwwwwwwwwwwwwwww")
        time.sleep(2)

    def test_full_name(self, setup):
        assert self.p1.full_name() == "sajjad moshtaghi"
        assert self.p2.full_name() == "jack stark"

    def test_email(self, setup):
        assert self.p1.email() == "sajjadmoshtaghi@gmail.com"
        assert self.p2.email() == "jackstark@gmail.com"

