# Part 2

## Follow along

1. `touch requirements.txt`
2. `mkdir src`
3. `touch src/main.py`
4. `mkdir src/smokeTest`
5. `touch src/smokeTest/router.py`
6. `echo "from .router import *" >> src/smokeTest/__init__.py`
7. `pip install -r requirements.txt`
8. SMOKE TEST the "Dev Container"
    - `uvicorn src.main:app --host 0.0.0.0 --port 4000 --reload`
    - `curl http://localhost:4000/smoke-test/hello-world`
9. BREAKPOINT DEBUGGING the "Dev Container"
    - `code --install-extension ms-python.python`
    - `code --install-extension ms-python.debugpy`

## Reference links

- https://fastapi.tiangolo.com/
- https://code.visualstudio.com/docs/python/debugging

## Troubleshooting

Need to manually kill the breakpoint debugging server?

```.sh
netstat -nlp|grep 5678
kill <PID>
```

Need to stop, delete, and rebuild the "Dev Container" as things didn't behave as expected?

Check out the "Docker Desktop" GUI
