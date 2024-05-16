# Local repro of https://issues.chromium.org/issues/42204454

uarm_web_6e6034d8087923ff330a08064cafec8a1f8474c3 is built from 

https://github.com/cloudpilot-emu/cp-uarm/commit/6e6034d8087923ff330a08064cafec8a1f8474c3 

with command

```bash
make emscripten
# at src/uarm_web.wasm
```

main.wasm is captured with [wasm-r3](https://github.com/jakobgetz/wasm-r3/) then modified manually.