# yaml-pkg
Package boilerplate creator using YAML schemas

## Sample Schema:

Users can generate a package using simple, quickly-written
YAML schemas as below: 
Properties are given for name and description, and the module
structure is written in a simple syntax

```yaml
# package name and description for setup.py
name: my-package
description: my very first package!

# here we list a filestructure-like module structure,
# where an item is a string if it has no children
# and an object if it has children. The toplevel is
# always "modules"
modules:
  - module_one
  - module_two:
      - submodule_one
  - module_three
```