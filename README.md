# API Data Extraction Examples

This repository contains examples of API data extraction patterns commonly used in data engineering workflows, with specific focus on integration with Microsoft Fabric.

## Features

- Basic API client with error handling and DataFrame conversion
- Advanced API client with:
  - Concurrent execution
  - Rate limiting
  - Retry logic
  - Pagination handling
- MS Fabric integration for loading extracted data

## Installation

```bash
pip install -r requirements.txt
```

## Usage

The repository includes several key components:

### Basic API Client

```python
from src.basic_api_client import BaseAPIClient

client = BaseAPIClient('https://api.example.com/v1', 'your_api_key')
data = client.get('users')
df = client.extract_to_dataframe('users')
```

### Advanced API Client

```python
from src.advanced_api_client import AdvancedAPIClient

client = AdvancedAPIClient('https://api.example.com/v1', 'your_api_key')
async def main():
    data = await client.batch_extract(['users/1', 'users/2'])
```

### MS Fabric Integration

```python
from src.fabric_integration import FabricLoader

loader = FabricLoader('your_connection_string')
loader.load_to_fabric(df, 'target_table')
```

## Best Practices

1. **Error Handling**: All API calls include proper error handling and logging
2. **Rate Limiting**: Implement rate limiting to respect API constraints
3. **Incremental Loading**: Support for incremental data extraction
4. **Type Hints**: Code includes type hints for better maintainability
5. **Asynchronous Operations**: Efficient handling of multiple API calls

## MS Fabric Integration

The repository includes specific support for MS Fabric integration:

1. Automatic table creation based on DataFrame schema
2. Proper data type mapping between pandas and SQL
3. Batch loading support
4. Error handling and logging

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.