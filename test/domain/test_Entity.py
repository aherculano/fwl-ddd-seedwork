from fwl_ddd_seedwork import Entity
from test.BaseTest import BaseTest


class ExampleEntity(Entity):
    def __init__(self, example_value: str):
        self.example_value: str = example_value


class TestEntity(BaseTest):

    def test_ensure_creating_a_entity_works(self):
        entity = Entity()
        self.assertEqual(type(entity), Entity)

    def test_ensure_changing_a_entity_orm_id_works(self):
        entity = Entity()
        self.assertEqual(entity.id, None)
        entity.id = 1
        self.assertEqual(entity.id, 1)

    def test_ensure_extending_entity_works(self):
        self.assertTrue(issubclass(ExampleEntity, Entity))

    def test_ensure_example_entity_has_id_field(self):
        entity = ExampleEntity("example")
        self.assertEqual(entity.id, None)
        entity.id = 1
        self.assertEqual(entity.id, 1)
