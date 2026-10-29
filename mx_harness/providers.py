"""Provider contract and an offline demo implementation."""

from typing import Protocol


class Provider(Protocol):
    def generate(self, prompt: str) -> str:
        """Return a response for one prompt."""


class EchoProvider:
    """Deterministic provider used to demonstrate the harness without a model."""

    def generate(self, prompt: str) -> str:
        return f"Demo response: {prompt}"
