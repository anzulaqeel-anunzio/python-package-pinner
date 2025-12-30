# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
import os

class VersionPinner:
    # We want versions to NOT start with ^ or ~ or > or <
    # We want exact versions like "1.2.3" or "0.0.1"
    
    @staticmethod
    def is_pinned(version):
        version = version.strip()
        if not version: return False
        
        # Ignored specific cases
        if version == "*" or version == "latest": return False
        if version.startswith(( '^', '~', '>', '<' )):
            return False
            
        return True

    @staticmethod
    def check_package_json(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            dep_types = ['dependencies', 'devDependencies', 'peerDependencies', 'optionalDependencies']
            
            for dtype in dep_types:
                if dtype in data:
                    for pkg, ver in data[dtype].items():
                        if not VersionPinner.is_pinned(ver):
                            issues.append({
                                'file': filepath,
                                'pkg': pkg,
                                'ver': ver,
                                'type': dtype,
                                'msg': f"Dependency '{pkg}' is not pinned (found: {ver})"
                            })
                            
        except json.JSONDecodeError:
             return [{'file': filepath, 'pkg': 'N/A', 'ver': 'N/A', 'type': 'Error', 'msg': 'Invalid JSON format'}]
        except Exception as e:
             return [{'file': filepath, 'pkg': 'N/A', 'ver': 'N/A', 'type': 'Error', 'msg': str(e)}]
             
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file == 'package.json':
                    path = os.path.join(root, file)
                    issues = VersionPinner.check_package_json(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
