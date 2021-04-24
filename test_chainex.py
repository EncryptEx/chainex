# unit test
import datetime
import corechainex
import time
numoftests = 0

def chainextest(numoftests):
   
    # do not change this variables
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "0", "")[0]) >= 10, "No result encryption expected. MODE =  0"
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "1", "")[0]) >= 10, "No result encryption expected. MODE =  1"
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "2", "")[0]) >= 10, "No result encryption expected. MODE =  2"
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "3", "")[0]) >= 10, "No result encryption expected. MODE =  3"
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "4", "")[0]) >= 10, "No result encryption expected. MODE =  4"
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "1", "")) == 1, "Two values given, 1 expected"
    assert len(corechainex.encrypt(str(datetime.datetime.now()), 1, "1", "I want 2 values")) == 2, "1 value given, 2 expected"
    numoftests = 7
    for i in range(100):
        # repeat it 100 times with 0.025 s of delay each one.
        result = corechainex.encrypt(str(datetime.datetime.now())+str(i), 1, "1", "")
        assert [str(datetime.datetime.now())+str(i)] == corechainex.encrypt(result, 2, "1", ""), "Encrypt and decrypt worked encrypt-->decrypt."
        time.sleep(0.05)
        numoftests = numoftests+1
    return numoftests
print("ALL TESTS PASSED:", chainextest(numoftests))