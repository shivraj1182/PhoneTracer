# PhoneTracer
A cybersecurity OSINT tool for gathering intelligence about phone numbers from publicly available sources

## 🔍 Overview

PhoneTracer is an Open Source Intelligence (OSINT) tool designed for security researchers and professionals to gather publicly available information about phone numbers. This tool aggregates data from various legitimate sources to help with:

- 🕵️ Security investigations
- 🛡️ Fraud detection
- 🔐 Threat intelligence gathering
- 📊 Data enrichment for security operations

> **⚠️ Important**: This tool is for legal and ethical use only. Always obtain proper authorization before conducting investigations.

## ✨ Features

- **Multi-Source Intelligence Gathering**: Query multiple public databases and APIs
- **Carrier Information**: Identify the telecom carrier and network type
- **Geolocation Data**: Approximate location based on phone number prefix
- **Spam/Scam Detection**: Check against known spam/scam databases
- **Format Validation**: Validate phone number formats across different countries
- **OSINT Integration**: Integration with popular OSINT frameworks
- **Export Options**: Export results in JSON, CSV, or HTML formats
- **Rate Limiting**: Built-in rate limiting to respect API usage policies

## 🎯 Use Cases

1. **Security Operations**: Investigate suspicious phone numbers in security incidents
2. **Fraud Prevention**: Verify phone numbers during customer onboarding
3. **Threat Intelligence**: Build profiles of phone numbers associated with threats
4. **OSINT Research**: Gather intelligence as part of broader investigations
5. **Compliance**: Verify contact information for regulatory compliance

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/shivraj1182/PhoneTracer.git
cd PhoneTracer

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys (if needed)
cp config.example.yml config.yml
# Edit config.yml with your API keys

# Run the tool
python phonetracer.py --help
```

## 📖 Usage

### Basic Usage

```bash
# Query a single phone number
python phonetracer.py +1234567890

# Query with specific modules
python phonetracer.py +1234567890 --modules carrier,location,spam

# Export results to JSON
python phonetracer.py +1234567890 --output results.json

# Batch processing from file
python phonetracer.py --batch phone_numbers.txt
```

### Advanced Options

```bash
# Verbose output
python phonetracer.py +1234567890 -v

# Use specific data sources
python phonetracer.py +1234567890 --sources numverify,twilio

# Set timeout for queries
python phonetracer.py +1234567890 --timeout 30

# Export to multiple formats
python phonetracer.py +1234567890 --output-format json,csv,html
```

## 🔌 Data Sources

PhoneTracer can integrate with various public and commercial data sources:

- **NumVerify API**: Phone number validation and carrier lookup
- **Twilio Lookup**: Carrier and caller ID information  
- **OpenCNAM**: Caller ID name lookup
- **IPQualityScore**: Fraud detection and risk scoring
- **Phonevalidator**: Number validation and type detection
- **Local Number Portability (LNP) databases**: Carrier information

> Note: Some data sources require API keys. See configuration section.

## ⚙️ Configuration

Create a `config.yml` file in the project root:

```yaml
api_keys:
  numverify: "your_api_key_here"
  twilio_sid: "your_twilio_sid"
  twilio_token: "your_twilio_token"
  opencnam: "your_opencnam_key"
  ipqualityscore: "your_ipqs_key"

settings:
  timeout: 30
  rate_limit: 60  # requests per minute
  cache_enabled: true
  cache_ttl: 3600  # seconds
  
output:
  default_format: json
  verbose: false
  save_to_file: true
```

## 🏗️ Project Structure

```
PhoneTracer/
│
├── phonetracer.py          # Main application entry point
├── requirements.txt        # Python dependencies
├── config.yml             # Configuration file
├── README.md              # This file
├── LICENSE                # MIT License
│
├── modules/               # Data source modules
│   ├── __init__.py
│   ├── carrier.py         # Carrier lookup module
│   ├── geolocation.py     # Location detection module
│   ├── spam_check.py      # Spam/scam detection
│   └── validator.py       # Number validation
│
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── formatter.py       # Output formatting
│   ├── parser.py          # Phone number parsing
│   └── cache.py           # Caching mechanisms
│
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── test_modules.py
│   └── test_utils.py
│
└── docs/                  # Documentation
    ├── API.md
    ├── CONTRIBUTING.md
    └── examples/
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=phonetracer tests/

# Run specific test file
python -m pytest tests/test_modules.py
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct and development process.

## 📋 Roadmap

- [ ] Add support for international number formats
- [ ] Implement machine learning for spam detection
- [ ] Create web interface for easier access
- [ ] Add support for bulk processing with progress tracking
- [ ] Integration with threat intelligence platforms
- [ ] Real-time monitoring capabilities
- [ ] Mobile application
- [ ] API endpoint for integration with other tools

## ⚖️ Legal & Ethics

**Important Legal Notice:**

- This tool is intended for legal and ethical use only
- Always obtain proper authorization before investigating phone numbers
- Respect privacy laws and regulations (GDPR, CCPA, etc.)
- Do not use this tool for harassment, stalking, or illegal activities
- The developers are not responsible for misuse of this tool
- Some features may require compliance with local telecommunications regulations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all open-source OSINT projects that inspired this tool
- Contributors and security researchers who provided feedback
- The Python community for excellent libraries and frameworks

## 📧 Contact

- GitHub: [@shivraj1182](https://github.com/shivraj1182)
- Issues: [GitHub Issues](https://github.com/shivraj1182/PhoneTracer/issues)

## 🔗 Related Projects

- [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) - Advanced phone number OSINT tool
- [Sherlock](https://github.com/sherlock-project/sherlock) - Username OSINT tool
- [theHarvester](https://github.com/laramies/theHarvester) - Email, subdomain and people OSINT

---

**Disclaimer**: This tool is for educational and professional security research purposes only. Users are responsible for ensuring their use complies with all applicable laws and regulations.
