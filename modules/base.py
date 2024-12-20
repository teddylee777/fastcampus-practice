from typing import Any, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar("T")  # 제네릭 타입 변수 정의


class BaseTool(ABC, Generic[T]):
    """도구들의 기본 클래스"""

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """도구 초기화를 위한 추상 메서드"""
        pass

    @abstractmethod
    def _create_tool(self) -> T:
        """실제 도구 객체를 생성하는 추상 메서드"""
        pass

    @classmethod
    def create(cls, *args: Any, **kwargs: Any) -> T:
        """도구 객체를 생성하고 바로 반환하는 팩토리 메서드"""
        instance = cls(*args, **kwargs)
        tool = instance._create_tool()
        return tool

    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """도구를 실행하는 추상 메서드"""
        pass
