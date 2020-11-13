from src.server.core.dl import deeplearning as dl

import pytest


@pytest.fixture()
def deeplearning():
    return dl.DeepLearning()


def test_1(deeplearning):
    assert deeplearning.analyze("Fructuti gura mentei") is None


def test_2(deeplearning):
    assert deeplearning.analyze("Hey pastarnacule") is None
