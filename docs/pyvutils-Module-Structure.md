# `pyvutils` Module Structure

```
pyvutils
├─ asserts
│  ├─ currency
│  │  ├─ assert_currency_code
│  │  ├─ assert_alphabetic_currency_code
│  │  ├─ assert_numeric_currency_code
│  └─ input
│     └─ assert_input
├─ checkers
├─ converters
│  └─ numerics
│     ├─ decimal_to_numeric
│     ├─ numeric_str_to_numeric
│     └─ normalize_numeric
├─ decimalkit
│  └─ round
│     ├─ round_down
│     └─ round_up
├─ dtutils
│  └─ stamps
│     ├─ current_date_stamp
│     ├─ current_month_stamp
│     └─ current_year_stamp
├─ filekit
├─ listutils
│  └─ processors
│     ├─ flatten
│     └─ remove_duplicates
├─ parsers
│  └─ numerics
│     ├─ parse_numeric
│     ├─ parse_integer
│     └─ parse_float
├─ pathkit
├─ projectkit
│  ├─ fileops
│  │  ├─ read_project_file
│  │  ├─ write_project_file
│  │  ├─ get_json
│  │  └─ save_json
│  └─ pathworks
│     ├─ get_project_path
│     ├─ get_project_relative_path
│     └─ get_project_relative_filepath
├─ strutils
│  ├─ splitters
│  │  ├─ split_by_char
│  │  ├─ split_by_comma
│  │  ├─ split_by_colon
│  │  ├─ split_by_semicolon
│  └─ transformers
│     └─ custom_title 
└─ validators
   ├─ currency
   │  ├─ valid_currency_code
   │  ├─ valid_alphabetic_currency_code
   │  └─ valid_numeric_currency_code
   └─ numerics
      └─ valid_numeric

```