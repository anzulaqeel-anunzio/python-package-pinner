# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from linter.core import VersionPinner

def main():
    parser = argparse.ArgumentParser(description="Package.json Version Pinner Checker")
    parser.add_argument("path", help="Directory or file to scan (defaults to current dir)", nargs='?', default=".")
    
    args = parser.parse_args()
    path = os.path.abspath(args.path)
    
    issues = []
    
    if os.path.isfile(path) and path.endswith('package.json'):
        issues = VersionPinner.check_package_json(path)
    elif os.path.isdir(path):
        issues = VersionPinner.scan_directory(path)
    else:
        if os.path.isfile(path):
            print("Error: Target file is not a package.json")
        else:
             print(f"Error: Path '{path}' not found.")
        sys.exit(1)
        
    if not issues:
        print("All dependencies are pinned! determinism++")
        sys.exit(0)
        
    print(f"Found {len(issues)} unpinned dependencies:\n")
    for issue in issues:
        print(f"[{issue['file']}] {issue['pkg']}: {issue['ver']} ({issue['type']})")
        
    sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
