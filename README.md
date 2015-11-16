[![Build Status](https://travis-ci.org/neuron-js/pyneuron.svg?branch=master)](https://travis-ci.org/neuron-js/pyneuron)

# pyneuronjs

Python utilities and middleware for neuron.js

pyneuronjs analyzes the dependencies from user defined facades according to the dependency tree, and output `<script>` tags and configurations for [neuron.js](https://github.com/kaelzhang/neuron) 

The dependency tree can be generated by [neuron-package-dependency](https://github.com/neuron-js/neuron-package-dependency)

## Install

```sh
$ pip install pyneuronjs
```

## Usage

```py
from pyneuronjs import Neuron

n = Neuron(
  dependency_tree=dependency_tree,  # must defined
  resolve=resolve
  version=version,                  
  cache=cache,
  debug=False
)
```

- **dependency_tree** `dict` the `json.loads()`ed dependency tree
- **resolve** `function(id)=` (optional) implements your own custom resolver. `resolve` accepts one parameter `id` which can be either a `str` of module id or a `list` of module ids. If a `str` is passed in, the method should returns the resolved absolute url of the module id. If `id` is a `list`, an url of comboed script files should be returned.
- **debug** `function|bool=False` tells pyneuronjs whether should switch on debug mode. When on debug mode, no javascript files of dependencies will be preloaded, and the output will not be compressed.
  - if `debug` is callable, pyneuronjs will use the return value of method `debug`
  - if `debug` is a boolean value, and `debug` is true, the debug mode will be on.
- **cache** `dict=None` if `cache` is defined, it should contains 3 methods:
  - `cache.has(key)` returns `bool`
  - `cache.get(key)` looks up and returns the cached value by key
  - `cache.set(key, value)` sets the value by key
- **version** `str` only works if `cache` is defined. pyneuronjs will uses `version`
to generate the key to cache the output result

#### module id

```js
<name>@<version><path>  # for example: 'jquery@2.0.0/jquery.js'
```

#### n.facade(entry, data)

#### n.combo(id...)

#### n.css(id)

#### n.output()

#### n.output_css()

## License

MIT
