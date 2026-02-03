#!/usr/bin/env python3
"""
PhoneTracer - OSINT Tool for Phone Number Intelligence

A cybersecurity OSINT tool for gathering intelligence about phone numbers
from publicly available sources.

Author: shivraj1182
License: MIT
"""

import argparse
import sys
import json
from typing import Dict, List, Optional
import logging
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PhoneTracer:
    """Main class for PhoneTracer application"""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize PhoneTracer
        
        Args:
            config_file: Path to configuration file
        """
        self.config = self._load_config(config_file)
        self.results = {}
        
    def _load_config(self, config_file: Optional[str]) -> Dict:
        """
        Load configuration from file
        
        Args:
            config_file: Path to configuration file
            
        Returns:
            Configuration dictionary
        """
        default_config = {
            'timeout': 30,
            'rate_limit': 60,
            'cache_enabled': True,
            'verbose': False
        }
        
        if config_file:
            try:
                with open(config_file, 'r') as f:
                    import yaml
                    user_config = yaml.safe_load(f)
                    default_config.update(user_config.get('settings', {}))
            except FileNotFoundError:
                logger.warning(f"Config file {config_file} not found. Using defaults.")
            except Exception as e:
                logger.error(f"Error loading config: {e}")
        
        return default_config
    
    def trace(self, phone_number: str, modules: Optional[List[str]] = None) -> Dict:
        """
        Trace phone number information
        
        Args:
            phone_number: Phone number to trace
            modules: List of modules to use (carrier, location, spam, validator)
            
        Returns:
            Dictionary containing gathered intelligence
        """
        logger.info(f"Tracing phone number: {phone_number}")
        
        results = {
            'phone_number': phone_number,
            'timestamp': self._get_timestamp(),
            'data': {}
        }
        
        # Parse and validate phone number
        parsed = self._parse_number(phone_number)
        if not parsed:
            logger.error("Invalid phone number format")
            return results
        
        results['data']['parsed'] = parsed
        
        # Determine which modules to run
        if modules is None:
            modules = ['validator', 'carrier', 'location']
        
        # Run each module
        for module_name in modules:
            try:
                module_result = self._run_module(module_name, phone_number)
                results['data'][module_name] = module_result
                logger.info(f"Module {module_name} completed")
            except Exception as e:
                logger.error(f"Error in module {module_name}: {e}")
                results['data'][module_name] = {'error': str(e)}
        
        self.results = results
        return results
    
    def _parse_number(self, phone_number: str) -> Optional[Dict]:
        """
        Parse phone number using phonenumbers library
        
        Args:
            phone_number: Phone number to parse
            
        Returns:
            Parsed number information or None
        """
        try:
            import phonenumbers
            parsed = phonenumbers.parse(phone_number, None)
            return {
                'country_code': parsed.country_code,
                'national_number': parsed.national_number,
                'is_valid': phonenumbers.is_valid_number(parsed),
                'is_possible': phonenumbers.is_possible_number(parsed)
            }
        except Exception as e:
            logger.error(f"Error parsing number: {e}")
            return None
    
    def _run_module(self, module_name: str, phone_number: str) -> Dict:
        """
        Run a specific intelligence module
        
        Args:
            module_name: Name of module to run
            phone_number: Phone number to analyze
            
        Returns:
            Module results
        """
        # This is a placeholder - actual implementation would import
        # and run the specific module from the modules/ directory
        return {
            'status': 'not_implemented',
            'message': f'Module {module_name} not yet implemented'
        }
    
    def _get_timestamp(self) -> str:
        """
        Get current timestamp
        
        Returns:
            ISO format timestamp
        """
        from datetime import datetime
        return datetime.utcnow().isoformat()
    
    def export_results(self, output_format: str = 'json', output_file: Optional[str] = None):
        """
        Export results to file
        
        Args:
            output_format: Format (json, csv, html)
            output_file: Output file path
        """
        if not self.results:
            logger.warning("No results to export")
            return
        
        if output_format == 'json':
            output = json.dumps(self.results, indent=2)
        else:
            logger.warning(f"Format {output_format} not yet implemented")
            output = json.dumps(self.results, indent=2)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(output)
            logger.info(f"Results exported to {output_file}")
        else:
            print(output)


def print_banner():
    """Print application banner"""
    banner = f"""{Fore.CYAN}
    ╔═══════════════════════════════════════════════╗
    ║          PhoneTracer v1.0.0                   ║
    ║   OSINT Tool for Phone Number Intelligence    ║
    ║                                               ║
    ║   Author: shivraj1182                         ║
    ║   License: MIT                                ║
    ╚═══════════════════════════════════════════════╝
    {Style.RESET_ALL}
    """
    print(banner)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='PhoneTracer - OSINT Tool for Phone Number Intelligence',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'phone_number',
        nargs='?',
        help='Phone number to trace (e.g., +1234567890)'
    )
    
    parser.add_argument(
        '--modules', '-m',
        nargs='+',
        help='Specific modules to run (carrier, location, spam, validator)'
    )
    
    parser.add_argument(
        '--config', '-c',
        help='Path to configuration file'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file path'
    )
    
    parser.add_argument(
        '--format', '-f',
        choices=['json', 'csv', 'html'],
        default='json',
        help='Output format (default: json)'
    )
    
    parser.add_argument(
        '--batch', '-b',
        help='Batch process from file (one phone number per line)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='PhoneTracer 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Print banner
    print_banner()
    
    # Check if phone number or batch file is provided
    if not args.phone_number and not args.batch:
        parser.print_help()
        sys.exit(1)
    
    # Initialize PhoneTracer
    tracer = PhoneTracer(config_file=args.config)
    
    try:
        if args.batch:
            # Batch processing
            logger.info(f"Batch processing from {args.batch}")
            with open(args.batch, 'r') as f:
                phone_numbers = [line.strip() for line in f if line.strip()]
            
            all_results = []
            for phone_number in phone_numbers:
                print(f"\n{Fore.GREEN}[*] Processing: {phone_number}{Style.RESET_ALL}")
                result = tracer.trace(phone_number, modules=args.modules)
                all_results.append(result)
            
            # Export batch results
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(all_results, f, indent=2)
                logger.info(f"Batch results exported to {args.output}")
        else:
            # Single number processing
            results = tracer.trace(args.phone_number, modules=args.modules)
            
            # Export results
            tracer.export_results(
                output_format=args.format,
                output_file=args.output
            )
        
        print(f"\n{Fore.GREEN}[✓] Operation completed successfully{Style.RESET_ALL}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Operation cancelled by user{Style.RESET_ALL}")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Error: {e}")
        print(f"{Fore.RED}[✗] An error occurred. Check logs for details.{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == '__main__':
    main()
