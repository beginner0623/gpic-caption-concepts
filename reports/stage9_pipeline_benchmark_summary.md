# Stage 9 Pipeline Benchmark Summary

- date: `2026-06-28`
- pipeline: spaCy `en_core_web_trf` parse + Stage 8 raw concept extraction + Stage 9 canonical parent/fact generation
- benchmark input: `data/gpic_captions_eval/val/gpic_val_00000.jsonl.gz`
- benchmark mode: 100 source captions repeated to target size
- GPU: `prefer_gpu=True`, `gpu_enabled=True`
- CuPy workaround: `--cupy-include-dir .mamba/env/Lib/site-packages/cupy/_core/include --disable-cupy-reduction-accelerators`
- batch_size: `256`
- n_process: `1`
- enabled pipeline options: quote retokenize, tag-list parsing, object MWE merge, hyphen span merge
- serialization: `serialize_json=True`, so JSON serialization cost is included, but full JSONL disk write cost is not included

## Detailed 100-Case Reports

| dataset | detailed report | size |
|---|---|---:|
| `sample100 val00000` | `reports/case_detail_sample100_val00000_trf_stage9_canonical_parent_v1.md` | 807,008 bytes |
| `alt100 val00001` | `reports/case_detail_alt100_val00001_trf_stage9_canonical_parent_v1.md` | 787,042 bytes |

## Throughput Scaling

| target captions | run seconds | docs/sec | estimated 100M days | linear workers for 100M / 3 days | benchmark json |
|---:|---:|---:|---:|---:|---|
| 100 | 0.5943 | 168.2704 | 6.8783 | 2.2928 | `reports/stage9_pipeline_benchmark_val00000_100.json` |
| 1,000 | 7.1859 | 139.1606 | 8.3171 | 2.7724 | `reports/stage9_pipeline_benchmark_val00000_1000.json` |
| 10,000 | 60.3119 | 165.8048 | 6.9805 | 2.3268 | `reports/stage9_pipeline_benchmark_val00000_10000.json` |

## 10k Output Scale

| item | count |
|---|---:|
| records | 10,000 |
| sentence parse path | 7,900 |
| tag-list parse path | 2,100 |
| raw concept mentions | 137,700 |
| raw edges | 112,200 |
| canonical entities | 72,400 |
| canonical events | 20,800 |
| canonical relations | 32,800 |
| canonical facts | 199,200 |
| count-eligible facts | 197,300 |
| serialized JSON bytes | 202,233,794 |

## Interpretation

The stable local estimate is roughly `160 docs/sec` for the current end-to-end Stage 8+9 pipeline on one active GPU process.

At this speed, 100M captions would take about `7 days` on one equivalent worker. To finish 100M captions in 3 days, the measured linear requirement is about `2.3-2.8 equivalent workers`.

This benchmark does not yet measure multi-GPU sharding, full JSONL disk writing, or distributed I/O. Since the target environment has H200 x16, the parser itself is unlikely to be the only bottleneck; the next bottlenecks to test are sharding, output write format, and loading/compression overhead.
