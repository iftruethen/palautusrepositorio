import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 4")

    def test_kaksi_perakkaista_summaa(self):
        io = StubIO([
            "1", "3", "-9999",   # ensimmäinen lasku -> 4
            "2", "6", "-9999"    # toinen lasku -> 8
        ])

        laskin = Laskin(io)
        laskin.suorita()

        # Tarkistetaan, että molemmat tulokset tulostuivat oikein
        self.assertEqual(io.outputs[0], "Summa: 4")
        self.assertEqual(io.outputs[1], "Summa: 8")

