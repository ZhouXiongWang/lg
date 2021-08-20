import pytest
import yaml


class Test_calc:
    # string参数化
    @pytest.mark.parametrize('a,b', [(1, 2), (2, 3), (3, 4)])
    def test_jf(self, a, b):
        print(a + b)

    # list参数化
    @pytest.mark.parametrize(['a', 'b'], [(1, 2), (2, 3), (3, 4)])
    def test_jf1(self, a, b):
        print(a + b)

    # 元组参数化
    @pytest.mark.parametrize(("a", "b"), [(1, 2), (2, 3), (3, 4)])
    def test_jf2(self, a, b):
        print(a + b)

    # 引用yaml
    @pytest.mark.parametrize(("a", "b","c"), yaml.safe_load(open("./Data.yaml")))
    def test_jfyaml(self, a, b,c):
        print(f"{a}+{b}={c}")
pytest