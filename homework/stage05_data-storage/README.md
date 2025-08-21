## Data Storage

### Folder Structure
We organize data into two main folders:
- `data/raw/`: stores raw input data (e.g., CSV files). These files are human-readable and serve as the original, reproducible source.
- `data/processed/`: stores processed data (e.g., Parquet files). These files are optimized for analysis and efficient querying.

This separation ensures reproducibility: raw data is never overwritten, while processed data can be regenerated.

### Formats Used
- **CSV**: widely supported, easy to inspect manually, suitable for small datasets and interchange.
- **Parquet**: a columnar storage format with better compression and performance. It supports efficient queries (e.g., column pruning, partitioning) and scales better for larger datasets.

We save raw data as CSV (in `data/raw/`) and processed data as Parquet (in `data/processed/`).

### Environment-Driven Paths
Paths are configured via environment variables defined in `.env`:

DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed