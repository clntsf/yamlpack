# yamlpack
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

## TODOs:

- [ ] *(Compat)*: Ensure filesystem operations work cross-platform and migrate them if not.

- [ ] *(CLI)*: Map out and implement a set of actions/subparsers

- [ ] *(CLI)*: Implement CLI for main and alt flows

- [ ] *(Builders)*: Decide on a builder protocol, populate the sample repo and link it

- [x] *(Config)*: Refactor config get and update functions to ensure write destination is in user data folder

## Milestones:

31 July 2025: 0.1.0 is the first version uploaded to [PyPI](https://pypi.org/project/yamlpack/) :partying_face: