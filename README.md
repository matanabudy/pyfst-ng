# pyfst
Python interface to [OpenFst](https://openfst.org).
This is based on the original PyFST repository by [vchahun](https://github.com/vchahun/pyfst), and the modifications done by [placebokkk](https://github.com/placebokkk/pyfst)

Documentation: http://pyfst.github.io

## Installation
1. Install [OpenFst 1.7.9](https://openfst.org)
2. Clone the repository and run `python setup.py install`

## Known Issues
- Works until OpenFST 1.7.9

## Basic Usage
```python
import fst

t = fst.Transducer()

t.add_arc(0, 1, 'a', 'A', 0.5)
t.add_arc(0, 1, 'b', 'B', 1.5)
t.add_arc(1, 2, 'c', 'C', 2.5)

t[2].final = 3.5

t.shortest_path() # 2 -(a:A/0.5)-> 1 -(c:C/2.5)-> 0/3.5 
```

The pyfst API is [IPython notebook](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html)-friendly: the transducers objects are [automatically drawn](http://nbviewer.ipython.org/3835477/) using [Graphviz](http://www.graphviz.org).

## Development

See [the wiki](https://github.com/vchahun/pyfst/wiki/Contributing) to learn about how to install pyfst from the Cython source.

## License

Copyright 2013 Victor Chahuneau

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
