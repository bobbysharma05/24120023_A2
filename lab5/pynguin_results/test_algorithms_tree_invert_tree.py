# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.tree.invert_tree as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    var_0 = module_0.reverse(none_type_0)
    bool_0 = False
    module_0.reverse(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 0.1
    module_0.reverse(float_0)
