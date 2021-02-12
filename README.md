# flask-tutorial
A tutorial on using flask including a working fieldnotes API.


### Requires
```bash
conda install flask flask-restful -c conda-forge
```

### To run

```bash
cd flask-tutorial
export FLASK_APP="src/app-0.py"
export FLASK_DEBUG=1
flask run
```

### endpoints for app-0
http://localhost:5000

### endpoints for app-1
http://localhost:5000
http://localhost:5000/string/int/int/int

### endpoints for app-2
http://localhost:5000
http://localhost:5000/string/int/int/int

### endpoints for app-3
http://localhost:5000/?
http://localhost:5000/api/?

required Rest API arguments:
- name=string
- year=int
- month=int
- day=int

### endpoints for app-4
http://localhost:5000/?
http://localhost:5000/api/?

optional Rest API arguments:
- genus=string  
- epithet=string
- locality=int
- accession=string
