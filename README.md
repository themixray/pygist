# PyGist
Manage gists with python
## Example
```python
import pygist

m = pygist.manager('token')

# Create gist
files = [
  pygist.file('Hello!','https://github.com/themixray/pygist')
  pygist.file('Second file','...')
]
r = m.create(files, 'Created by pygist', True)
print('Url:', r.html_url)
print('Raw url to first file:', r.files['Hello!']['raw_url'])

# Update gist
files = [
  pygist.file('Hello',r.html_url)
  pygist.file('Second file','...')
]
r = m.update(r.id, files, 'Created by pygist')

# Delete gist
r = m.delete(r.id)

# Get gist info
r = m.get('238b810bbc059f811eb7044bf7533ecc')
```
