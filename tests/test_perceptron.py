import sys
import pytest
import os
import platform 

sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "Error in .predict(), Input [1,1] does not equal 1 and it should."
    assert the_perceptron.predict([1,0]) ==  1, "Error in .predict(). Input [1,0] does not equal 1 and it should."
    assert the_perceptron.predict([0,1]) ==  1, "Error in .predict(). Input [0,1] does not equal 1 and it should."
    assert the_perceptron.predict([0,0]) ==  0, "Error in .predict(). Input [0,0] does not equal 0 and it should."

@pytest.mark.xfail
def test_perceptron_2():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])
    if the_perceptron.predict != 1:
       pytest.fail(f'Error in .predict(). Input [0,0] does not equal 0 and it should.')

@pytest.mark.skipif(platform.system() != 'Linux', reason ="requires linux ubuntu")
def test_perceptron_3():
    total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])


    assert total_memory >= used_memory, "Memory capacity reached"

@pytest.mark.skipif(True, reason = "This test is not yet ready for prime time.")
def test_perceptron_4():
    return "Hello, World!"


@pytest.mark.parametrize("training_set, labels, expected",
        [
            ([[5,-1],[2,-1],[0,-1],[-2,-1]],[1,0,0,0],[1,0,0,0]),
            ([[5,-1],[2,-1],[0,-1],[-2,-1]],[1,0,0,0],[1,0,0,0]),
            ([[5,-1],[2,-1],[0,-1],[-2,-1]],[1,0,0,0],[1,0,0,0]),
            ([[5,-1],[2,-1],[0,-1],[-2,-1]],[1,0,0,0],[1,0,0,0]),
            ([[5,-1],[2,-1],[0,-1],[-2,-1]],[1,0,0,0],[1,0,0,0]),
        ],
        )
def test_perceptron_final(training_set, labels, expected):
    the_perceptron = Perceptron()
    the_perceptron.train(training_set, labels)

    for i in range(len(training_set)):
        assert the_perceptron.predict(training_set[i]) == expected[i], f"Prediction {the_perceptron.predict(training_set[i])} does not match expected {expected[i]}"  
    

@pytest.fixture(scope='module')
def train_perceptron():
    training_set_init = [[5,-1],[2,-1],[0,-1],[-2,-1]]
    labels_init = [1,0,0,0]
    the_perceptron = Perceptron()
    the_perceptron.train(training_set_init, labels_init)
    return the_perceptron

@pytest.mark.parametrize("test_set,labels",
        [
            ([[5,-1],[2,-1],[0,-1],[-2,-1]],[1,0,0,0]),
            ],
        )

def test_perceptron_extra_credit(train_perceptron, test_set, labels):
    for i in range(len(test_set)):
        assert train_perceptron.predict(test_set[i]) == labels[i], "fail"

