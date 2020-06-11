# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = nodes_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Position:
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'Position':
        assert isinstance(obj, dict)
        x = from_int(obj.get("x"))
        y = from_int(obj.get("y"))
        return Position(x, y)

    def to_dict(self) -> dict:
        result: dict = {}
        result["x"] = from_int(self.x)
        result["y"] = from_int(self.y)
        return result


@dataclass
class Node:
    title: str
    tags: str
    body: str
    position: Position
    color_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Node':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        tags = from_str(obj.get("tags"))
        body = from_str(obj.get("body"))
        position = Position.from_dict(obj.get("position"))
        color_id = from_int(obj.get("colorID"))
        return Node(title, tags, body, position, color_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["tags"] = from_str(self.tags)
        result["body"] = from_str(self.body)
        result["position"] = to_class(Position, self.position)
        result["colorID"] = from_int(self.color_id)
        return result


def nodes_from_dict(s: Any) -> List[Node]:
    return from_list(Node.from_dict, s)


def nodes_to_dict(x: List[Node]) -> Any:
    return from_list(lambda x: to_class(Node, x), x)
