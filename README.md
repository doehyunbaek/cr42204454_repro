# Local repro of https://issues.chromium.org/issues/42204454

uarm_web.wasm is built from 

https://github.com/cloudpilot-emu/cp-uarm/commit/6e6034d8087923ff330a08064cafec8a1f8474c3 

with command

```bash
make emscripten
# at src/uarm_web.wasm
```

main.wasm is captured with [wasm-r3](https://github.com/jakobgetz/wasm-r3/) then modified manually.

run.js is a modification of [run.js in wish-you-were-fast repo](https://github.com/composablesys/wish-you-were-fast/blob/65c968685d66eea3ae88ef747df95210690c6b46/wasm/engines/run.js#L4) to supply imports to uarm_web.wasm.

To prepare the test input, run

```bash
wasm-merge --rename-export-conflicts --enable-reference-types --enable-multimemory --enable-bulk-memory --enable-threads --debuginfo manual_main.wasm main uarm_web.wasm index -o diff.wasm
```