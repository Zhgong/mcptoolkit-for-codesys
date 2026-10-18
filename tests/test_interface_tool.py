"""Tests for codesys.pou.create_interface ToolSpec and schema validation."""
from __future__ import annotations

import pytest

from mcptoolkit_for_codesys.tools import REGISTRY


def test_create_interface_tool_registered():
    spec = REGISTRY.get("codesys.pou.create_interface")
    assert spec is not None, "codesys.pou.create_interface must be registered"
    assert spec.name == "codesys.pou.create_interface"
    assert callable(spec.handler)


def test_create_interface_schema():
    spec = REGISTRY.get("codesys.pou.create_interface")
    schema = spec.input_schema
    assert schema.get("type") == "object"
    assert "name" in schema.get("required", [])
    props = schema.get("properties", {})
    assert "name" in props
    assert "parent" in props
    assert "base_interfaces" in props
    assert "methods" in props


def test_pou_create_includes_interface():
    spec = REGISTRY.get("codesys.pou.create")
    assert spec is not None
    props = spec.input_schema.get("properties", {})
    assert "interface" in props.get("pou_type", {}).get("enum", [])
