import pytest
import my_solution

cipher1 = "YFwoJeELOvlDVrOlNBDConouLwhdCC mkIjsYeKsuaGsDbSRJymLJVOaYNQRrgKBSifPOdnCbUleWCbf"
cipher2 = "HNABntvVepMaQSNHyKxQTXZf HVbQXcqJSXfswOAuRBzpefOdfBeylimeqDHDlFc"
cipher3 = "PqKgakYBpfzveAHVrrUgbzpkaMWUcskukxac QfsWpFSrTrwiaQRtSsXesGlrBqv"
cipher4 = "HXelrEed fCxojmVersu Gtehvee NSluGnJ"
cipher5 = "PHcRrveeRUmDnfqMFAnBJvvwyzSDrj tqXhrLRXIegaDLwdInIGCvqelcjzU"


def test_decryption():

    assert my_solution.decrypt(cipher1, 4) == 'Yellow submarine'
    assert my_solution.decrypt(cipher2, 7) == 'Hey Jude'
    assert my_solution.decrypt(cipher3, 3) == 'Paperback Writer'
    assert my_solution.decrypt(cipher4, 1) == 'Here Comes the Sun'
    assert my_solution.decrypt(cipher5, 5) == 'Penny Lane'
