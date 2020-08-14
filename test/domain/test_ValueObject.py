from fwl_ddd_seedwork import ValueObject
from test.BaseTest import BaseTest


class ExampleValueObject(ValueObject):
    def __init__(self, value: str):
        self.value = value


class TestValueObject(BaseTest):

    def test_ensure_creating_a_value_object_works(self):
        value_object = ValueObject()
        self.assertEqual(type(value_object), ValueObject)
        self.assertTrue(issubclass(ExampleValueObject, ValueObject))
        example_value_object = ExampleValueObject("value")
        self.assertEqual(example_value_object.value, "value")
        self.assertEqual(type(example_value_object), ExampleValueObject)
