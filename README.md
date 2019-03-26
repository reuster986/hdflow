# Hdflow: Convert CSV Netflow to HDF5 in Parallel

Command line usage:

```bash
csv2hdf --formats-file=my_formats.py --format=sample /path/to/netflow/files/*.csv
```

## Defining Formats

Hdflow uses `pandas.read_csv()` to parse input files. The keyword arguments passed to `pandas.read_csv()` come from the formats-file via the module-level variable `OPTIONS`, which must be a dictionary mapping names of netflow formats to dictionaries containing their keyword arguments. See the included `lanl_format.py` for an example. 
